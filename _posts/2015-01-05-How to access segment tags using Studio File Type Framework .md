---
layout: post
title:  "How to access segment tags using Studio File Type Framework"
date:   2015-01-05 16:20:00
category: "SDL Studio"
tags: "Studio plugins OpenExchange Framework File "
summary: "SDL Studio plugin system allows developers to develop new features on top of the standard functionality. There are 2 types of plugins that can be developed, one which behaves like a Studio add-in and another one which behaves as a standalone application. Both plugin types require to run inside Studio installation folder. This is because the public Studio SDK is using other assemblies that are located in Studio folder. While this is perfectly fine for add-in type plugins for standalone plugins this adds limitation on where and how you can deploy your application."
image: "/assemblyresolver/assemblyresolver.jpg"
---

<img src="/assets/images/posts/assemblyresolver/assemblyresolver.jpg" alt="Assembly Resolver" title="Assembly Resolver" class="img-responsive">

<p class="dropcap">Accessing segment tags might not be something you have to do everyday but there might be some scenarios where you need to manipulate the formatting tags of your segments. This can be done using Studio File Type Support Framework which is part of the Studio SDK. The documentation is not touching this particular scenario so I will detail it as part of this article. </p>

### Visitor Pattern ###

Before jumping into the problem I recommend you to get familiarized with the visitor pattern since this is used as part of the Studio File Type Framework and you will need apply it in order to get the tags. To get familiarized you can read the theory on [wikipedia](http://en.wikipedia.org/wiki/Visitor_pattern) or if you want a practical example you can have a look [here](http://www.codeproject.com/Articles/588882/TheplusVisitorplusPatternplusExplained). 
  
### Paragraphs and Segments ###

When a document is opened for translation Studio brakes it into segments. This is done by the segmentation engine using the segmentation rules defined in Studio. A segment can be a paragraph or a sentence length but what is important to understand is that for Studio a segment represents a piece of localizable content for which existing translations can possibly be used. Besides localizable content there are other elements, like formatting, that Studio needs to take into considerations.

Now that we have a better understanding of how Studio is handling the content let me highlight how this is reflected in the File Type Framework:

``IParagraph`` explain paragraph

``IParagraphUnit`` explain paragraphunit

``ISegment`` explain segment

``ISegmentPair`` explain segment pair 

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