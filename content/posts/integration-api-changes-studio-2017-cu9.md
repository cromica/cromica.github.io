+++
title = "Integration API updates in Trados Studio 2017 CU9"
date = 2018-02-25T17:02:44.000Z
lastmod = 2018-12-04T13:08:43.000Z
slug = "integration-api-changes-studio-2017-cu9"
tags = ["Integration API", "SDL Studio", "SDL Studio Plugins", "Trados Studio"]
featured = false
featured_image = "/images/2018/02/rawpixel-com-559745-unsplash.jpg"
ghost_id = "5a926600209ba9225d66da14"
migration_source = "ghost"
+++
With the recent [Trados Studio 2017 CU9](https://gateway.sdl.com/apex/communityknowledge?articleName=CUs-Studio2017SR1) update there are 4 new cool additions to the ==[Integration API](http://producthelp.sdl.com/SDK/StudioIntegrationApi/2017/html/135dcb1c-535b-46a9-8063-b83be4a06d82.htm)==. All these changes came as feedback in the [developer community](https://community.sdl.com/developers-more/developers/language-developers/) so I'm really proud that I can now talk about them.

**[Update 4th December 2018] Please make sure you use System.Reactive in your project when using project notifications.**

### When setting active segment the control focus was not changing

When using the [SetActiveSegmentPair](http://producthelp.sdl.com/SDK/StudioIntegrationApi/2017/html/de2879a8-89ff-1959-d118-1b29aac7560b.htm) there was a problem where the focus was not moved to the correct editor control. In order to fix this issue the method exposes an additional boolean parameter, *setFocusOnSegment*, which gives the developer the ability to control the focus behaviour. By default the value is false in order to maintain ~~backwards compatibility~~ similar behaviour with existing implementations that already rely on this method.

`document.SetActiveSegmentPair(projectFile:projectFile, segmentNumnber:segmentNumber, setFocusOnSegment:true);`

### Adding comments to segments with track change on was not working

This is now fixed and is available without any changes to the method signature. In other words there's nothing to be done in your plugin. The fix affects all of the following methods:

* AddCommentOnSegment
* UpdateCommentOnSegment
* DeleteCommentOnSegment
* DeleteAllCommentsOnSegment

### Expose detailed information about current editor text selection

This is a new addition to the Integration API and is meant to provide more information around the current text selection set in the editor. You will now be able to get the following information related to a text selection:

* row number
*  segment id
*  cursor position
*  if the selection is empty or reversed

The following example creates an action on the Trados Studio ribbon which extracts the content selection information and displays it in the window. The purpose of this example is to show how to work with the new exposed information:
<script src="https://gist.github.com/cromica/4a9434a544c22f4bf91ab599a943042b.js"></script>

### Improved project notification

As a developer you're now able to get notified in your plugin when a project is created, opened or published. As we expect to expose more Trados Studio events in the future we decided that we need a simple mechanism for developers to register to the events so it was a good opportunity to introduce a new pattern called [event aggregator](https://martinfowler.com/eaaDev/EventAggregator.html). It's not mandatory to to read about this pattern in detail as the registering mechanism is straight forward but if you're looking to broaden your knowledge it's something worth reading about.

The following example creates a new view part on the projetcs view that will display and append a message every time a project is opened, created or published.
<script src="https://gist.github.com/cromica/6bc54468bfe6b15f493164c3783a485a.js"></script>

<i class="em em-clap"></i> Kudos for this awesome additions goes to the Studio engineering team.

Enjoy!

Photo by [rawpixel.com](https://www.rawpixel.com) on [Unsplash](https://unsplash.com/photos/sJEd2VfVTGE).
