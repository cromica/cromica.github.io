+++
title = "Studio plugin versioning"
date = 2015-05-05T16:20:00.000Z
lastmod = 2016-09-07T18:48:38.000Z
slug = "studio-plugin-versioning"
tags = ["SDL AppStore", "SDL Studio", "SDL Studio Plugins"]
aliases = ["/sdl%20studio/2015/05/05/Studio%20plugin%20versioning.html/"]
featured = false
featured_image = "/images/2016/09/version.jpg"
ghost_id = "5a11ca067dd80546c26298ce"
migration_source = "ghost"
+++
SDL Studio 2015 is just around the corner and as a plugin developer there are a few things you should do to make your plugin compatible with this new Studio version. You can read more about this here: <a href="https://community.sdl.com/developers/language-developers/w/wiki/647.steps-to-upgrade-your-plugin-for-studio-2015">Steps to upgrade your plugin for Studio 2015</a>. Now with all Studio versions out there some may ask how can I control my plugin versions and how can I make sure my plugin will be used only by the appropriate version of SDL Studio.

### Plugin manifest
Every plugin must contain a manifest file that defines a few general information about your plugin. The file is called *pluginpackage.manifest.xml* and if you open any *.sdlplugin file with and archiving tool, like [7zip](http://www.7-zip.org/), you should be able to see it and open it. Also when you create a new plugin solution in Microsoft Visual Studio this file will be automatically created for you and it will be included in our plugin package (.sdlplugin file). In this file you can add your plugin name, description, author, version, required product and you can [specify additional files to be included in the package](/3rd-party-assemblies-and-sdl-studio-plugins/).

### Plugin versioning
As I highlighted before you can specify a plugin version by using the tag:
> Version

This is used by SDL Studio to remove previously deployed plugins. For example if you have on your machine a plugin with version 0.1.0.0 if you install a new version like 0.1.1.0 it will automatically remove the unpacked version of the plugin and unpack the newer version. If the version is the same or lower this will not happen hence you will have to do it yourself.

### Product versioning
Besides plugin versioning you can also specify SDL Studio versions that are compatible with your plugin. This can be done using the tag:
>RequiredProduct

On this tag you can specify in the attribute *minversion* the lowest SDL Studio version that is compatible with your plugin. For example if you specify a minimum version of *10.0* this means that your plugin will be compatible with Studio 2011 or higher. If you want to limit your plugin just to a specific SDL Studio version you can also specify a *maxversion* attribute. So for example if in our case we add a maximum version of *10.9* this will not be compatible with Studio 2014 or higher and even if it's copied into the Studio 2014 plugins folder it will be ignored.

### Universal plugin installer
The universal plugin installer is also using this information to avoid deploying plugins that are not compatible with a specific Studio version. If you are not familiar with the universal plugin installer you can read more here: [SDL plugin installer](https://github.com/sdl/Sdl-plugin-installer).

### Final words
I recommend to review your manifest file and take advantage of the versioning capabilities. Even if there is no obvious reason at the moment it might prove handy in the future. 

Please leave a comment if you have any questions.
