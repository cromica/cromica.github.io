---
layout: post
title: About SDL Studio SDK
date: 2016-01-31 10:37:00
category: 
  - SDL Studio
tags: Studio SDK
excerpt: "This is the 5th part of the OpenExchange: Age of Developers series. In the previous articles I talked about how to configure your development environment and also gave  some suggestion on how you can start the development for OpenExchange store. One of the steps from the development environment setup was to install the SDL Studio SDK and I think it's worth talking about it in a bit more detail."
image: "about-sdl-studio-sdk.jpg"
published: true
---

![about-sdl-studio-sdk.jpg]({{site.baseurl}}/assets/images/posts/about-sdl-studio-sdk.jpg)


<p class="dropcap">This is the 5th part of the <a href="http://romuluscrisan.com/sdl%20studio/2015/07/20/OpenExchange-age-of-developers.html" target="_blank">OpenExchange: Age of Developers</a> series. In the previous articles I talked about how to configure your development environment and also gave  some suggestion on how you can start the development for OpenExchange store. One of the steps from the development environment setup was to install the SDL Studio SDK and I think it's worth talking about it in a bit more detail.</p>

### Age of developers - table of contents###

As I release parts of this series I will update this page with links to the articles.

1. [Introduction](http://romuluscrisan.com/sdl%20studio/2015/07/20/OpenExchange-age-of-developers.html)
2. [I'm a translator do I need to write code?](http://romuluscrisan.com/sdl%20studio/2015/07/20/OpenExchange-age-of-developers-translator-code.html)
3. [I'm a developer, why bother with translation industry?](http://romuluscrisan.com/sdl%20studio/2015/08/05/OpenExchange-age-of-developers-developer-translation-industry.html)
4. [Configure OpenExchange development environment](http://romuluscrisan.com/sdl%20studio/2015/08/25/OpenExchange-age-of-developers-build-environment.html)
5. [OpenExchange:Where do I start?](http://romuluscrisan.com/sdl%20studio/2015/10/09/OpenExchange-age-of-developers-where-do-i-start.html)
6. About SDL Studio SDK

### What is an SDK? ###

SDK stands for **software development kit** and typically is a set of software development tools that enable the creation of applications for certain software applications. What exactly an SDK contains differ between each target software applications. Sometimes it can be a set of libraries in certain programming languages, like [Microsoft .Net](https://www.microsoft.com/net) or [Java](https://www.java.com), or it can also contain a bunch of supporting tools. Typically the SDK comes as a separate download since not every user might be interested in using this type of capabilities.If you are interested to read more details you can have a look [here](https://en.wikipedia.org/wiki/Software_development_kit). 

### What I can find inside the SDL Studio SDK? ###

SDL Studio SDK comes as a separate download from the standard SDL Studio application. You can get it from the developer page located [here](http://www.translationzone.com/openexchange/developer/sdk.html). Now let's see what goodies we get with the SDK:

1. Sample applications, developed in C#, to demonstrate the basic capabilities of SDL Studio API's. This applications are really good to get you started with one of the API's but please bare in mind that they don't cover the entire API's feature set so please also look for features in the [documention](http://www.translationzone.com/openexchange/developer/sdk.html) or ask on our [developer community](https://community.sdl.com/developers/language-developers/). After the SDL Studio SDK is installed you can find the samples located under the `c:\ProgramData\SDL\SDK {Version}\` folder.
    
2. Microsoft Visual Studio project templates. This templates are very useful when you start developing a new plugin for SDL Studio because you just select the template that is appropriate for the API you want to use.
![sdl-project-vs-templates.png]({{site.baseurl}}/assets/images/posts/sdl-project-vs-templates.png)


### What is not part of the SDL Studio SDK? ###

At this point you might wonder a bit why the previous section didn't mention anything about the **API libraries** since typically this libraries come with the SDK. The reason I didn't mention them is because they are installed together with SDL Studio. There is a simple and good reason why they are distributed with the product and this is because some of the default SDL Studio features are developed using this API's. To give you some good examples all out-of-the-box filters are developed on top of the same [File Type Support Framework](http://producthelp.sdl.com/SDK/FileTypeSupport/4.0/), also each translation provider is built using the same [Translation Memory API](http://producthelp.sdl.com/SDK/TranslationMemoryApi/4.0/).

Distributing the API libraries together with the product has some pros and cons. The main disadvantage is that we are not able to provide new features in the API libraries on a different pace than the product releases. A big advantage is that the API's that are used for default features are well tested and mature.

At this point I need to mention that not all API libraries are used for default features. For example the [Intergration API](http://producthelp.sdl.com/SDK/StudioIntegrationApi/4.0/) is just a wrapper on top of internal components.

### Do I need to install the SDK? ###

If the **API libraries** are distributed with the product a valid questions pops up and that is if I need to install the SDK. The answer is no but I highly recommend it. It is possible to develop a plugin for SDL Studio without having the SDK installed on your machine is just that it will take more time to setup your Visual Studio project. First of all you will have to specify all the SDL Studio API libraries you need. This is pretty straightforward task but the complicated bit is to create the `.sdlplugin` file. You will have to manually edit the Visual Studio project file and add the msbuild targets to create the `.sdlplugin` package. 

### Future plans ###

I have to say that SDL Studio SDK is kind of slim in terms of the tooling that is providing to the developers and it doesn't make too much sense to keep it in the current form. There other better ways in which we can provide the current content so the future plans are as follows:

1. Move sample applications to Github. This gives us a few benefits like better search-ability, improvements and fixes can be done by anyone interested not just SDL internal developers and of course it will still be available to download locally as a zip file.

2. Create more specific Visual Studio project templates.

3. Provide Visual Studio project templates as Visual Studio extension. Initially this will probably be available only for Visual Studio 2015 and based on the need we will make it available for older versions.

I believe this changes will make the SDK more open and closer to the developer. Of course when all the above points will be done the current installer will probably disappear.

Please let me know if you have any comments or questions.

*Picture: [kballo - SDK Bayonne](https://flic.kr/p/Q4MPv)*
