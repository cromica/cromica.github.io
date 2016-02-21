---
layout: post
image: ""
excerpt: null
category: 
  - SDL Studio
published: true
title: SDL Studio public API
---




<p class="dropcap"> I love writting code and most probably I said it before in other articles. Writting code means dealing with all sorts of API's all day long, starting from your development plaform, in my case <a href="https://www.microsoft.com/net" target="_blank">Micrososft .Net</a>, to different application or platform API's. In my humble opinion in today's world it's all about API's and if I were to decide to buy a piece of software for a company I wouldn't consider any which doesn't come with some sort development experience. I might not needed it today but it's definetly going to pay of on a longer term. Who want's to buy or use a product that doesn't offer flexibility? Based on the type of product, API's can come in multiple forms, for example SAAS products tend to offer nowadays some sort of <a href="https://en.wikipedia.org/wiki/Representational_state_transferREST" target="_blank">REST API</a> which can be consumed in different ways and devices. For traditional, desktop type, products the API is composed from certain classes, events and contracts that allow you to either hook into a certain process or to extend their user interface to some degree. As you probably figured it out in this article I will talk about the SDL Studio API's but what about the public word from the title?</p>

### Public vs Private API
The internet is full on debates on this topic trying to figure out pros and cons for this approach. My take on this is that there is no silver bullet solution and the decision should be made based on the specific context of the application/product, how the API is bringing value to the product and the impact on product delivery.

SDL Studio comes with a public API wich I will explain in detail in a bit but you might ask yourself why aren't all the application components public? At the end of the day the product it's just a bunch of assemblies/dll's that I can easily consume from my code/application. From a stricly technical standpoint this absolutely correct but other things have to be taken in consideration. Certain parts, that are considered internals, are changing quit often and that means your application/plugin that depend on those components might be broken with every change made, also there areas that were not necesarly build to be extensible (at least not for the moment). For SDL Studio the benefit of having a clearly defined public API is the  guarantee that changes are done in a controlled manner. Of course bugs may still pop-up as in any piece of software but we won't remove or change things overnight just because we need them in a certain way to develop a new feature or fix a bug.

### The SDL Studio public API's

At the time I'm writing this article SDL Studio comes with six public API's. We are also at the point to release two new public API's ([More details](https://community.sdl.com/developers/language-developers/f/61/t/6451)). For a clear understanding of each of the available API's in the following lines I will enumerate them and give some details about each of them together with the corresponding assemblies that you need to include in your application:

