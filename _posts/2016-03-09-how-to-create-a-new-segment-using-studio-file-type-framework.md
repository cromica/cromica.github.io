---
layout: post
title: How to create a new segment using Studio File Type Framework
date: {}
category: 
  - SDL Studio
tags: Studio SDK plugins OpenExchange Framework File
image: "create-segments-file-type.jpg"
excerpt: "Until I started to work in the translation industry I lived with the impression that the translation of a certain content is just a mater of knowing the right languages. I never realized that when you translate something everyone expects the results to look and feel identical just with the text in another language. For example you expect to have the same headings, fonts, colors, paragraphs and so on. In my humble opinion I think this is one of the reasons (not the only one) why CAT tools should be preferred to manual translation because this tools are able to keep the same look and feel between your source and target content and allow the translator to focus on the actual translation. How CAT tools handle this is a really broad topic that is not fit for just a blog article but in the following lines I would like to talk a bit about how you can correctly add content in SDL Studio using it&#x27;s file type framework. This means adding new content programatically rather than adding it from the user interface."
published: true
---



![create segments]({{site.baseurl}}/assets/images/posts/create-segments-file-type.jpg)

<p class="dropcap">Until I started to work in the translation industry I lived with the impression that the translation of content is just a matter of knowing the right languages. I never realized that when you translate something everyone expects the results to look and feel identical, just with the text in another language. For example you expect the translated text to have the same headings, fonts, colors, paragraphs and so on. In my humble opinion I think this is one of the reasons (not the only one) why <a href="http://www.translationzone.com/products/cat-tools/" target="_blank">CAT tools</a> should be preferred to manual translation because these tools are able to maintain the same look and feel between your source and target content and allow the translator to focus on the actual translation of the text. How <a href="http://www.translationzone.com/products/cat-tools/" target="_blank">CAT tools</a> handle this is a really broad topic that is not fit for just a blog article but in the following lines I would like to talk a bit about how you can correctly add content in SDL Studio using it's file type framework. This means adding new content programmatically rather than adding it from the user interface.</p>

### How SDL Studio breaks the content

To properly handle any type of content during the translation process SDL Studio transforms the source content into a bilingual format called SDLXLIFF. This format is actually an xml file based on the XLIFF standard which stands for XML Localisation Interchange file format. This sounds pretty good but if you try to just read an actual SDLXLIFF it might give you a few headaches as it can be really hard to follow. Now there isn't a good reason to do such a thing but if you are trying to somehow parse this xml programmatically then you need to understand it before being able to implement you parser. This is why SDL Studio exposes the file type framework api which is an abstraction of the raw xml format that simplifies working with this type of bilingual format.

As part of transforming a piece of content into an SDLXLIFF SDL Studio also breaks it into so called segments based on specific segmentation rules that are governed by the product. For example such a segment can represent a paragraph or a sentence from the original content. What is important to understand here is that these segments, besides the actual text,also contain specific markup that is holding information about the look and feel, or style of the document (headings, fonts, tags etc.). In this article I'm not going to explain in detail how all this is represented in the file type framework api but about a year ago I wrote a blog article in which I explain this in detail so if you need more details please go [here](http://romuluscrisan.com/sdl%20studio/2015/01/06/How%20to%20access%20segment%20tags%20using%20Studio%20File%20Type%20Framework%20.html#paragraphs-segments-and-more), especially in the **Paragraphs, Segments and more** section.

### Create a segment from code

I guess it's about time to look at the code. In order to properly understand the code please make sure that you are at least familiar with the Paragraph and Segment concepts from the file type framework.

The sample code I'm about to share is showing how you would create a new segment that is added on the active segment in the editor. This is done using the [Integration API](http://producthelp.sdl.com/SDK/StudioIntegrationApi/4.0/html/135dcb1c-535b-46a9-8063-b83be4a06d82.htm) and the [File Type Support API](http://producthelp.sdl.com/SDK/FileTypeSupport/4.0/html/1f5584af-9763-46ff-894b-08127a2421a7.htm). The following text is added in the target segment:

>Place the photo printer on a flat, clean and dust-free surface, **in a dry location**, and _out of direct sunlight_.

<script src="https://gist.github.com/cromica/7a2ae9e07687a1913b8b.js"></script>

### Code walk-trough

This is quite a long example but I wanted it to be a meaningful example. Let me explain a bit about what the code does:

1. The first 10 lines of code are used to obtain the current active segment from the SDL Studio Editor. 
2. In order to create text, tags, comments and so on we need to use the [Document Item Factory](http://producthelp.sdl.com/SDK/FileTypeSupport/4.0/html/ec213843-28e2-c1a2-146c-691e67026710.htm) which is created at line 12.
3. From line 13 up to line 87 I can create a segment with text and tag pair elements that have different formatting's. The code is self explanatory so I'm not going to dwell on this.
4. The last 2 lines from the sample are used to update the current segment in the editor. Because the Integration API works on clones of the actual segments we need to create a temporary segment pair that is then passed to the update method

### Document item factory

In my sample I'm creating the instance of the [Document Item Factory](http://producthelp.sdl.com/SDK/FileTypeSupport/4.0/html/ec213843-28e2-c1a2-146c-691e67026710.htm) but if you are creating a new file type, custom batch task or extending an existing file type there is no need to create the instance on your own because this available as part of the [abstract content processor](http://producthelp.sdl.com/SDK/FileTypeSupport/4.0/html/6d8b8094-0fd3-c557-7217-909ed952ca75.htm).

### Outro

I hope this clarifies a little how CAT tool are actually handling bilingual content and how you can take advantage of the SDL Studio file type framework to create new content.

Please leave a comment if you have any questions.

*Picture: [misschristi1972 - Focus 52 Week Six](https://flic.kr/p/brjbNM)*
