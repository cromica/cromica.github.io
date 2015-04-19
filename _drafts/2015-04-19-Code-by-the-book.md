---
layout: post
title:  "Code by the book"
date:   2015-04-19 19:20:00
category: "Career"
tags: "Code book programing development software"
excerpt: "SDL Studio allows the user to merge multiple files into one bilingual document (sdlxliff). This can be done during project creation and it can be useful in situations where you have multiple small files and you might want to translate them in one go without switching between documents.  If you don't already know SDL Studio is very extensible via the API's that are made available but sometimes simple things are not so simple to do by code because of software design decision or technical limitations. Merging files using SDL Studio Project Automation API can be done but is not that straight forward as you might expect and this is why I decided to write this article to show how this is done."
image: "code-by-the-book/books.jpg"
---

<img src="/assets/images/posts/code-by-the-book/books.jpg" alt="Code by the book" title="Code by the book" class="img-responsive">

<p class="dropcap">SDL Studio allows the user to merge multiple files into one bilingual document (sdlxliff). This can be done during project creation and it can be useful in situations where you have multiple small files and you might want to translate them in one go without switching between documents. If you don't already know SDL Studio is very extensible via the API's that are made available but sometimes simple things are not so simple to do by code because of software design decision or technical limitations. Merging files using SDL Studio Project Automation API can be done but is not that straight forward as you might expect and this is why I decided to write this article to show how this is done.</p>

### Create Merged Project File ###

Looking at the documentation you can easily find [CreateMergedProjectFile](http://producthelp.sdl.com/SDK/ProjectAutomationApi/3.0/html/8c0d6583-c31c-365b-0819-ff19e18e1f5e.htm) method which allows you to specify the files you want to be merged and the name of the bilingual file which must have ".sdlxliff" extension. At this point this seems to be very simple but when you run this method you realize that is not actually doing much, there is no visible result on the project and the status is *Not Merged*. 

### What am I missing? ###

At this point you only get an [MergedProjectFile](http://producthelp.sdl.com/SDK/ProjectAutomationApi/3.0/html/4ea34241-0524-aac3-45fa-817765b3bc5e.htm) object which is just a representation of the merging structure. In order to actually create the bilingual merged file we need to use [Studio File Type Framework](http://producthelp.sdl.com/SDK/FileTypeSupport/3.0/html/1f5584af-9763-46ff-894b-08127a2421a7.htm) to generate the sdlxliff file. Once we have that we can use *CopyToTargetLanguages* to copy the merged files to all target languages we need. To make this even more clear and concrete I'm going to share a sample code that is doing all the steps I've described until now.

<script src="https://gist.github.com/cromica/af1242f60511c52fba79.js"></script>

### Conclusion ###

It's not that complicated to merge files using the SDL Studio API but is not obvious and intuitive. I hope this article will clarify this situation. 

Please leave a comment if you have any questions or feedback.