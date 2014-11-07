---
layout: post
title:  "3rd party assemblies and SDL Studio plugins"
date:   2014-11-07 16:18:00
category: "SDL Studio"
tags: "Studio plugins OpenExchange"
summary: "Last week I was working at a new plugin for SDL Studio 2014 and I wanted to serialize some information in json. The best tool handle this type of operations in .NET, at least in my opinion, is Json.NET. It made perfect sense to use it but until now I didn't use any external dependencies in an SDL Studio plugin so I started to look into what options we have to deploy our plugins together with 3rd party assemblies."
image: "/3rdparty/3rdpartyassemblies.png"
---

<img src="/assets/images/posts/3rdparty/3rdpartyassemblies.png" alt="Hello SDL" title="Hello SDL" class="img-responsive">

<p class="dropcap">Last week I was working at a new plugin for SDL Studio 2014 and I wanted to serialize some information in json. The best tool handle this type of operations in .NET, at least in my opinion, is <a href="http://james.newtonking.com/json" target="_blank">Json.NET</a>. It made perfect sense to use it but until now I didn't use any external dependencies in an SDL Studio plugin so I started to look into what options we have to deploy our plugins together with 3rd party assemblies.</p>



### SDL Studio plugins ###

This is not a detailed look at what SDL Studio plugins are but I want to give a bit of context on how they are working. First of all each plugin has to be packed in a package with extension `.sldplugin` (this a zip file in essence). If you use the SDL Studio templates from Visual Studio this done for you automatically. Once you have the package you need to deploy it in one of the three location where SDL Studio is expecting plugins:

>1. $(CurrentUser)\AppData\Local\SDL\SDL Trados Studio\{Studio Version}\Plugins\Packages\

>2. $(CurrentUser)\AppData\Roaming\SDL\SDL Trados Studio\{Studio Version}\Plugins\Packages\

>3. $(ProgramData)\SDL\SDL Trados Studio\{Studio Version}\Plugins\Packages\

There is no difference between this locations so you can choose whatever you prefer. Once the package is in one of this locations when SDL Studio starts it will unpack the package, drop the content into a dedicated location and load the plugin assembly. This depends on where you deployed your package and can be one of this locations:

>1. $(CurrentUser)\AppData\Local\SDL\SDL Trados Studio\{Studio Version}\Plugins\Unpacked\

>2. $(CurrentUser)\AppData\Roaming\SDL\SDL Trados Studio\{Studio Version}\Plugins\Unpacked\

>3. $(ProgramData)\SDL\SDL Trados Studio\{Studio Version}\Plugins\Unpacked\

### Deploy 3rd party assemblies ###

Now that we have a brief understanding on how SDL Studio handles plugins let's see what options we have to deploy 3rd party plugins:

>1. Include the assemblies in the plugin package

>2. Create an installer which will copy the 3rd party assemblies into SDL Studio folder under $(ProgramFiles)

Although the second option can work I don't like it because it requires more work, administrative rights to deploy the assemblies and might intefere with Studio installation. This was also suggest by [David Fritch](https://community.sdl.com/members/davidfritch/default.aspx) in this [thread](https://community.sdl.com/phase_2_groups/sdl_openexchange_developers/f/39/t/3149.aspx) as a possible way to do it.

I consider the first option the right way to do it since it's very simple and clean. All you have to do is change the `pluginpackage.manifest.xml` which has to be part of the solution in order to generate the `.sdlplugin` file. By default this xml file contains some tags to specify the plugin name, version, description, author and required SDL Studio product. You will need to add an `<Include>` tag which in my case, for [Json.NET](http://james.newtonking.com/json), looked something like this:

{% highlight xml %}
<Include>
	<File>Newtonsoft.Json.dll</File>
</Include>
{% endhighlight%} 
   
You can have a look at my entire xml file [here](https://github.com/sdl/SDL-Community/blob/master/Controlled%20Machine%20Translation%20Providers/Sdl.Community.ControlledMTProviders/pluginpackage.manifest.xml#L9).

Please leave a comment if you have any questions or feedback.