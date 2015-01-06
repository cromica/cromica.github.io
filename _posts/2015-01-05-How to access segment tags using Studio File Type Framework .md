---
layout: post
title:  "How to access segment tags using Studio File Type Framework"
date:   2015-01-05 16:20:00
category: "SDL Studio"
tags: "Studio plugins OpenExchange Framework File "
summary: "SDL Studio plugin system allows developers to develop new features on top of the standard functionality. There are 2 types of plugins that can be developed, one which behaves like a Studio add-in and another one which behaves as a standalone application. Both plugin types require to run inside Studio installation folder. This is because the public Studio SDK is using other assemblies that are located in Studio folder. While this is perfectly fine for add-in type plugins for standalone plugins this adds limitation on where and how you can deploy your application."
image: "/segmentTags/segments.png"
---

<img src="/assets/images/posts/segmentTags/segments.png" alt="Assembly Resolver" title="Assembly Resolver" class="img-responsive">

<p class="dropcap">Accessing segment tags might not be something you have to do everyday but there might be some scenarios where you need to manipulate the tags of your segments. This can be done using Studio File Type Framework which is part of the Studio SDK. The documentation is providing an overview of the entire framework and also includes high level overview of what I'm going to discuss in this article. </p>

### Visitor Pattern ###

Before jumping into the problem I recommend you to get familiarized with the visitor pattern since this is used as part of the Studio File Type Framework and you will need apply it in order to get the tags. To get familiarized you can read the theory on [wikipedia](http://en.wikipedia.org/wiki/Visitor_pattern) or if you want a practical example you can have a look [here](http://www.codeproject.com/Articles/588882/TheplusVisitorplusPatternplusExplained).

In Studio File Type Framework visitor pattern is made available via *IMarkupDataVisitor* interface. 
  
### Paragraphs, Segments and more ###

When a document is opened for translation Studio brakes it into segments. This is done by the segmentation engine using the segmentation rules defined in Studio. A segment can be a paragraph or a sentence length but what is important to understand is that for Studio a segment represents a piece of localizable content for which existing translations can possibly be used. Besides localizable content there are other elements, like formatting, that Studio needs to take into considerations.

Now that we have a better understanding of how Studio is handling the content let me highlight how this is reflected in the File Type Framework:

``IParagraph`` represents the entire content that is displayed on one Studio editor row. This can contain multiple elements like tags or segments.

``IParagraphUnit`` a unit of source language content and the localized target language content. Source and Target can be accessed using the corresponding properties which will return an *IParagraph* object instance with the information described above. One thing to keep in mind is that there are two type of paragraph units:

1. Structure paragraph units will contain only structure tags that are not localizable. In this case the Target will be null.
2. Localizable paragraph units will contain localizable content.


``ISegment`` represents a piece of localizable content.

``ISegmentPair`` segments exists in source and target language versions which are bot accessible using *ISegmentPair*. 

Segments and Paragraphs are considered containers of other elements like text, comments, revisions and so on. All containers share common behavior and that's why in the File Type Framework both are abstracted using *IAbstractMarkupDataContainer*. An *IAbstractMarkupDataContainer* contains multiple *IAbstractMarkupData* elements. This means that text, comments and other similar elements are represented in the framework using *IAbstractMarkupData* interface. One very important aspect of this structure is the fact that a segment can be considered as an element of the paragraph but also as a container for other elements which means that it can be manipulated as an *IAbstractMarkupDataContainer* or as an *IAbstractMarkupData*.

Here's a diagram which describes the structure:

<img src="/assets/images/posts/segmentTags/abstractmarkupdatacontainer.png" alt="Abstract Markup Data Container" title="Abstract Markup Data Container" class="img-responsive">

### Access segment tags ###

All paragraph elements are like a tree structure that must be traversed using visitor pattern. For each paragraph unit we can look at the Source property which is an *IParagraph*. Thinking at the abstraction I was talking earlier an *IParagraph* is in essence an *IAbstractMarkupDataContainer* which in turn is an enumeration of *IAbstractMarkupData*. Here's a sample code on how you can iterate paragraph unit elements:

{% highlight csharp %}
IEnumerable<IAbstractMarkupData> container = paragraphUnit.Source;
 
foreach (var contentItem in container)
{
    //structure tag is not supported by IMarkupDataVisitor and you should ignore it
    IStructureTag stag = contentItem as IStructureTag;
       if (stag == null) continue;
                       
      contentItem.AcceptVisitor(new MarkupDataVisitor());
}	
{% endhighlight%}

There is one new thing in the above sample which I didn't discuss about.This is *MarkupDataVisitor* which is an implementation of the interface *IMarkupDataVisitor* I was mentioning in the visitor pattern section. Here's how the interface looks like:
{% highlight csharp %}
/// <summary>
/// Interface for the visitor in the visitor pattern implementation for translatable source / target 
/// content items in a localizable paragraph unit.
/// </summary>
public interface IMarkupDataVisitor
{
	/// <summary>
	/// Called by tag pair instances.
	/// </summary>
	/// <param name="tagPair"></param>
    void VisitTagPair(ITagPair tagPair);


	/// <summary>
	/// Called by placeholder tag instances.
	/// </summary>
	/// <param name="tag"></param>
    void VisitPlaceholderTag(IPlaceholderTag tag);


	/// <summary>
	/// Called by text instances.
	/// </summary>
	/// <param name="text"></param>
    void VisitText(IText text);


	/// <summary>
	/// Called by segment instances.
	/// </summary>
	/// <param name="segment"></param>
    void VisitSegment(ISegment segment);


	/// <summary>
	/// Called by location marker instances.
	/// </summary>
	/// <param name="location"></param>
	void VisitLocationMarker(ILocationMarker location);


	/// <summary>
	/// Called by comment marker instances.
	/// </summary>
	/// <param name="commentMarker"></param>
    void VisitCommentMarker(ICommentMarker commentMarker);


	/// <summary>
	/// Called by other marker instances.
	/// </summary>
	/// <param name="marker"></param>
    void VisitOtherMarker(IOtherMarker marker);


	/// <summary>
	/// Called by locked content instances.
	/// </summary>
	/// <param name="lockedContent"></param>
    void VisitLockedContent(ILockedContent lockedContent);


	/// <summary>
	/// Called by revision marker instances.
	/// </summary>
	/// <param name="revisionMarker"></param>
	void VisitRevisionMarker(IRevisionMarker revisionMarker);
}
{% endhighlight%}

As you can see you are now able manipulate each element type. For example if you need formatting information you can get it from the *ITagPair* interface. 

**Don't forget** that segments are containers as well so on *VisitSegement* method you need to traverse his structure in the same way as for the paragraph unit.

Please leave a comment if you have any questions or feedback.