---
layout: post
title:  "Configure OpenExchange development environment"
date:   2015-08-25 10:00:00
category: "SDL Studio"
tags: "Studio OpenExchange plugin"
excerpt: "This is the third part of the OpenExchange: Age of Developers series and is meant to provide guideline on how to setup the development environment for OpenExchange."
image: "age-of-developers-build-ox-environment/age-of-developers-build-ox-environment.jpg"
---

<img src="/assets/images/posts/age-of-developers-build-ox-environment/age-of-developers-build-ox-environment.jpg" alt="Age Of Developers" title="Age of Developers" class="img-responsive">

<p class="dropcap">This is the third part of the <a href="http://romuluscrisan.com/sdl%20studio/2015/07/20/OpenExchange-age-of-developers.html" target="_blank">OpenExchange: Age of Developers</a> series and is meant to provide guideline on how to setup the development environment for OpenExchange.</p>

### Age of developers - table of contents###

As I release parts of this series I will update this page with links to the articles.

1. [Introduction](http://romuluscrisan.com/sdl%20studio/2015/07/20/OpenExchange-age-of-developers.html)
2. [I'm a translator do I need to write code?](http://romuluscrisan.com/sdl%20studio/2015/07/20/OpenExchange-age-of-developers-translator-code.html)
3. [I'm a developer, why bother with translation industry?](http://romuluscrisan.com/sdl%20studio/2015/08/05/OpenExchange-age-of-developers-developer-translation-industry.html)
4. Configure OpenExchange development environment
5. [OpenExchange:Where do I start?](http://romuluscrisan.com/sdl%20studio/2015/10/09/OpenExchange-age-of-developers-where-do-i-start.html)

### First things first  ###

In my previous article I tried to articulate why developing applications or plugins for OpenExchange can bring you benefits regardless if you are a developer or not. Now it's time to move on and start get our hands dirty. Before starting any development you need to prepare your machine/laptop and based on which Studio(2014 or 2015) version are you going to use the configuration might be a bit different but let's take it step by step:

1. **Operating system** - Since the development is done using Microsoft .NET at least for the moment this is only possible only on Windows operating systems. The minimum version you should use is Windows Vista SP2 but I highly recommend to try and use Windows 7 or later. If you want to develop on Windows server that's fine but you need to have at least Windows Server 2008 SP2.
2. **SDL Product** - At the moment you can build applications around a few SDL products like Multiterm, Passolo or Studio. Based on which plugin you want to build you will need a licensed product. Now if you don't have a license don't worry because if you register [here](http://www.translationzone.com/openexchange/developer/) and join the SDL Developer Program we can help you with the licenses you need for development.
3. **SDK** - You can download the SDK for the product you're looking to develop from [here](http://www.translationzone.com/openexchange/developer/sdk.html). Now before going forward I would like to clarify what exactly you get and what you don't get with this SDK's. The main purpose for the SDK's is to help the developer in building the application and this why with the SDK you get some code samples, documentation, Microsoft Visual Studio project templates (2012, 2013 and soon 2015) and build targets that are used by Microsoft Visual Studio to create your *sdlplugin* file at each build. You won't get the product API with the SDK since this is already part of the application.
4. **Microsoft .Net** - This depends on the SDL Studio version you are developing for. SDL Studio 2014 uses .Net framework 4.0.3 and SDL Studio 2015 uses .Net framewrok 4.5.2. Based on the operating system you might already have .net installed on your machine.
5. **Microsoft Visual Studio** - For SDL Studio 2014 development you can use any version of Visual Studio starting from Visual Studio 2010 and for SDL Studio 2015 you need to use Visual Studio 2013 or later. I highly recommend to use Visual Studio 2013 or 2015. For this 2 versions you can use the community edition which is completely free and offers the same features like the professional version. More details about it [here](https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx).

There aren't a lot of things to be installed and configured but it might take some time to install all of them.  

### Version control ###

A version control system allows you to track the changes you've done to a file or a set of files. It is also backing up your files on some server/cloud. A few people might say that this is not necessary for small projects because it's an overhead. This might be true but there are plenty of other reasons to do it:

1. Files are backed up on a server/cloud and in case your machine crashes you don't loose all your work.
2. Every change you make to a file is tracked and version-ed. This means you can always rollback to a previous version if you've done something bad in your current version.
3. What do you do if you have multiple development machines, like a desktop and a laptop? Synchronizing between them can give you lot's of headaches.
4. There are free solutions like [github](https://github.com/) or [visual studio online](https://www.visualstudio.com/en-us/products/visual-studio-online-pricing-vs.aspx). Now github is free for as many users as you like as long as your project is public (you should consider open source licensing in this case). Visual Studio online is free but only for the 5 users. I'm pretty sure that one of this options will fit your needs.


### Conclusion###

Please leave a comment if you have any questions.