**[Core API](http://producthelp.sdl.com/SDK/Core/4.0/html/ecbcf309-0686-4cc0-85ef-a8963f73d369.htm)**

`This is the foundation which provides the plug-in framework available in SDL Studio. This is used by other API's to [Define Extension Points](http://producthelp.sdl.com/SDK/Core/4.0/html/c26dc9f8-a68a-4977-a20a-82b25f69efaa.htm) inside the host application which in this case is SDL Studio. You can use this libraries inside another host application if you are looking for a plugin framework and you want to provide this type feature. Besides the plug-in framework this API provides also the engine besides the settings mechanism you find inside SDL Studio`

In order to use the API you will need to reference the following assemblies:
- Sdl.Core.Globalization.dll
- Sdl.Core.PluginFramework.dll
- Sdl.Core.Settings.dll

**[File Type Support API](http://producthelp.sdl.com/SDK/FileTypeSupport/4.0/html/1f5584af-9763-46ff-894b-08127a2421a7.htm)**

`In order to translate the content from a certain file type SDL Studio extracts the content into a billingual file type called [SDLXliff](http://producthelp.sdl.com/kb/Articles/4529.html). Out of the box SDL Studio comes with a comprehensive list of file types that are supported but in case you have a particular file type that is not supported you can use this API to extract the content and create the SDLXliff needed for translation. Also you can extend existing file type to handle certain use case that might not work as expected. This API is also used by the out of the box filters.`

In order to use the API you will need to reference the following assemblies:
- Sdl.FileTypeSupport.Framework.Core.dll
- Sdl.FileTypeSupport.Framework.Core.Utilities.dll
- Sdl.FileTypeSupport.Framework.Core.Settings.dll
- Sdl.FileTypeSupport.Framework.PreviewControls.dll

**[Project Automation API](http://producthelp.sdl.com/SDK/ProjectAutomationApi/4.0/html/b986e77a-82d2-4049-8610-5159c55fddd3.htm)**

`There many activities that must be done as part of the translation process and this is why SDL Studio provides project management features such analysis, pre-translation, generation of finalized target documents,etc. Using the Project Automation API you can build a customized translation workflow based on activities specific to your needs.`

In order to use the API you will need to reference the following assemblies:
- Sdl.ProjectAutomation.Core.dll
- Sdl.ProjectAutomation.FileBased.dll
- Sdl.ProjectAutomation.Settings.dll

**[Translation Memory API](http://producthelp.sdl.com/SDK/TranslationMemoryApi/4.0/html/790076c4-fb7c-4c3d-9ad5-e7691c317500.htm)**

`Translation memories are an essenctial piece of technology for translators. Of course SDL Studio comes with this capabilities but in case you want to use a different piece of technology for translation memories you can enable that in SDL Studio by creating a new translation memory provider using the Translation Memory API.`

In order to use the API you will need to reference the following assemblies:
- Sdl.LanguagePlatform.Core.dll
- Sdl.LanguagePlatform.TranslationMemory.dll
- Sdl.LanguagePlatform.TranslationMemoryApi.dll
- Sdl.LanguagePlatform.IO.dll

**[Integration API](http://producthelp.sdl.com/SDK/StudioIntegrationApi/4.0/html/135dcb1c-535b-46a9-8063-b83be4a06d82.htm)**

`This API enables 3rd party developers to extend or customize the user interface or create custom functionalities for SDL Studio. To be more specific you can create new views, new sections in the menu ribbon, new buttons in the menu ribbon, new options in the context menu or hook into the editor to create, update or delete certain informations or you can get notified when certain events happen.`

In order to use the API you will need to reference the following assemblies:
- Sdl.DesktopEditor.BasicControls.dll
- Sdl.DesktopEditor.EditorApi.dll
- Sdl.Desktop.IntegrationApi.dll
- Sdl.Desktop.IntegrationApi.Extensions.dll
- Sdl.TranslationStudioAutomation.Licensing.dll
- Sdl.TranslationStudioAutomation.IntegrationApi.dll
- Sdl.TranslationStudioAutomation.IntegrationApi.Extensions.dll

**[Verification API](http://producthelp.sdl.com/SDK/Verification/4.0/html/4bc459fe-8ca2-4686-8764-616ebb5ce526.htm)**

`SDL Studio allows translators to check their work by runining verifiers during translation. There can be many ways to verify the quality of a translation and it can also become verify specific so to cope with that need SDL Studio allows custom verifiers to be build and run.`

In order to use the API you will need to reference the following assemblies:
- Sdl.Verification.Api.dll

**[Batch Task API](https://community.sdl.com/developers/language-developers/f/61/t/6451)**

`As part of project management workflow there certain tasks that must happen, like pre-translation, analysis and so on. SDL Studio is coming with a predefined set of tasks but you also create your custom tasks that can be included in your workflows. This API is linked to the Project Automation API but since it's a new addition it's worth mention it separately.`

In order to use the API you will need to reference the following assemblies:
- Sdl.ProjectAutomation.AutomaticTasks.dll

**[Terminology Provider API](https://community.sdl.com/developers/language-developers/f/61/t/6451)**

`Multiterm is the defacto technology for handling terminology in SDL Studio. This API allows 3rd party developers to enable different terminology technology in SDL Studio by creating new terminology providers.`

In order to use the API you will need to reference the following assemblies:
- Sdl.Terminology.TerminologyProvider.Core.dll

For each of the API's I've listed the corresponding assemblies but based on your needs you can combine them. A plugin might have dll's from Core API combined with dll's from Project Automation API.

Please let me know if you have any questions.



