---
title: Adding new commandline options
permalink: /Adding_new_commandline_options/
---

The `babel` command line has the form:

      babel inputfile [outputfile] [options]

There are several types of options: some, like -i, -o, -m, etc, control the conversion process; those with-a and -x prefixes are used by the input and output formats respectively. The ones of interest here are the 'general' formats. These can be single letter options, like -c (which centers coordinates), or multi-character options like --separate (which makes separate molecules from disconnected fragments). They usually operate on the a molecule after it has been read by the input format and before it has been written by the output format. The ones mentioned are hardwired into the code, but it is possible to define new options which work in a similar way using the OBOp class, which is a plugin class so that there is no need to alter any existing code to deploy it.

The OBOp class
--------------

The name is intended to imply an operation as well as an option. The ops that are installed can be found using

      babel -L ops

or in the plugins memnu item in the GUI. An example is the --gen3D option, which adds 3D coordinates to a molecule.

    class OpGen3D : public OBOp
    {
    public:
      OpGen3D(const char* ID) : OBOp(ID, false){};                  //  1**
      const char* Description(){ return "Generate 3D coordinates"; }//  2**

      virtual bool WorksWith(OBBase* pOb)const{ return dynamic_cast<OBMol*>(pOb)!=NULL; }//  3**
      virtual bool Do(OBBase* pOb, OpMap* pmap, const char* OptionText);
    };

    OpGen3D theOpGen3D("gen3D"); //  4**

    bool OpGen3D::Do(OBBase* pOb, OpMap* pmap, const char* OptionText) //  5**
    {
      OBMol* pmol = dynamic_cast<OBMol*>(pOb);
      if(!pmol)
        return false;

      OBBuilder builder;
      builder.Build(*pmol);
      pmol->SetDimension(3);

      return true;
    }

The real work is done in the Do function, but there is a bit of boiler plate code that is necessary.

1\*\* The constructor calls the base class constructor, which registers the class with the system. There could be additional parameters on the constructor if necessary, provided the base constructor is called in this way. (The false parameter is to do with setting a default instance which is not relevant here.)

2\*\* It is necessary to provide a description. The first line is used as a caption for the GUI checkbox. Subsequent lines are shown when listed with the verbose option.

3\*\* WorksWith() identifies the type of object. Usually this is a molecule (OBMol) and the line is used as shown. The function is used by the GUI to display the option only when it is relevant.

The OBOp base class doesn't know about OBMol or OBConversion and so it can be used with any kind of object derived from OBBase (essentially anything), and so that the dependencies between one bit of the program and another are reduced. This does lead to some compromises, as having to code WorksWith() explicitly rather than as a base class default.

4\*\* This is a global instance which defines the id of the class, which is the option name used on the command line, preceded by --.

5\*\* The Do() function carries out the operation on the target object. It should normally return true. Returning false causes the molecule to be not sent to the output format, so that it is possible to use an OBOp class as a filter, but this is more flexibly done using the [--filter option](/--filter_option "wikilink").

Any other general options specified on the command line (or the GUI) can be accessed by calling `find` on the parameter pmap. For example, to determine whether the -c option was also specified

      OpMap::const_iterator iter = pmap->find("c");
      if(iter!=pmap->end())
        do something;

Using nBabel
------------

Using the alternative nbabel interface can provide increased flexibility, because the options can have parameters. It is built by using nbabel.cpp in place of babel.cpp. Command lines look almost the same but output files need to be preceded by -O. So, for example, it is then possible to have command lines like:

      babel infile.smi -O outfile.sdf --minE sd --ff UFF

where --minE is an op with a parameter sd, which would appear in the OptionText parameter in its Do() function. There could even be multiple parameters, separated by spaces. The ff is not an op, but just a regular general option, and would be accessible the Do() of minE in the pmap parameter as above, with its parameter, “UFF”, obtained as <code>iter-&gt;second<code>.

As well as this extra flexibility, the nbabel interface also provides increased security by reducing confusion over which file is input and which output by making the specification of output file explicit and in a more standard way. It also simplifies some of the internal code