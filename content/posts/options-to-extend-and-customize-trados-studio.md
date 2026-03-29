+++
title = "Options to extend and customize Trados Studio"
date = 2017-03-08T16:48:22.000Z
lastmod = 2017-03-25T17:50:00.000Z
slug = "options-to-extend-and-customize-trados-studio"
featured = false
featured_image = "/images/2017/03/antique-1845268_1920.jpg"
ghost_id = "5a11ca067dd80546c26298e5"
migration_source = "ghost"
+++
I'm absolutely sure that Trados Studio is the most customizable product on the market. To me this a no brainer; all you have to do is to go to the [SDL AppStore](http://appstore.sdl.com/list/language/most-downloaded/) and have a look at the number of plugins and applications that are available. And that is not all, because there are at least the same number of customizations carried out which are not published on the store because they are built to fulfill a specific need. Depending on the extension or customization you either have something that adds a new options inside Trados Studio or you have an exe that you have to run alongside Trados Studio. In this article I want to talk about this two options and when and why you should choose them.

### "Why" is important

Both options require software development skills and rely on the same Trados Studio APIs. Deciding which type of extension/customization to build is key in order to provide the best solution to fulfill the user need. If you are looking to publish your application on the [SDL AppStore](http://appstore.sdl.com/list/language/most-downloaded/) then it is important to know that we encourage publishing of Trados Studio plugins instead of the standalone applications, and for every new extension or customization that is to be published we will not approve it as a standalone application unless there is a strong reason behind it. Of course there are still quite a few of them on the store and we are working to migrate them into plugins where appropriate.

### Standalone applications

The first version of Trados Studio APIs didn't allow any form of user interface extension so the only option to provide a friendlier experience was to build an application that ran alongside Trados Studio.

**Pros**

* They don't require Trados Studio to run.

**Cons**

* Limited to project automation and translation memory operations. 
* If your application works with the [Project Automation API](http://appstore.sdl.com/developers/sdk.html) it must be deployed in the Trados Studio application folder.
* Need to run a separate application besides Trados Studio.
* The Provided features will not be in the context of Trados Studio workflows.
* No support provided in the future Trados Studio appstore integration.
* The developer must create a custom installer.

### Trados Studio plugins

Plugins were around from the first version of the Trados Studio APIs but didn't support any form of user interface extension until the introduction of the [Integration API](http://appstore.sdl.com/developers/sdk.html).

**Pros**

* Integrate as part of Trado Studio workflows. 
* Provide Trados Studio contextual options.
* Ability to create custom file types, verifications, translation providers, terminology providers, display filters, project and batch task automation.
* No need to develop an installer as Trados Studio comes with the plugin installer.
* Ability to disable a plugin without having to uninstall it.

**Cons**

* Limited to certain user interface integration points inside Trados Studio.
* Plugin installer limited in terms of plugins dependency deployment.
 
To my mind most of the times building a plugin for Trados Studio should be the go to option most of the time. Although there are though situations where a standalone application is needed, like the [SDL Analyse](http://appstore.sdl.com/app/sdl-analyse/726/) where we wanted to give the user the ability to run an analysis outside Trados Studio.

Please leave a comment with your thoughts, ideas and suggestions.
