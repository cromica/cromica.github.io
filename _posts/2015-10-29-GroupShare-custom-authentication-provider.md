---
layout: post
title:  "GroupShare custom authentication provider"
date:   2015-10-29 19:00:00
category: "SDL-GroupShare"
tags: "GroupShare OpenExchange plugin"
excerpt: "GroupShare is a collaboration platform for translation teams that is helping streamline translation processes, reduce coordination efforts and offer a secure access to all in-house and external resources. I'm not going to get into details about GroupShare but if you want to know more have a look here. Since GroupShare is a collaboration platform it implies that there are ways to create and manage users. Out of the box GroupShare allows 2 types of users to be defined. One is the SDL type for which the username and password is created and stored in the GroupShare database. The second one is Windows type which means that the password is not stored in GroupShare database rather the user will be authenticated against a corporate network that is using Microsoft Active Directory service domain identity or other Windows accounts. While this is good enough in most of the situations there are customers that already have a system where they store users and would like to use that instead of having different users in various systems. To overcome this need GroupShare allows implementation of custom authentication providers."
image: "groupshare-custom-authentication-provider/groupshare-custom-authentication-provider.png"
---

<img src="/assets/images/posts/groupshare-custom-authentication-provider/groupshare-custom-authentication-provider.png" alt="GroupShare custom authentication provider" title="GroupShare custom authentication provider" class="img-responsive">

<p class="dropcap">GroupShare is a collaboration platform for translation teams that is helping streamline translation processes, reduce coordination efforts and offer a secure access to all in-house and external resources. I'm not going to get into details about GroupShare but if you want to know more have a look <a href="http://www.translationzone.com/products/sdl-studio-groupshare/" target="_blank">here</a>. Since GroupShare is a collaboration platform it implies that there are ways to create and manage users. Out of the box GroupShare allows 2 types of users to be defined. One is the SDL type for which the username and password is created and stored in the GroupShare database. The second one is Windows type which means that the password is not stored in GroupShare database rather the user will be authenticated against a corporate network that is using Microsoft Active Directory service domain identity or other Windows accounts. While this is good enough in most of the situations there are customers that already have a system where they store users and would like to use that instead of having different users in various systems. To overcome this need GroupShare allows implementation of custom authentication providers.</p>

### Custom authentication provider###

In order to implement a custom authentication provider you will have to implement a GroupShare plugin. Building such a plugin is very similar experience to building an SDL Studio plugin. Since GroupShare is built using Microsoft .NET you will have to use the Microsoft development platform and to be more specific for GroupShare 2015 you will need to use Microsoft .NET 4.5.2 version. The tool of choice for doing Microsoft .NET development is [Visual Studio](https://www.visualstudio.com/). You can use any flavor of Visual Studio (including the [free community edition](https://www.visualstudio.com/products/visual-studio-community-vs)) but since you need to build your plugin for Microsoft .NET 4.5.2 you will have to use Visual Studio 2013 or later. Here are the steps you need to follow to create the plugin:

1. Using Visual Studio create a new project of type Class Library.
2. Add reference to the following assemblies (both can be found under `SDL Server\Application` folder of your GroupShare install location):

	> Sdl.Core.PluginFramework.dll
	> 
	> Sdl.StudioServer.Api.Core.dll

3. Add a new class to the project and name it accordingly to your needs.
4. Open the newly created class and decorate it with the attribute `CustomAuthenticationProviderExtention`. Also set attribute property `CanValidateUserExistance` to true.

	`[CustomAuthenticationProviderExtention(CanValidateUserExistance = true)]`
 
5. Inherit the newly created class from `ICustomAuthenticationProvider`. This will require to create 2 methods in your class `UserExists` and `ValidateCredentials`.
6. Implemented this 2 new methods with your custom authentication logic.
7. Add a new xml file to your project with the following naming format `{yourcustomname}.plugin.xml`. This is used to describe the plugin you are building and it will be used by GroupShare to load your plugin. The content of your file has to follow a certain structure. You can use the following example to build yours:

<script src="https://gist.github.com/cromica/c8083af5d32caa6cdd63.js"></script>


### Signing ###

Before you can deploy your plugin to GroupShare your plugin assembly must be signed. To sign it please send your plugin assembly to `app-signing@sdl.com`.  

### Deploy ###

To deploy your plugin you will have to copy the plugin.xml file described at point 7 to the `SDL Server\Application\Plugins` folder of your GroupShare install location. Next you need to drop your plugin assembly in the `SDL Server\Application` folder. If you have other dependencies to your plugin please copy those also to the `SDL Server\Application` folder.

### Final words ###

You can find a complete sample implementation of a custom authentication provider [here](https://github.com/sdl/Sdl-GroupShare-Custom-Authentication-Provider).

Please let me know if you have any comments or questions.