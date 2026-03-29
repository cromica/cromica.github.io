+++
title = "Introducing Trados Studio Community Toolkit"
date = 2017-05-30T19:03:00.000Z
lastmod = 2017-05-31T06:29:57.000Z
slug = "introducing-trados-studio-community-toolkit"
tags = ["Development", "SDL AppStore", "SDL Studio Plugins", "Trados Studio"]
featured = false
featured_image = "/images/2017/05/cc0-picture-10013_HD.jpg"
ghost_id = "5a11ca067dd80546c26298ea"
migration_source = "ghost"
+++
More than 2 years ago I started an initiative to open source pretty much all the plugins and applications that are developed and maintained by SDL on our appstore. There's still work do be done in this space but at the point of writing this article there are around 30 plugins and applications that are published on the [SDL AppStore](http://appstore.sdl.com/list/language/) which are open sourced. If you are interested in more details on this please have a look [here](https://sdl.github.io/Sdl-Community/). 

### Why this toolkit was needed?

Working on [these plugins](https://sdl.github.io/Sdl-Community/), I hit the situation were I needed to implement a certain feature that was already part of another plugin or application. Because I was in a hurry (and as many other developers, lazy from time to time) all I did was to copy paste the implementation. That did the trick but soon I was in situations where I needed the same implementation in several other locations and it was not only one thing I had to duplicate. That was the point when I decided that it would make perfect sense to create a redistributable library that can be used across projects. I also believe that this has potential to help other developers or technical partners who are doing work around  developing Trados Studio plugins.

Some of you might ask why not add these features in the product? The main reason to have these features as a set of separate libraries is that I wanted to have more flexibility and speed in adding features. I didn't want to depend on specific product releases in order to add and experiment with new things and functionalities.

### What is the Trados Studio Community Toolkit?

The Trados Studio Community Toolkit is a collection of helper functions created with the objective of simplifying common developer tasks while building Trados Studio plugins. These are made available as a set of libraries (4 at the time of writing this article) that can be included in any existing Trados Studio 2017 plugins or applications. 

###  How can I use it?

Well this should be fairly easy if you're familiar with the Microsoft .Net development environment. The library is available via [nuget](https://www.nuget.org/packages?q=sdl.community.toolkit). You can also find more detailed steps on how to use the library [here](https://github.com/sdl/SDL-Studio-Community-Toolkit#getting-started).

### What if I need a certain feature?

The toolkit is also open source so if you need or want a feature that's not in there you can always send a [pull request](https://help.github.com/articles/about-pull-requests/) and I would be more than happy to accept your contribution. Make sure you have a look at the [contribution guideline](https://github.com/sdl/SDL-Studio-Community-Toolkit/blob/master/contributing.md) before sending the changes.

If you want to give some feedback, ask a question or suggest a new feature have a look [here](https://github.com/sdl/SDL-Studio-Community-Toolkit#feedback-and-requests).
