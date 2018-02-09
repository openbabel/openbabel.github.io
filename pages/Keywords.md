---
title: Keywords
permalink: /Keywords/
---

This page contains information regarding using OpenBabel to translate application keywords between formats. Development in this area is very preliminary and only manages a few keywords currently. This page should give enough information for various format maintainers to implement keywords information to their own formats.

It is obvious that because each program is designed to do different things it is not always possible to translate all keywords. However some keywords do in fact translate between programs. This documentation should explain enough to understand the approach taken to be very diverse with all programs.

Generic Keywords
----------------

Right now our generic keywords are restricted to **model**, **method** and **basis**. These are keywords which are determined to be standard enough across formats to be useful when translating between formats giving the model of the operation, the basis set, and method (job / operation) to perform on molecule. The following table gives a list of valid values for each keyword.

|                           |                                                                                   |                                       |
|---------------------------|-----------------------------------------------------------------------------------|---------------------------------------|
| **model**                 | **basis**                                                                         | **method**                            |
| b3lyp, rhf, mp2, am1, pm3 | sto-2g, sto-3g, sto-4g, sto-5g, sto-6g, 3-21G, 6-21G, 4-31G, 5-31G, 6-31G, 6-311G | gradient, hessian, optimize, sadpoint |
||

Importing Keywords
------------------

It is useful in any conversion operation to get as much data about our input format as possible. Because of this it is suggested the formats import all of their specific keyword information whether it is related to the **Generic Keywords** or not. This section gives information on how to store this information in a more uniform way so that certain programs can access the information.

### Format Keywords

Formats should create a new OBSetData ([Generic Data](/Generic_Data "wikilink")) with an attribute for it's name in lowercase (GAMESSFormat = gamess). OBSetData is designed to allow adding of OBGenericData subclasses including additional OBSetData elements. To demonstrate this layout consider the GAMESS keywords which relate to the following OBSetData structure.

` $CONTRL SCFTYP=RHF DFTTYP=BLYP RUNTYP=OPTIMIZE $END`
` $SYSTEM MWORDS=7 TIMLIM=10 $END`
` $TDDFT NSTATE=3 MULT=1 $END`
` $GUESS GUESS=HUCKEL $END`
` $BASIS GBASIS=N31 NGAUSS=6 DIFFSP=.T. NDFUNC=1 $END`

OBMol

-   gamess (OBSetData)
    -   CONTRL (OBSetData)
        -   SCFTYP=RHF (OBPairData)
        -   DFTTYP=BLYP (OBPairData)
        -   RUNTYP=OPTIMIZE (OBPairData)
    -   SYSTEM (OBSetData)
        -   MWORDS=7 (OBPairData)
        -   TIMLIM=10 (OBPairData)
    -   TDDFT (OBSetData)
        -   NSTATE=3 (OBPairData)
        -   MULT=1 (OBPairData)
    -   GUESS (OBSetData)
        -   GUESS=HUCKEL (OBPairData)
    -   BASIS (OBSetData)
        -   GBASIS=N31 (OBPairData)
        -   NGAUSS=6 (OBPairData)
        -   NDFUNC=1 (OBPairData)
        -   DIFFSP=.T. (OBPairData)

Exporting Keywords
------------------

This section contains suggestions on how to give the best possible exports from OpenBabel. The following template should be considered in the **WriteMolecule** function.

`const char *keywords = pConv->IsOption(`“`k`”`,OBConversion::OUTOPTIONS);`
`const char *keywordsEnable = pConv->IsOption(`“`k`”`,OBConversion::GENOPTIONS);`
`const char *keywordFile = pConv->IsOption(`“`f`”`,OBConversion::OUTOPTIONS);`
`string defaultKeywords = " $CONTRL COORD=CART UNITS=ANGS $END";`
`if(keywords)`
`{`
`  defaultKeywords = keywords;`
`}`
`if (keywordsEnable)`
`{`
`  OBSetData *gmsset = (OBSetData *)pmol->GetData(`“`gamess`”`);`
`  if(gmsset)`
`  {`
`    /* export keywords from GAMESS keywords specifically */`
`  }`
`  else`
`  {`
`     string model;`
`     string basis;`
`     string method;`
`     OBPairData *pd = (OBPairData *) pmol->GetData(`“`model`”`);`
`     if(pd)`
`       model = pd->GetValue();`
`     pd = (OBPairData *) pmol->GetData(`“`basis`”`);`
`     if(pd)`
`       basis = pd->GetValue();`
`     /* pull the global method keyword */`
`     pd = (OBPairData *) pmol->GetData(`“`method`”`);`
`     if(pd)`
`       method = pd->GetValue();`
`     if(model != "" && basis != "" && method != "")`
`     {`
`       /* demonstrates convert method to an export friendly keyword */`
`       if(method == `“`optimize`”`)`
`       {`
`         method = `“`opt`”`;`
`       }`
`       ofs << model << `“`/`”` << basis << `“`,`”` << method << endl;`
`     }`
`     else`
`     {`
`       ofs << `“`#Unable`` ``to`` ``translate`` ``keywords!`”` << endl;`
`       ofs << defaultKeywords << endl;`
`     }`
`   }`
`  }`
`}`
`else if (keywordFile)`
`{`
`  ifstream kfstream(keywordFile);`
`  string keyBuffer;`
`  if (kfstream)`
`  {`
`    while (getline(kfstream, keyBuffer))`
`      ofs << keyBuffer << endl;`
`  }`
`}`
`else`
`{`
`  ofs << defaultKeywords << endl;`
`}`

This code demonstrates one interesting feature. Notice that we can check to see if we have imported GAMESS specific information and may do a special export specifically for that format. This is used in the Ghemical(gpr) export functionality as Ghemical supports saving the GAMESS specific data and thus if we want to translate from GAMESS Output to Ghemical we want to make sure we get all the GAMESS keywords and not just the Generic Keywords. In the case of GAMESS to Gaussian we simply export the Generic Keywords. (This code snippet can be found in the *src/formats/gaussformat.cpp* file.)

TODO
----

Currently the only format that imports it's keywords is GAMESS. The GAMESS format also attempts to translate it's keywords to generic keywords but all of this is done with numerous if-then-else statements to pick out the specific keywords we are testing keyword translation. We need to develop some uniform method / class which helps to take format specific keywords and translate them to generic keywords. It is unknown how this information relates to XML formats.

[Category:Developer](/Category:Developer "wikilink")