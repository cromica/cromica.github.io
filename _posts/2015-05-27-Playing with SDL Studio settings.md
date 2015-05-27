---
layout: post
title:  "Playing with SDL Studio settings"
date:   2015-05-27 19:00:00
category: "SDL Studio"
tags: "Studio OpenExchange plugin"
excerpt: "SDL Studio is a complex and extendable application witch comes with a few APIs that allows any developer to extend the application in all kind of ways. To be more exact there are 6 APIs you can use to build your application. This degree of complexity and extensibility translates in a huge amount of settings you can play with. The user interface does a great job present them in a meaningful way but that is not the same when you want to develop something in your custom applications and you need to read or update some of the settings."
image: "playing-with-settings/playing-with-settings.png"
---

<img src="/assets/images/posts/playing-with-settings/playing-with-settings.png" alt="Playing with SDL Studio settings" title="Playing with SDL Studio settings" class="img-responsive">

<p class="dropcap">SDL Studio is a complex and extendable application witch comes with a few APIs that allows any developer to extend the application in all kind of ways. To be more exact there are 6 APIs you can use to build your application. This degree of complexity and extensibility translates in a huge amount of settings you can play with. The user interface does a great job presenting them in a meaningful way but that is not the same when you want to develop something in your custom applications and you need to read or update some of the settings.</p>

### Project Settings ###

Lets say you are in a situation where the API is not offering you direct access to the user setting you would like to change, what options you have in this situation? A great amount of settings are store in the project file which in essence it's an xml file. This mean I could use the standard .NET libraries to parse the project xml file and change what I need. This is completely true and can be done but the problem is knowing the xml structure which for the project file can be pretty complex and hard to understand. To give you an example the project file for a very simple test project is over 1000 lines. Understanding those lines can take some time and patience. Before continuing I want to clarify one thing which is knowing that the SDL Studio project file is not only about user settings it's much more than that, things that are used internal by Studio so we need to be very careful when we change anything in this file. My recommendation would be to use the [settings classes](http://producthelp.sdl.com/SDK/Core/3.0/search.html?SearchText=settingsbundle) exposed by SDL Studio Core API.

### Settings Bundle and Group ###

User settings are stored in hierarchical structure as settings bundles. A bundle is bound to a feature from SDL Studio. For example I can have a settings bundle for project specific settings, another project bundle with settings for language direction, another one for language file and so on. Each bundle will have unique identifier as a GUID value and can have one or multiple child elements in form of settings group. A settings group represent a smaller piece from the bundle feature and can have, as child's, one or multiple settings. As an example of settings group you can think at specific settings for a file type which is part of the project settings bundle.

With this said the SDL Studio API has [ISettingsBundle](http://producthelp.sdl.com/SDK/Core/3.0/html/9e4ba18c-dab1-bb47-0ce7-a31fb3002ba3.htm) interface and a [SettingsGroup](http://producthelp.sdl.com/SDK/Core/3.0/html/72c76110-8d6c-6315-58d9-dc36b998d14b.htm) class used to represent the hierarchical structure I explained above. The API doesn't expose a concrete implementation of [ISettingsBundle](http://producthelp.sdl.com/SDK/Core/3.0/html/9e4ba18c-dab1-bb47-0ce7-a31fb3002ba3.htm) so you need to use [SettingsUtils](http://producthelp.sdl.com/SDK/Core/3.0/html/ae69c32c-3ebe-946f-3e3c-d091278a407f.htm) class to create an instance of settings bundle.

### Real use case ###

To clarify the things a bit I want to show you a real use case where you can use the settings classes from the SDL Studio Core API. Let's say that for a project we want to disable all the global verifiers. This value is kept in the project file and can be changed using .NET xml libraries or using the settings classes I explained in the previous paragraph. Here's the code required to implement this feature:

<script src="https://gist.github.com/cromica/7299796351f364d93aa5.js"></script>

In this case I obtain the settings group id by instantiating all the global verifiers but you can request the setting group also by just providing the string. 


Please leave a comment if you have any questions.