+++
title = "SDL Studio plugin dependencies cleanup"
date = 2016-09-30T13:27:40.000Z
lastmod = 2016-09-30T13:27:40.000Z
slug = "sdl-studio-plugin-dependencies-cleanup"
featured = false
featured_image = "/images/2016/09/pensacola-beach-83233_1920.jpg"
ghost_id = "5a11ca067dd80546c26298e1"
migration_source = "ghost"
+++
I decided to write this article after I got a question on my last blog article, [SDL Studio plugin manifest](/sdl-studio-plugin-manifest/), about an issue with files that are overridden during an SDL Studio plugin build. Although this issue is quite specific I received questions with similar situations from other people and the root cause of this problem is related to how you manage SDL Studio plugin dependencies, or, in other words, how you manage the assemblies that are copied in the output folder of the plugin.

### SDL Studio Plugin Generation Process

To better understand the problem I need to explain what is happening when an SDL Studio plugin is generated from Microsoft Visual Studio. By default Visual Studio generates dll files for the projects you have in your solution when you select a build action. To be more accurate all that Visual Studio does is to run [MSBuild](https://en.wikipedia.org/wiki/MSBuild) which is the Microsoft Build Engine that is responsible for producing the assemblies, out of your source code and projects. Some of you might know already but for those of you who don't know an `.sdlplugin` file is not a dll, rather it's a specialized archive that could potentially contain one or more assemblies (dlls) and some other resources. So it's pretty clear that the `.sdlplugin` file is not produced by Visual Studio with a default setup. 

A few months ago I've written an article [about the SDL Studio SDK](/about-sdl-studio-sdk/) in which I explained about the SDL Studio project templates for Visual Studio. These project templates extend the standard project build process from Visual Studio by adding another step which generates the `.sdplugin` file. So the workflow to generate the plugin package is something like ==generate the dlls== and then based on what you've specified in the plugin manifest ==generate the `.sdplugin` package==.

If you really want to know where the magic happens, you should open your plugin `.csproj` file (which is just a specialized xml file) with your favourite text editor and scroll down the bottom where you should find a line similar to the one in the screenshot:

![](/images/2016/09/sdl-pluginframework-build-targets.png)


### The problem(s)

If you run the build for your plugin and then you look in the output location, you might be surprised to find that you have a lot of files (I have had around 200 files for one plugin). This might come as a surprise since your plugin might only depend on a few assemblies. So from where are all these files/dlls coming from? Can these files cause any harm (this is the issue in my previous article)? Can I avoid having these files copied at all?

These files come from the SDL Studio install location and are copied over because your plugin depends on some Studio APIs that internally depends on these files. So, in other words, they are dependencies of your plugin dependencies. The problem with these files is that they are useless since the plugin will be loaded by SDL Studio and all this dependency will be resolved at runtime from the SDL Studio install location. On top of that you might want to use a newer version of a particular library that is also used by SDL Studio but all of a sudden you realize that during the build this is overridden with the version that was deployed with SDL Studio. All of this is happening because of Microsoft Visual Studio default behaviour.

### The solution

The solution is quite simple and requires just a few clicks:

* Open your plugin solution in Microsoft Visual Studio and expand your plugin project.

* Under the project you should find a References section you can also expand. 

* Select all SDL Studio API assemblies that are used in your plugin and then right-click and select ==Properties==.

![](/images/2016/09/api-prop.png)

* You should now see the Properties pane inside which should have an option called ==Copy Local== set to True.

![](/images/2016/09/copy-local.png)

* Change it to false and run ==Clean Solution== from Visual Studio.

![](/images/2016/09/clean-solution.png)

After those steps the dependencies will no longer be copied over which will result in a cleaner output location, faster build and avoid duplicate library version issues.

If you have any questions don't hesitate to leave a comment.
