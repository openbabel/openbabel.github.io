---
title: Plugins
permalink: /Plugins/
---

[Image:Design3plugin.png](/Image:Design3plugin.png "wikilink")

All plugins inherit from OBPlugin, this class has public GetType(), GetName() and GetDescription() methods and a protected SetInfo() method which can be called by friend class OBPluginFactory. OBPlugin doesn't have any other uses at the moment and no OBPlugin methods have to be re-implemented or called when creating plugins.

Real plugins inherit from an OBPluginInterface, which itself inherits from OBPlugin. These interfaces are the types of plugins, they have pure virtual functions to be implemented in the derived plugin class. OBMoleculeFormat, OBDescriptor, OBFingerprint, ... are all plugins interfaces. In the future, perception models will also be plugins with matching interfaces. (Note: there is no OBPluginInterface class, this is just to make the diagram more generic.)

A plugin will need to use the MAKE_FACTORY(Class, ClassFactory) macro to create a derived OBPluginFactory. The plugin will also need to declare a static instance of the derived OBPluginFactory with the type, name and description as parameters:

`#include `<openbabel/descriptor.h>
`class MyDescriptor : public OBDescriptor`
`{`
`  public:`
`    double Predict (...) `
`    {`
`      ...`
`      return ...;`
`    }`
`};`
`MAKE_FACTORY(MyDescriptor, MyDescriptorFactory)`
`MyDescriptorFactory myDescriptionFactory(OBPlugin::DescriptorType, `“`MyDescriptor`”`, `“`description...`”`)`

Improvements compared to 2.2:

-   OBPluginManager is now a facade/interface and the implementation details are hidden.
-   OBPluginManager provides all needed plugin iterators, the client never sees how the plugins are stored internally, ...
-   The plugin type, name and des&lt;cription is in one single place (at the bottom of the plugin file)
-   static instance of the plugin replaced by much smaller factory

TODO:

-   have both a MAKE_FACTORY and MAKE_SINGLETON_FACTORY to create multiple or a single instance (&lt;-- using a shared_ptr?)
-   create interface(s) for perception models

[Category:Projects](/Category:Projects "wikilink")