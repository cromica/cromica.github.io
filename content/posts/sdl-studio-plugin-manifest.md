+++
title = "SDL Studio plugin manifest"
date = 2016-09-23T09:07:09.000Z
lastmod = 2016-09-23T09:07:09.000Z
slug = "sdl-studio-plugin-manifest"
tags = ["SDL AppStore", "SDL Studio", "SDL Studio Plugins"]
featured = false
featured_image = "/images/2016/09/Optimized-56H.jpg"
ghost_id = "5a11ca067dd80546c26298e0"
migration_source = "ghost"
+++
This week I reached two years since I joined SDL as a [developer evangelist](http://developer-evangelism.com/). Stay relaxed, this article is not a retrospective of this period. However it is a milestone and as part of my own reflection over this interval of time I also looked at the blog articles I've written. Besides the fact that I could have done better in terms of how many articles I've written, I quickly realized that I didn't talk clearly enough about the [SDL Studio](http://www.sdl.com/cxc/language/translation-productivity/trados-studio/coming-soon/?InterestProfile=LTTranslatorProductivity) plugin manifest file. This is an important part of Studio plugin development which typically is just an afterthought. To some extent this is not a surprise as there wasn't an obvious reason why this is important, other than it was mandatory for creating the *.sdlpugin* file.

### Why Is Important

With SDL Studio 2015 we introduced a new tool called the [SDL Plugin Installer](http://appstore.sdl.com/app/sdl-plugin-installer/462/) which is deployed alongside Studio 2015, or if you have an older version of Studio you can download it from the App Store. This app greatly simplified the installation process of the downloaded plugins, removed the necessity of using an external installer technology during development and it quickly evolved into more than just an installer, it is now a plugin manager. [Paul Filkin](https://twitter.com/paulfilkin) already wrote in detail about this [here](https://multifarious.filkin.com/2016/04/24/managing-your-sdl-plugins/) so I'm not going to insist on this, rather I want to highlight that all the plugin information displayed by this plugin management app is coming from the *.sdlplugin* manifest file. So if almost nobody could see the info from the manifest file this is no longer true since 2015 and in order to provide a great experience, relevant information should be provided in the manifest file.

As I'm writing this article, we are getting closer and closer to the release of the new [SDL appstore](http://appstore.sdl.com/) backend. This might not have an immediate  direct impact on you, but this will enable us to develop our next step in terms of plugin management and with that the information will become more important in terms of providing the best user experience.

Last but not least is the fact that this file provides the developer the mechanism to specify with which SDL Studio version his plugin is compatible with.

### Plugin Manifest elements

The next screenshot is an example of a manifest file which covers all the important details.

![](/images/2016/09/plugin-manifest-1.png)

I can tell you this only takes a few minutes to fill, then you're done and in return you get happy users, I definitely think this is a good tradeoff. Some of the elements are self-explanatory, like name, author or description and for the version please have a look at the next section. So let's talk a bit about the rest of the elements:

* ==RequiredProduct== - this might be obvious especially the name attribute which in our case will always be *SDLTradosStudio*. The second attribute of this element,*minversion*, provides one of the most critical pieces of information which is the minimum product version with which the plugin is compatible. The SDL plugin installer will also use this piece of information to deploy it to the appropriate product versions. If this is not set accordingly to the compatible product version, it might cause a bad user experience which is unfortunate and should be avoided. You should test your plugin against the product version you want to release for. There is also a *maxversion* attribute which helps defining a very exact range of product compatibility.
* ==Include== - This element is just the parent for the ==File== element and by using this you can include external libraries that must to be deployed with your plugin. So instead of creating an installer that deploys all the plugin resources (dlls, images, configuration files, etc.) all you need to do is include all of them inside the *.sdlplugin* package and everything will be taken care of.

### Plugin Versioning

As you probably figured it out, this is done via the ==Version== attribute. This is a free text field so you can version as you see fit. I would recommend to use a well-known versioning technique like [Semantic Versioning](http://semver.org/) to avoid confusion. This piece of information is totally independent of the plugin [assemblies version](https://support.microsoft.com/en-us/kb/556041) and you can have them in sync or use different versions. I prefer to have them in sync because it simplifies my versioning strategy. An important aspect of the impact of the version field is that Studio will not unpack and load your new *.sdplugin* package if the version of the installed plugin is the same or higher as the version of your newly deployed one.

Also an important aspect to keep in mind is that the manifest version field has nothing to do with the version field from the App Store. They are completely independent.
