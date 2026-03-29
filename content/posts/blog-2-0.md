+++
title = "Blog 2.0"
date = 2016-09-18T04:54:00.000Z
lastmod = 2016-09-18T05:36:51.000Z
slug = "blog-2-0"
tags = ["Blogging", "Ghost", "Github Pages"]
featured = false
featured_image = "/images/2016/09/photo-1470225620780-dba8ba36b745.jpg"
ghost_id = "5a11ca067dd80546c26298df"
migration_source = "ghost"
+++
It's been awhile since I've written my last article and if you've been on my blog before you will probably notice that it has new look. I was absolutely fine with the previous design and I didn't have any intention to change it but this came as a side effect of changing my blogging platform. If you followed my blog, you probably knew I was using [Github Pages](https://pages.github.com/) and that worked great for me until it didn't. This article will talk more about why I moved from [Github Pages](https://pages.github.com/) but if you are still interested in my initial setup have a look [here](/my-journey-to-start-a-blog/).

### Why I did it?

As I've said, this worked great for me until the point where I had problems building and publishing the blog. All my machines (laptop/desktop) are using Windows and unfortunately I had all sorts of problems with Jekyll on Windows, the templating engine that sits behind [Github pages](https://pages.github.com/), and not only that but also different ruby gems which don't install properly on Windows. There are all sorts of workarounds for this issue and in the end I managed to make it work but keeping up the environment was a bit of a challenge from time to time. I ended up even having an Ubuntu machine in Microsoft Azure just for publishing new articles. 

So yes, this all worked but at the end of the day the purpose of the blog is to write. For me writing is not second nature, so I realized as I started to write more often that the blogging engine was not helping me at all. Keeping it up required more attention so every time I wanted to write my focus had to go on technicalities around the engine.

Maybe it's just me but I wanted to be able to focus just on writing rather than other technicalities. I enjoyed learning all the things around [Github pages](https://pages.github.com/) because they were really interesting and different especially for a .Net guy.

### The New Blogging Platform

Recently my wife decided to start a blog and when I choose the platform for her I needed something that was simple and didn't require much technical skill. I ended up choosing [Ghost](https://ghost.org/) which is an open-source blogging platform that allows you to write articles using Markdown. You can download the source code, change it and host it yourself or everywhere your heart desires. While this is great, I didn't have time to manage all this for her so we ended up using Ghost Pro which is a hosting service provided by the team who develops the software. I have to say I immediately started to envy her for the simplicity she was writing the articles (this is most probably also related to the fact she is a better writer than me).

Migrating the content was easy since all my articles were already written in markdown so all I had to do is move them on Ghost and make some small adjustments (image links). The biggest problem was that my old design was not compatible with Ghost and the work to make it compatible was significant so I decided to use a Ghost theme. Once I had the design and articles, the only issue left was the different article URLs that Ghost is generating. Since I'm using Ghost Pro the support team sorted the URL redirects that needed to be done in order for the old links to work and voila this is it **Blog 2.0**.

Enjoy.
