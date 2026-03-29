+++
title = "Explore GroupShare 2017 REST API's using swagger"
date = 2017-07-17T17:39:49.000Z
lastmod = 2017-07-17T17:39:49.000Z
slug = "explore-groupshare-2017-rest-apis-using-swagger"
featured = false
featured_image = "/images/2017/07/cave-2129548_1920.jpg"
ghost_id = "5a11ca067dd80546c26298eb"
migration_source = "ghost"
+++
As a developer I'm always interested in a products API's and SDL Trados GroupShare 2017 is no exception. Among many improvements this new release also comes with a much improved REST API. There's a lot to talk around this topic but for this article I want to briefly introduce you to a neat way of exploring and learning the API's. With this new release SDL Trados GroupShare 2017 comes with [Swagger](https://swagger.io/specification/), which is a small framework that gives the developer a nice way to document REST API's and more than that even make real calls using available endpoints. I found this an awesome facility as I can immediately jump and start experimenting with the API's.

### I tried but something went wrong

It's true that you can immediately start doing tangible things with the SDL Trados GroupSahre 2017 REST API documentation, however for the api endpoints to work you need to authenticate. In GroupShare this is done using a username and password but for the API's that's not enough and you we will need to obtain a special token. There a few simple steps to that must be done to obtain the required token:

* On the top right hand side you should see a username and password field. Add your credentials there
* Search for the ==signin== endpoint under the ==Login== area.
* Expand the endpoint and specify the scope (specify the values described from the action notes section)
* Click *Try it out*
* If the response code is 200, copy the result (should be a big ugly string) into the token field (near the username and password)
* You're done with authentication. You should be able to try other available actions

Just in case the above points don't make too much sense I also recorded a short video that describe the above steps:

<iframe width="560" height="315" src="https://www.youtube.com/embed/jmaZyarM-8s" frameborder="0" allowfullscreen></iframe>

### Where's the documentation page?

The documentation page is part of your SDL Trados GroupShare 2017 installation under 
`/documentation/api/index` url path. You also need to make sure that the url specifies port `41234`. This should be like `http://www.yourUrl:41234/documentation/api/index`

Enjoy!
