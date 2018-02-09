---
title: ChiralData
permalink: /ChiralData/
---

The OBChiralData class is a [Generic Data](/Generic_Data "wikilink") class used to hold and access the chirality data of a particular atom -- listings of 4atomrefs for its neighbours in the input format, and output format.

` bool OBChiralData::SetAtom4Refs(std::vector`<unsigned int>` atom4refs, atomreftype t)`

is used to set a vector of length 4 as the atom references. (atomreftype is an enum which can be set to input, output or calcvolume, these are 3 seperate vectors which can be stored on the atom)

` int OBChiralData::AddAtomRef(unsigned int atomref, atomreftype t)`

is used to add (pushback) a refernce to the vector. There is no error checking that it doesn't grow beyond size 4 so the code using it should make sure it dosen't add more than 4 or error checking should be added.

` unsigned int OBChiralData::GetAtomRef(int a, atomreftype t)`

returns the atom number specified by int a.(I don't think I used this, but it might be usefull in the future)

` std::vector`<unsigned int>` OBChiralData::GetAtom4Refs(atomreftype t) const`

returns a vector of the atomrefs stored in the OBChiralData of atomreftype t.

` unsigned int OBChiralData::GetSize(atomreftype t) const`

returns the size of atomreftype t

Funtions in chiral.cpp:

` int GetParity4Ref(vector`<unsigned int>` pref)`

returns either 0 or 1 depending on the parity of the vector(of length 4) it is given. 1234 returns 0 while 1243 returns 1.

` bool CorrectChirality(OBMol &mol, OBAtom *atm, atomreftype i, atomreftype o)`

this looks at the asociated OBChiralData for the atom and checks if its input and output parity are the same. If they are not then it inverts the ClockWise/AntiClockwise stereo of the atom.

HasChiralityPerceived() is a flag which is checked before mol.FindChiralCenters() is run, it should probably be set in all formats after reading in chiral data.

Exampe Code: plucked from the V3000 MDL format

    #include "chiral.h"
    using namespace std;
    namespace OpenBabel {
    class MOLFormat : public OBMoleculeFormat
    {
    map<OBAtom*,OBChiralData*> _mapcd; // map of ChiralAtoms and their data. This is needed to avoid losing data when mol.EndModify() is called.

    bool MOLFormat::ReadMolecule(OBBase* pOb, OBConversion* pConv)
    {
    _mapcd.clear();
    *while reading in an atom and finding the stero flag*
               {
                   //Stereo configuration: 0 none; 1 odd parity; 2 even parity; (3 either parity)
                   if(val==2) atom.SetAntiClockwiseStereo();
                   else if(val==1) atom.SetClockwiseStereo();
                   chiralWatch=true;
    *after adding creating atom, add its number to the _mapcd so it can be checked for in the bond table later and its neighbours added mol.NumAtoms() returns the ID of the most recent atom, other formats might need to do this differently*
    if(chiralWatch)_mapcd[mol.GetAtom(mol.NumAtoms())]= new OBChiralData; // fill the map with chrial data for each chiral atom

    *while reading in bond data*
    *this checks when a bond is made if the atom ID is in the chiralmap, and if so adds the neighbour to the atomrefs. This will be processed in the order of the bond table which is the order which matters for how MDL chirality is defined, needs to check both start and end atom as bonds are only listed once*
    if (!mol.AddBond(obstart,obend,order,flag)) return false;
             // after adding a bond to atom "obstart"
        // search to see if atom is bonded to a chiral atom
           map<OBAtom*,OBChiralData*>::iterator ChiralSearch;
           ChiralSearch = _mapcd.find(mol.GetAtom(obstart));
           if (ChiralSearch!=_mapcd.end())
           {
              (ChiralSearch->second)->AddAtomRef(obend, input);
           }
        // after adding a bond to atom "obend"
        // search to see if atom is bonded to a chiral atom
           ChiralSearch = _mapcd.find(mol.GetAtom(obend));
           if (ChiralSearch!=_mapcd.end())
           {
              (ChiralSearch->second)->AddAtomRef(obstart, input);
           }
       }

    *after the molecule is finished reading in need to add the chiral data to the atoms, has to be done after EndModify() as that wipes generic data for some reason*
       mol.EndModify();
      //We now add the OBChiralData stored inside the _mapcd to the atoms after end
       // modify so they don't get lost.
       if(_mapcd.size()>0)
       {
       OBAtom* atom;
       OBChiralData* cd;
       map<OBAtom*,OBChiralData*>::iterator ChiralSearch;
          for(ChiralSearch=_mapcd.begin();ChiralSearch!=_mapcd.end();ChiralSearch++)
          {
           atom=ChiralSearch->first;
           cd=ChiralSearch->second;
           atom->SetData(cd);
          }      }

    **Writing**
    *if the atom is chiral then it needs to generate the Atom4Refs output and compare it with the input ones. Each format will have a different defination of how it counts chirality so will need to generate its own atom4refs output.*
       if(atom->IsChiral())
           {
            // MOLV3000 uses 1234 unless an H then 123H
                   OBChiralData* cd=(OBChiralData*)atom->GetData(OBGenericDataType::ChiralData);
            if(!cd){ //if no Chiral Data Set, need to make one!
                    cd=new OBChiralData;
                    atom->SetData(cd);
                    }
                if (atom->GetHvyValence()==3) // If there are only 3heavy atoms, then need to sort them into ID //order 123H so make large number (mol.numatoms()+1) to go at the end.)
                {
                   OBAtom *nbr;
                   int Hid = (mol.NumAtoms()+1) ;// max Atom ID +1
                   vector<unsigned int> nbr_atms;
                   vector<OBEdgeBase*>::iterator i;
                   for (nbr = atom->BeginNbrAtom(i);nbr;nbr = atom->NextNbrAtom(i))
                   {
                       if (nbr->IsHydrogen()){Hid=nbr->GetIdx();continue;}
                       nbr_atms.push_back(nbr->GetIdx());
                   }
                   sort(nbr_atms.begin(),nbr_atms.end());
                   nbr_atms.push_back(Hid);
                   cd->SetAtom4Refs(nbr_atms,output);   // This saves the output atom4refs calculated above
                }
                else if (atom->GetHvyValence()==4)
                {
                   vector<unsigned int> nbr_atms;
                   int n;
                   for(n=1;n<5;n++)nbr_atms.push_back(n);
                   cd->SetAtom4Refs(nbr_atms,output); //Saves the output atom4refs for if all heavy(1234)
                }

    *If it has co-ordinates then we can calculate the signed volume which stores the atom4refs used in the calculation and its result. This can then be compared to the output order and the corretchirality worked out. At the moment this overides input chirality, rather than checking for a conflict with input chirality (which might be a usefull check)*
           double vol=0;         if (mol.HasNonZeroCoords())
            {
               vol=CalcSignedVolume(mol,atom);
               if (vol > 0.0)atom->SetClockwiseStereo();
               else if(vol < 0.0)atom->SetAntiClockwiseStereo();
               CorrectChirality(mol,atom,calcvolume,output);
            }

    *If no co-ords, then use the atom4refs defined by the input format*
            else {                        CorrectChirality(mol,atom); // will set the stereochem based on input/output atom4refs
                 }

               int cfg=0;
               if(atom->IsClockwise())cfg=1;
               else if(atom->IsAntiClockwise())cfg=2;
                         ofs << " CFG=" << cfg;

[Category:Developer](/Category:Developer "wikilink")