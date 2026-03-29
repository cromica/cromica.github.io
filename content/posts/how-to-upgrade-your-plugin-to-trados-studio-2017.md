+++
title = "How to upgrade your plugin to Trados Studio 2017"
date = 2017-04-15T04:14:17.000Z
lastmod = 2017-04-15T04:14:17.000Z
slug = "how-to-upgrade-your-plugin-to-trados-studio-2017"
featured = false
featured_image = "/images/2017/04/upgrade-1672367_1920.jpg"
ghost_id = "5a11ca067dd80546c26298e9"
migration_source = "ghost"
+++
As a developer I like to keep my project dependencies up to date. I am working on several applications and plugins for Trados Studio which I had to upgrade to Trados Studio 2017. I did this because I either want to take advantage of the newly released APIs or just because I have users that use Trados Studio 2017 and I want to be sure that the plugin is working correctly on this version. Depending on what version of Trados Studio my plugin is currently targeting, the upgrade process can be slightly different. Upgrading a plugin that targets Trados Studio 2015 is a simple process but for the previous versions there are a few additional steps that must be done.



### Upgrade from Trados Studio 2015

Trados Studio 2017 and 2015 use the same .NET Framework version so there's nothing that needs to be done regarding .NET. In fact there are just two simple steps that must be done to upgrade the plugin from 2015 to 2017:

* Change Trados Studio API reference to point to Trados Studio 2017 (Studio5 folder).
* Change the plugin framework build targets to be taken from [nuget](https://www.nuget.org/) 

Let's provide a little detail about each of the above steps.  

### ==Update Trados Studio references==

Every developer has worked with references so updating them is a trivial activity. However, not everyone is aware that references can be updated/changed by [manually editing the project file](http://stackoverflow.com/a/5129214) (csproj). I prefer this approach because all I have do is run a quick [replace](https://msdn.microsoft.com/en-us/library/139eef4h.aspx) from Studio4(replace this with your Studio folder version) to Studio5 and save the csproj file.

### ==Change the plugin framework build targets==

*Plugin framework build targets* might sound a bit strange and unfamiliar even if you've done several plugins and that's absolutely fine. This is a hidden process that runs during the plugin build process and does a bit of magic. I recommend reading [this article](/sdl-studio-plugin-dependencies-cleanup/) for more details.

So to update my plugin to use the 2017 version of the plugin framework build targets I need to remove the old version and then add the new version. To remove the old version I need to [manually edit the project file](http://stackoverflow.com/a/5129214) (csproj), search after **`<Import Project="$(MSBuildExtensionsPath)\SDL\SDLTradosStudio\`**, remove the entire line and then save the project file. Now that I have removed the old version I can add the new version by installing the **`Sdl.Core.PluginFramework.Build`** nuget package. If you're not sure how to install a nuget package have a look [here](https://docs.microsoft.com/en-us/nuget/tools/package-manager-ui).

### Upgrade from versions prior to Trados Studio 2015

In the case that my plugin is targeting Trados Studio 2014 or earlier the first thing I need to do is to upgrade the .NET Framework to version 4.5.2 (the same version that is used by Trados Studio 2015 and 2017). I recommend reading [this article](https://community.sdl.com/developers/language-developers/w/wiki/647.steps-to-upgrade-your-plugin-for-studio-2015), which covers in details the topic of moving your plugin to .NET Framework 4.5.2. Once the .NET Framework is updated the same steps apply as for Trados Studio 2015.

Please let me know if you have any questions or comments on upgrading your plugin to Trados Studio 2017.
