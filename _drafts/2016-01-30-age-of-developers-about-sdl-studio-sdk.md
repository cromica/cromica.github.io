---
layout: post
title: About SDL Studio SDK
date: 2016-01-30T12:54:21.000Z
category: 
  - SDL Studio
tags: Studio SDK
excerpt: "I love small and simple things that help me be more productive with my work. This is the main reasons why some time ago I started to work on GroupShareKit and I&amp;amp;#x27;m now happy to say that this is now available for everyone to use it as they like. Not only that you can use it but is completely open source."
image: "introducing-groupsharekit/introducing-groupsharekit.jpg"
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

SDK stands for **software development kit** and typically is a set of software development tools that enable the creation of applications for certain software applications. What exactly an SDK contains differ between each target software applications. Sometimes it can be a set of libraries in certain programing languages, like [Microsoft .Net](https://www.microsoft.com/net) or [Java](https://www.java.com), or it can contain a bunch of supporting tools. Typically the SDK cames as separate download since not every user might be interested in using this type of capabilities.If you are interested in more details you can have a look [here](https://en.wikipedia.org/wiki/Software_development_kit). 

### What can I find inside the SDL Studio SDK ###

SDL Studio SDK comes as a separate download from the standard SDL Studio application. You can get it from the developer page located [here](http://www.translationzone.com/openexchange/developer/sdk.html). Here's the list of things that will be installed with the SDK:

1. Sample applications, developed in C#, to demonstrate the basic capabilities of SDL Studio API's. This applications are really for good to get started with one of the API's but please bare in mind that they don't cover the entire API's so please also look for features in the [documention](http://www.translationzone.com/openexchange/developer/sdk.html) or ask on our [developer community](https://community.sdl.com/developers/language-developers/).
    
2. Microsoft Visual Studio project templates. This templates are very usefull when you start developing a new plugin for SDL Studio because you just select the template that is appropriate for the API you want to use

### What is not part of the SDL Studio SDK ###

At this point you might wonder a bit why the previous section didn't mention anything about the **API libraries** since typically this libraries come with the SDK. The reason I didn't mention them is because they are installed together with SDL Studio. There is a simple and good reason why they are distributed with the product and this is because some of the default features are developed using this API's. To give you some good examples all out-of-the-box filters are developed on top of the same [File Type Support Framework](http://producthelp.sdl.com/SDK/FileTypeSupport/4.0/), also each translation provider is built using the same [Translation Memory API](http://producthelp.sdl.com/SDK/TranslationMemoryApi/4.0/).

Distributing the API libraries together with the product has some pros and cons. The main disadvantage is that we are not able to provide new features in the API libraries on a different pace than the product releases. A big advantage is that the API's that are used for default features are well tested and mature.

At this point I need to mention that not all API libraries are used for default features. For example the [Intergration API](http://producthelp.sdl.com/SDK/StudioIntegrationApi/4.0/) is just a wrapper on top of internal components.

### Contribution ###

GroupShareKit is open source and published under [MIT License](https://opensource.org/licenses/MIT) so if you would like to add a new feature or you find a bug please don't hesitate to use the [issue tracker](). Of course you can do more than that by actually implementing the feature or the fix your looking for. Also you might find issues that are already opened with which you might be able to help. More about that [here](https://github.com/sdl/groupsharekit.net/issues). 

If you wonder why should you contribute to open source projects read this [article](http://opensource.about.com/od/what-is-open-source/fl/Why-Do-People-Contribute-to-Open-Source-Projects.htm).

### Happy coding ###

I'm really keen to hear about your experience with the library and what kind of integration you've done.

Please let me know if you have any comments or questions.

*Picture: [kballo - SDK Bayonne](https://flic.kr/p/Q4MPv)*
