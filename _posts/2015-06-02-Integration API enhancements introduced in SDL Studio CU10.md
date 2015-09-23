---
layout: post
title:  "Integration API enhancements introduced in SDL Studio CU10"
date:   2015-06-02 19:00:00
category: "SDL Studio"
tags: "Studio OpenExchange plugin"
excerpt: "Latest SDL Studio update, cumulative update 10, was released on 13th of May and together with this update there a few additions to the integration API. If you want to see the entire list of changes included in this update have a look at the sdl knowledge base. Now lets get down to business and talk about the integration api changes."
image: "integration-api-enhancements-cu10/integration-api-enhancements-cu10.jpg"
---

<img src="/assets/images/posts/integration-api-enhancements-cu10/integration-api-enhancements-cu10.jpg" alt="Integration API enhancements introduce in SDL Studio CU10" title="Integration API enhancements introduce in SDL Studio CU10" class="img-responsive">

<p class="dropcap">Latest SDL Studio update, cumulative update 10, was released on 13th of May and together with this update there a few additions to the integration API. If you want to see the entire list of changes included in this update have a look <a href="http://kb.sdl.com/#tab:homeTab:crumb:7:artId:5375" target="_blank">here</a>. Now lets get down to business and talk about the integration api changes.</p>

### Table of contents ###

This is a pretty long post and you might not want to read through the entire article so if you want to read only a specific topic I prepared a jump-list with the topics I cover in this article:

1. [Segment translation on-demand](#segment-translation-on-demand)
2. [Active file properties](#active-file-properties)
3. [Access/update segment and paragraph unit properties](#accessupdate-segment-and-paragraph-unit-properties)
4. [CRUD operations on comments](#crud-operations-on-comments)
5. [Change segment confirmation level](#change-segment-confirmation-level)
6. [AutoSuggest provider icon](#autosuggest-provider-icon)
6. [Segment Content ready](#segment-content-ready)

### Segment translation on-demand ###

Segment translation is done by the translation providers that are configured and enabled at the project level. This can happen as a pre-translation step or when the current segment is changed by the user in the user interface. With this new feature added to the integration API a developer is able to request the translation of the current selected segment whenever this is needed. This can be done from the [EditorController](http://producthelp.sdl.com/SDK/StudioIntegrationApi/3.0/html/2a868ca0-831d-4614-9763-2bf928a0f3fb.htm). To see this in action you can look at this sample:
     
<script src="https://gist.github.com/cromica/4676c94c596aa174c4f4.js"></script>

This sample code is take from the [Controlled Machine Translation Providers](https://github.com/sdl/Sdl-Community/tree/master/Controlled%20Machine%20Translation%20Providers) plugin.

### Active file properties ###

Until now developers were only able to get information about [ActiveFile](http://producthelp.sdl.com/SDK/ProjectAutomationApi/3.0/html/2b0cadd0-8be7-eea2-f974-bb14bdcb6db8.htm) like statistics, language, project id and so on. There was no way to get information like creation date, change date, metada and so on. This is now possible using *ActiveFileProperties* property of the [Document](http://producthelp.sdl.com/SDK/StudioIntegrationApi/3.0/html/9bb61319-d033-7198-9aee-b29eb5f759e9.htm) class. Also an event was added to notify when the active file properties are changed.

### Access/update segment and paragraph unit properties ###

**Update 23.09.2015** - *This feature didn't make it in Studio 2014 CU10 and it's available only in Studio 2015* 

If you needed to make any work around segments the only available option was to use [ProcessSegmentPairs](http://producthelp.sdl.com/SDK/StudioIntegrationApi/3.0/html/b4f43e30-8ba6-f2c2-7ea2-883ab83d1d67.htm) method from the [Document](http://producthelp.sdl.com/SDK/StudioIntegrationApi/3.0/html/9bb61319-d033-7198-9aee-b29eb5f759e9.htm) class. Now this can do the trick but it's not straightforward to use and can be an overhead for simple scenarios, also this method was not providing any way to interact with paragraph units. We've now added a couple other options that provide more granularity and flexibility in how a developer is able to process segments. We also added  capabilities to work directly with paragraph units. Here's the list with the methods available:

1. *GetSegmentPairsFromParagraph* - Based on the paragraph id you can obtain the segment pairs of that paragraph

<script src="https://gist.github.com/cromica/92f94e278fe1c41d6a46.js"></script>

2. *UpdateSegmentPair* - updates the document with the specified segment pair

<script src="https://gist.github.com/cromica/4182815a61117b5a3dbb.js"></script>

3. *UpdateSegmentPairProperties* - updates the document with the specified segment pair properties

<script src="https://gist.github.com/cromica/233216998995c82eaaef.js"></script>

4. *UpdateParagraphProperties* - updates the document with the specified paragraph properties

<script src="https://gist.github.com/cromica/c755798e710a09b153aa.js"></script>

### CRUD operations on comments ###

 Adding comments was only possible using [Billingual API](https://community.sdl.com/developers/language-developers/f/57/p/3414/12658#12658). While this is fine when you want to do it for your custom file type is not productive to use it when you just want to add comments to your well known file type. To solve this issue the integration api has now specialized methods that allow [CRUD](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations for comments. Here's the list with the methods available: 

1. *AddCommentOnSegment*

<script src="https://gist.github.com/cromica/86234330eb378a3798de.js"></script>

2. *UpdateCommentOnSegment*

<script src="https://gist.github.com/cromica/5b1931864dcbe16935e1.js"></script>

3. *DeleteCommentOnSegment*

<script src="https://gist.github.com/cromica/a281d232959dbabe1222.js"></script>

4. *DeleteAllCommentsOnSegment*

<script src="https://gist.github.com/cromica/363b895641c7443c1bdf.js"></script>

### Change segment confirmation level  ###

Developers are now able to change the segment confirmation level using the integration API and also they can now subscribe to an event that is trigger when the confirmation level is changed.

<script src="https://gist.github.com/cromica/b70a13dd8c08f8882ecb.js"></script>

### AutoSuggest provider icon  ###

Developer can now add custom icons for their AutoSuggest providers.

<script src="https://gist.github.com/cromica/a55d2a6b9cbd848af1b7.js"></script>

### Segment Content ready  ###

There are situations where you may want to do some additional work after the translation has been done. To cover this type of situation the event *ActiveSegmentContentIsReady* was added to the [Document](http://producthelp.sdl.com/SDK/StudioIntegrationApi/3.0/html/9bb61319-d033-7198-9aee-b29eb5f759e9.htm) class.


Please leave a comment if you have any questions.