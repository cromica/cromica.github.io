---
layout: post
title:  "The engine behind my blog"
date:   2014-03-03 21:52:21
category: "Blog"
tags: "Jekyll Blogging Github"
excerpt: "I guess it's time to dive a bit more on what technology stands behind my blog. In the previous posts I've talked about the reasons to start a blog, why I choose github pages to host it and now I will talk about Jekyll, the engine behind my blog."
image: ""
---

<p class="dropcap">I guess it's time to dive a bit more on what technology stands behind my blog. In the previous posts I've talked about the <a href="http://www.romuluscrisan.com/blog/2014/02/23/why-a-blog.html">reasons to start a blog</a>, <a href="http://www.romuluscrisan.com/blog/2014/02/24/why-i-choose-github-pages.html">why I choose github pages</a> to host it and now I will talk about Jekyll, the engine behind my blog.</p>

### What is Jekyll ? ###

Jekyll is a parsing engine which generates static html pages from dynamic components like template or markdown files. It uses a simple inline syntax which at build time is evaluated and replaced resulting a static page. Here is a short and very simple example:
{% highlight html %}
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<title>{{ "{{ page.title " }}}}</title>
{% endhighlight%}

In the above example the value for the title tag will be set with the value of the title property of the page object. Jekyll has a simple and limited syntax so it's quit easy to learn it, but it has great flexibility with lots of options on how to build the site. Also you can have partial files which Jekyll will combine at build time.

Jekyll has a special folder structure which is used in order to generate the static website:

- **_includes** folder is used to define partial files which can then be added to various pages. Some possible partial files might be the footer or header which for sure will be nice to define in one place and use on all pages.

- **_layout** folder is pretty self explanatory and is the location where you will define the layouts of your pages.

- **_posts** folder is the location from where dynamic content/posts will be saved. Jekyll uses a markup language like Markdown for this kind of files.

- **_drafts** folder is where the working in progress stuff will be held since this location will not be evaluated at build unless `--draft` is specified.

- **_site** folder is the location from where Jekyll will serve the static pages. During the build process Jekyll will combine partial files and evaluate the syntax producing a static html file which will be saved in this folder.

### Jekyll and Github pages ###

Jekyll can be installed locally and since it has a small static webserver embedded it can be used in lots of ways to serve the website. Using `jekyll serve` you can build and browse the site. Beside this option you can use the site developed with Jekyll directly with Github pages since behind the scenes it uses Jekyll. So all you have to do is push your site developed with jekyll to a repository and Github will do the trick almost instant. Please be aware that this is not true for all Github repositories, it's only valid for Github pages repositories which must be created according to this [steps](http://pages.github.com/).  


My intention with this article was to give a high overview of what Jekyll means and some basic principles. If you are looking for more details please have a look [here](http://jekyllrb.com/) and [here](http://jekyllbootstrap.com/lessons/jekyll-introduction.html).

If you have any questions please don't hesitate and leave a comment.

