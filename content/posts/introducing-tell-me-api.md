+++
title = "Trados Studio QuickInfo - Introducing Tell Me API"
date = 2019-01-16T08:34:59.000Z
lastmod = 2019-01-17T09:11:28.000Z
slug = "introducing-tell-me-api"
tags = ["SDL AppStore", "SDL Studio Plugins", "Trados Studio"]
featured = false
featured_image = "/images/2019/01/question-mark-2492009_1920.jpg"
ghost_id = "5bfd584da168c83fd5399cd5"
migration_source = "ghost"
+++
I finaly got the chance to write about this new API that was introduced in Trados Studio 2019. This major release introduces a new functionality that let's me explore and invoke available Trados Studio commands and settings called "Tell Me". For more details about "Tell Me" please have a look [here](https://www.sdl.com/software-and-services/translation-software/sdl-trados-studio/tell-me-feature.html). Underneath this interesting functionality there's a new API that allows me to either enhance the default functionality with the commands and settings that are available in my Studio plugin or I have the ability to specify some additional search sources. A few ideas passed my mind, like the ability to search on the [SDL AppStore](https://appstore.sdl.com/language/), [Google](https://www.google.com/) or maybe some internal knowledge based system. To better understand the new API I created a studio plugin that allows me to directly search on google from Studio but I didn't publicly release it as I built as more of an experiment. Someday maybe ... if there's enough interest. Another reason why I didn't release the google plugin might be that I also started playing with another idea where Studio, via the "Tell Me" user interface, could provide all kinds of useful information, like conversations, math arithmetic or airport information. This idea turned into a concrete Trados Studio 2019 plugin that's available on the SDL AppStore  [SDL QuickInfo](https://appstore.sdl.com/language/app/sdl-quickinfo/938/).

![8hN7rW5qvM](/images/2019/01/8hN7rW5qvM.gif)

## How can I enhance "Tell Me" results?

One way to enhance the "Tell Me" results is to specify additional commands, actions or settings available with my plugin. The api is fairly simple and there are just 4 simple constructions I had to use in order to enhance the tell me results. 

1. In order to access the "Tell Me" API I needed to add a reference to `Sdl.TellMe.ProviderApi.dll` from my plugin. The dll is located in the Trados Studio 2019 installation folder and the process is the same as with any standard .net framework project.
2. After adding the reference I registered my plugin as a "Tell Me" provider. I then created a new class that is inherited from `ITellMeProvider` and also mark it with the `TellMeProvider` attribute.
3. Implementing the `ITellMeProvider` interface required me to set the Name property and the actions that are defined as part of this provider. For each provided action I specified a few keywords so that the Tell Me engine is able to match my actions when the user is searching.
4. In order to specify the action I wanted in my "Tell Me" provider, I created a new class that I inherited then from `AbstractTellMeAction` and implemented the execute method so that it performs the action I wanted.
<script src="https://gist.github.com/cromica/cf059ee2e5b253a8c3bab5a5e2b2939c.js"></script>

Support for "Tell Me" will be add to the new plugins developed under [SDL Community](https://github.com/sdl/Sdl-Community) and for existing ones it will be based on the need. 

## How can I enhance "Tell Me" by adding new search sources?

Before going forward I need to clarify the aspect of different search sources. The Tell Me user interface is able to display information coming from various places and sources. The default search source is the list of available commands and settings available in Trados Studio (and a bit more if I look at the previous section). Besides this default search source the Tell Me API allows me to define new search sources. Results from these additional search sources will not be returned unless the user enters in the search area the name of the search source prefixed by the `@` character. For example in order to get results from [SDL QuickInfo](https://appstore.sdl.com/language/app/sdl-quickinfo/938/) I need to write something like `@info *color*`. This instructs the Tell Me engine to identify a search source with the name `info` and inside that source to look for `color`.

In order to create and add a new search source, or search data provider, for "Tell Me" I had to carry out the following steps (make sure to have a reference to `Sdl.TellMe.ProviderApi.dll` as described in the previous section):

1. Define a "Tell Me" plugin loader. I needed this so that I am able to instruct Trados Studio 2019 about my new search data provider. This is a simple class that has to be decorated with the `TellMeSearchProvider` attribute and inherited from `ITellMePluginLoader`
<script src="https://gist.github.com/cromica/d8ffc5cdc51927e8cf6f63fc95ac4df1.js"></script>
2. Create a new search data provider that is specified at the first step. I had to inherit the search data provider from `ISearchDataProvider` interface. Besides the name and icon information this interface exposes two methods. One, `GetProviderForQuery(string query)`, that is allowing me to verify if the search source introduced by the user is matching my search data provider and `SearchForSuggestion(string query)` which is the method where the lookup for the specified query happens. It's important to understand that each search source/search data provider needs to implement it's own search engine. Trados Studio comes with a specialized search implementation for the commands and settings which might not be the best option in certain scenarios and that's why each search source should implement it's own engine.  
<script src="https://gist.github.com/cromica/654841159e3c6d04f23b880be01072d0.js"></script>

Don't hesitate to leave me a comment if you have any questions or suggestions.
