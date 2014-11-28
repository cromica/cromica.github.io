---
layout: post
title:  "SDL Studio standalone plugin assembly resolver"
date:   2014-11-28 12:20:00
category: "SDL Studio"
tags: "Studio plugins OpenExchange assembly standalone"
summary: "Last week I was working at a new plugin for SDL Studio 2014 and I wanted to serialize some information in json. The best tool handle this type of operations in .NET, at least in my opinion, is Json.NET. It made perfect sense to use it but until now I didn't use any external dependencies in an SDL Studio plugin so I started to look into what options we have to deploy our plugins together with 3rd party assemblies."
image: "/3rdparty/3rdpartyassemblies.png"
---

<img src="/assets/images/posts/assemblyresolver/assemblyresolver.jpg" alt="Hello SDL" title="Hello SDL" class="img-responsive">

<p class="dropcap">SDL Studio plugin system allows developers to develop new features on top of the standard functionality. There are 2 types of plugins that can be developed, one which behaves like a Studio add-in and another one which behaves as a standalone application. Both plugin types require to run inside Studio installation folder. This is because the public Studio SDK is using other assemblies that are located in Studio folder. While this is perfectly fine for add-in type plugins for standalone plugins this adds limitation on where and how you can deploy your application.</p>



### Why not GAC ? ###

Many developers have asked us to register Studio assemblies in [GAC](http://msdn.microsoft.com/en-us/library/yf1d93sz%28v=vs.110%29.aspx) in order to solve the issue on where and how you can deploy your standalone Studio plugins. Having Studio assemblies registered in [GAC](http://msdn.microsoft.com/en-us/library/yf1d93sz%28v=vs.110%29.aspx) means that those assembly can be shared across the entire system. Although registering assemblies in GAC might had seem to be a good solution there are many implications when doing it. The main reason why Studio is not using [GAC](http://msdn.microsoft.com/en-us/library/yf1d93sz%28v=vs.110%29.aspx) is because of the following scenario:

> **GAC supports multiple version of an assembly. This means that when an assembly is updated to a newer version both versions will be saved. You might say that the old version should be removed, but this is not always possible since for example there are customers that have multiple version of Studio that are used on the same machine. Keeping multiple version of the same assembly will lead to unexpected behavior and errors from the application.**

You can read more about why to avoid GAC [here](http://www.sellsbrothers.com/Posts/Details/12503).   

### Got it ... no GAC, but we want solutions! ###

To solve this problem I've developed a small library called **Studio AssemblyResolver**. Basically every time an dll is not found in the current application location the library will look after the dll in the Studio folder. The library comes with 2 mechanism for looking after Studio folder but you can add your own resolve mechanism. If you are interested about more details please have a look [here](https://github.com/cromica/Studio-AssemblyResolver). The library is also published in the [Nuget package repository](https://www.nuget.org/packages/Studio.AssemblyResolver/0.1.1) which allows to be easily added to your project.

### How to use Studio AssemblyResolver ###

There are 2 simple steps to get your Studio assemblies resolved:

- Add a reference to the **Studio.AssemblyResolver** library from Visual Studio using NuGet

<img src="/assets/images/posts/assemblyresolver/managenuget.png" alt="Manage Nuget" title="Manage Nuget" class="img-responsive">

<img src="/assets/images/posts/assemblyresolver/nugetassemblyresolver.png" alt="Nuget assembly resolver" title="Nuget assembly resolver" class="img-responsive">

- Add the following line of code in you application entry point

{% highlight csharp %}
AssemblyResolver.Resolve();
{% endhighlight%}

I've already included the **Studio AssemblyResolver** library in [Reindex Translation Memories](https://github.com/sdl/SDL-Community/tree/master/Reindex%20Translation%20Memories) plugin. You can have a look [here](https://github.com/sdl/SDL-Community/blob/master/Reindex%20Translation%20Memories/Sdl.Community.ReindexTms/Program.cs#L18) if you are interested to see how I've included the library.


Please leave a comment if you have any questions or feedback.