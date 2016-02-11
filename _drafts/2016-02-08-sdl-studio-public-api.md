---
layout: post
image: ""
excerpt: null
category: 
  - SDL Studio
published: true
title: SDL Studio public API
---



<p class="dropcap"> I love writting code and most probably I said it before in other articles. Writting code means dealing with all sorts of API's all day long, starting from your development plaform, in my case <a href="https://www.microsoft.com/net" target="_blank">Micrososft .Net</a>, to different application or platform API's. In my humble opinion in today's world it's all about API's and if I were to decide to buy a piece of software for a company I wouldn't consider any which doesn't come with some sort development experience. I might not needed it today but it's definetly going to pay of on a longer term. Who want's to buy or use a product that doesn't offer flexibility? Based on the type of product API's can come in multiple forms, for example SAAS products tend to offer nowadays some sort of <a href="https://en.wikipedia.org/wiki/Representational_state_transferREST" target="_blank">REST API</a> which can be consumed in different ways and devices. For traditional, desktop type, products the API is composed from certain classes, events and contracts that allow you to either hook into a certain process or to extend their user interface to some degree. As you probably figured it out in this article I will talk about the SDL Studio API's but what's whit the public word?</p>

### Public vs Private API
The internet is full on debates on this topic trying to figure out pros and cons for this approach. My take on this is that there is no silver bullet solution and the decision should be made based on the specific context of the application/product, how the API is bringing value to the product and the impact on product delivery.

SDL Studio comes with a public API wich I will explain in detail in a bit but you might ask yourself why isn't entirely public? At the end of the day the product it's just a bunch of assemblies/dll's that I can easily consume from my code/application. From a stricly technical standpoint this absolutely correct but other things has to be taken in consideration. Certain parts, that are considered internals, are changing quit often and that means your application might be broken with every change made, also there areas that were not necesarly build to be extensible (at least not for the moment). For SDL Studio the benefit of having a clearly defined public API is the  guarantee that changes are done in a controlled manner. Of course bugs may still pop-up as in any piece of software but we won't remove or change things overnight just because we need them in a certain way to develop a new feature or fix a bug.

### The SDL Studio API's
