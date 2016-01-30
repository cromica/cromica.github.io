---
layout: post
title: About SDL Studio SDK
date: {}
category: 
  - SDL Studio
tags: Studio SDK
excerpt: "I love small and simple things that help me be more productive with my work. This is the main reasons why some time ago I started to work on GroupShareKit and I&amp;#x27;m now happy to say that this is now available for everyone to use it as they like. Not only that you can use it but is completely open source."
image: "introducing-groupsharekit/introducing-groupsharekit.jpg"
published: true
---


<img src="/assets/images/posts/introducing-groupsharekit/introducing-groupsharekit.jpg" alt="Setting up build automation" title="Setting up build automation" class="img-responsive">

<p class="dropcap">This is the 5th part of the <a href="http://romuluscrisan.com/sdl%20studio/2015/07/20/OpenExchange-age-of-developers.html" target="_blank">OpenExchange: Age of Developers</a> series. In the previous articles I talked about how to configure your development environment and also gaeve  some suggestion on how you can start the development. Now in this  </p>

### What is GroupShareKit? ###

GroupShareKit is a client library targeting .NET 4.5 and above that provides an easy way to interact with [GroupShare Rest API](http://sdldevelopmentpartners.sdlproducts.com/documentation/api). This library will greatly simplify and reduce the work a developer has to do in order to consume resources available in GroupShare by reducing the amount of boilerplate code and configuration that has to be written. This way the developer can focus his time and work on the actual implementation that has to be done.

Another benefit of this library is that you don't have to actually understand how rest API's are working since all this will be completely hidden. If you are not sure what an rest API is please have a look [here](http://schoolofdata.org/2013/11/18/web-apis-for-non-programmers/).

### How do I start? ###

Using GroupShareKit library is very simple and it doesn't require to run any installer, all you have to do is a few clicks inside Microsoft Visual Studio. The first step you need to do is to open the project where you want to use GroupShareKit in Visual Studio. After the project is opened go in the `Solution Explorer` area (if you can't find it just press CTRL+ALT+L inside Visual Studio), then right click on the project `References` and select `Manage Nuget packages...`(if you can't see this option have a look [here](https://docs.nuget.org/consume/installing-nuget)). This action will open a window where you need to search for `GroupShareKit` and once you get the result just click the install button. That's all, you can start use the GroupShareKit library in your project.

<img src="/assets/images/posts/introducing-groupsharekit/manage-nuget.png" alt="Manage Nuget" title="Manage Nuget" class="img-responsive">


### Documentation ###

For more details please have a look [here](https://github.com/sdl/groupsharekit.net#groupsharekit---groupshare-rest-api-client-library-for-net-). If you don't find an answer don't hesitate to ask a question on [language developer community](https://community.sdl.com/developers/language-developers/).

### Contribution ###

GroupShareKit is open source and published under [MIT License](https://opensource.org/licenses/MIT) so if you would like to add a new feature or you find a bug please don't hesitate to use the [issue tracker](). Of course you can do more than that by actually implementing the feature or the fix your looking for. Also you might find issues that are already opened with which you might be able to help. More about that [here](https://github.com/sdl/groupsharekit.net/issues). 

If you wonder why should you contribute to open source projects read this [article](http://opensource.about.com/od/what-is-open-source/fl/Why-Do-People-Contribute-to-Open-Source-Projects.htm).

### Happy coding ###

I'm really keen to hear about your experience with the library and what kind of integration you've done.

Please let me know if you have any comments or questions.

*Picture: [BOB008 - Swiss Army Knife](https://flic.kr/p/5o9EuF)*
