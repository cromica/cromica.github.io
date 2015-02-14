---
layout: post
title:  "Click'n'Deploy Studio plugins"
date:   2015-02-12 23:20:00
category: "SDL Studio"
tags: "Studio plugins OpenExchange Deploy"
excerpt: "App stores changed the way we install and maintain software on our devices. You now have a single centralized place where you go and search for what you need, click a button and in a matter of minutes you have the app working on your device. In a similar way you can extend SDL Studio by going on OpenExchange store and download a plugin you would like or need. Now this works just fine for most of the Studio plugins or apps but there are situations when you need to develop something that is specific for your company and doesn't make sense to be public to everyone since it's probably irrelevant for them and it might also contain confidential information. It would be nice if you would be able to create your private store inside OpenExchange where you can have you apps centralized and search-able just by you  but such a feature is not available at the moment. This article and video is about an alternate solution for this type of scenarios."
image: "/click-n-deploy/click-n-deploy.png"
---

<a href="https://speakerdeck.com/cromica/clickn-deploy" taget="_blank"><img src="/assets/images/posts//click-n-deploy/click-n-deploy.png" alt="Click'n'Deploy" title="Click'n'Deploy" class="img-responsive"></a>

<p class="dropcap">App stores changed the way we install and maintain software on our devices. You now have a single centralized place where you go and search for what you need, click a button and in a matter of minutes you have the app working on your device. In a similar way you can extend SDL Studio by going on <a href="http://www.translationzone.com/openexchange/">OpenExchange</a> store and download a plugin you would like or need. Now this works just fine for most of the Studio plugins or apps but there are situations when you need to develop something that is specific for your company and doesn't make sense to be public to everyone since it's probably irrelevant for them and it might also contain confidential information. It would be nice if you would be able to create your private store inside <a href="http://www.translationzone.com/openexchange/">OpenExchange</a> where you can have you apps centralized and search-able just by you  but such a feature is not available at the moment. This article and video is about an alternate solution for this type of scenarios.</p>

### The solution ###

The solution is very simple and is based on the idea to automate as much as possible the process of releasing you plugin. The exact same thing is promoted by [Continuous Delivery](http://en.wikipedia.org/wiki/Continuous_delivery)  practice and together with the evolution of this a couple of release management tools like [Octopus Deploy](https://octopusdeploy.com/) or [GO](http://www.thoughtworks.com/products/go-continuous-delivery) appeared in order to ease the adoption of such a practice. In our case since Studio plugins are developed using [Microsoft .Net](http://www.microsoft.com/net) and it makes perfect sense to use [Octopus Deploy](https://octopusdeploy.com/) since is dedicated for .Net solutions. Of course you can try and use [GO](http://www.thoughtworks.com/products/go-continuous-delivery) or any other release management tool you prefer. If it's not clear by now the solution I'm talking about is to automate your Studio plugin release management using [Octopus Deploy](https://octopusdeploy.com/).   
 
  
### Octopus Deploy ###

I'm not going to cover in detail [Octopus Deploy](https://octopusdeploy.com/) since it comes with a very good documentation, rather I'm going to present a higher level overview of how is going to work with Studio plugins. Octopus comes with a central server component which is called [Octopus Deploy Server](http://docs.octopusdeploy.com/display/OD/Installing+Octopus) that you need to install somewhere where all your users machines will be able to access it. It can be an internal private server, a public server or somewhere in a cloud platform, there is no limitation as long as it's accessible. [Octopus Deploy Server](http://docs.octopusdeploy.com/display/OD/Installing+Octopus) comes with web user interface which you can use once you have the server installed. Besides the server component Octopus comes with a client component called [Tentacle Deploy agent](http://docs.octopusdeploy.com/display/OD/Installing+Tentacles). This has to be installed on each user machine and it will be used to deploy your software, in our case the Studio plugins. This is a one time operation and once it's done you will only use the web user interface that comes with the server. There is a third component called [OctoPack](http://docs.octopusdeploy.com/display/OD/Using+OctoPack) that is used to push the software/Studio plugin from you development or build machine to [Octopus Deploy Server](http://docs.octopusdeploy.com/display/OD/Installing+Octopus).  

### Click'n'Deploy Studio plugins ###

There are quit a few moving parts when you first setup [Octopus Deploy](https://octopusdeploy.com/) and some of the steps might not that obvious so instead off writing them in this article I decided that it would be better if just create a video to show you exactly how you configure Octopus to release Studio plugins to the user machine. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/mMDnY73D1x8" frameborder="0" allowfullscreen></iframe>

Useful learning resources:

1. [Octopus Deploy Getting Started](http://docs.octopusdeploy.com/display/OD/Getting+started)

2. [Installing Octopus Deploy Server](http://docs.octopusdeploy.com/display/OD/Installing+Octopus)

3. [Installing Tentacles](http://docs.octopusdeploy.com/display/OD/Installing+Tentacles)

4. [Using OctoPack](http://docs.octopusdeploy.com/display/OD/Using+OctoPack)

5. [What is Nuget?](https://www.nuget.org/)

6. [Develop SDL Studio plugins](http://www.translationzone.com/openexchange/developer/sdk.html)

Please leave a comment if you have any questions or feedback.