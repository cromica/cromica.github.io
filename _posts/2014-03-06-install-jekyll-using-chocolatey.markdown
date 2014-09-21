---
layout: post
title:  "Install Jekyll using Chocolatey"
date:   2014-03-06 19:14:00
category: "Jekyll"
tags: "Jekyll Chocolatey Ruby Python Windows Blogging Github"
summary: "As you probably already know this website and blog is created using github pages which behind the scene uses Jekyll. More on this you can read on my blog post.Every time I write a new article or make a change I would like to preview it before publishing it to live website."
image: ""
---
<p class="dropcap">As you probably already know this website and blog are created using github pages which behind the scene uses Jekyll. More on this you can read on my <a href="http://romuluscrisan.com/blog/2014/03/03/the-engine-behind-my-blog.html">blog post</a>.Every time I write a new article or make a change I would like to preview it before publishing it to live website.When this get published to my website repository, Github builds it almost instantly so I'm able to see my change really fast, but this is still done on the public website. This can work pretty well but I prefer to see my changes locally and only if I'm ok to publish them on my <a href="https://github.com/cromica/cromica.github.io">repository</a>. So in order to do that I need to install jekyll on my local machine and use `jekyll serve` to build and serve the website.</p>

### Install Jekyll on a Windows machine ###

Jekyll is build with Ruby and uses some Python libraries so we need to install them in order to run Jekyll. Since most the work I do is around Microsoft .Net platform I need to use Windows operating system . My source of inspiration was this [article](http://blog.davidebbo.com/2014/01/converting-my-old-blog.html) by David Ebbo. In his artcile he points to this [article](http://yizeng.me/2013/05/10/setup-jekyll-on-windows/) which explains all the steps in detail. The information is perfectly valid at this moment so you can follow that too but I would like to show you a simple way using [Chocolatey](https://chocolatey.org/). The steps are pretty much the same with the article, the only difference is in the way you install the applications.

### What is Chocolatey ? ###

>Chocolatey is a global PowerShell execution engine using the NuGet packaging infrastructure. Think of it as the ultimate automation tool for Windows.

It is very simple to install Chocolatey you just have to run this script on your command prompt:

{% highlight powershell %}
@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%systemdrive%\chocolatey\bin
{% endhighlight%}

If this doesn't work for you there are other ways to install chocolatey [here](https://github.com/chocolatey/chocolatey/wiki/Installation).

Now that we have chocolatey installed we can open a command prompt and using `cinst` we can install what we need. 
### Install Ruby ###

Run the following command on the command prompt:
>cinst ruby

To check if it was installed with success open a new command prompt and run:
> ruby --version

### Install Ruby Devkit###

Unfortunately at this moment there is no devkit package for ruby 2.0 on chocolatey but for sure it will be released pretty soon. Until then this are the steps to install (taken from this [post](http://yizeng.me/2013/05/10/setup-jekyll-on-windows/)):

1.Go to [http://rubyinstaller.org/downloads/](http://rubyinstaller.org/downloads/)

2.Download "Developemnt Kit" installer that matches the Windows architecture and the Ruby version just installed, which can be found with the following command `ruby --version`

3.Run the installer and extract it to a folder, e.g. `C:\DevKit`

4.Initialize and configure `config.yml` file. In the command prompt type the following:
>cd "C:\DevKit"

>ruby dk.rb init

>notepad config.yml

This will open notepad where you need to add `- C:\ruby200` at the end of the file.

5.After this step you need to go back to the command prompt and install gem:
>ruby dk.rb review

>ruby dk.rb install

At this point you should have gem installed. You can check it this way:
>gem --version

### Install Jekyll###
Run the following command on the command prompt:
>gem install jekyll -v 1.4.2

At this moment the latest version of jekyll is 1.4.3 but this has some issue on windows if you install pygments for syntax highlighting, so for now I recommend to stick to version 1.4.2.

### What is Pygments ?###

>Pygments is a generic syntax highlighter for general use in all kinds of software such as forum systems, wikis or other applications that need to prettify source code.
 
Pygments is written in python so we need to install Python

### Install Python ###
Run the following command on the command prompt:
> cinst python

Run the following command in a new command prompt to verify installation:
>python --version

### Install 'Easy Install' ###
Easy Install is a mechanism similar with ruby gems or chocolatey for python packages. In order to install it follow the steps:

1.Download [ez_setup.py](https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py)

2.Run the following command from the location where you saved ez_setup.py
>python ez_setup.py

3.Set the  'Python Scripts' directory (e.g. `C:\Python27\Scripts`) to PATH

4.Verify that easy_install is installed properly:
> easy_install --help

### Install Pygments ###
Now that we have python and easy install all we just need to run the following commnad to install pygments:
>easy_install pygments


### Start Jekyll###

You can now create a new Jekyll blog which can be browsed on [localhost:4000](http://localhost:4000):
>jekyll new myblog

>cd myblog
    
>jekyll serve

I found it much easier to install all this using Chocolatey. I'm keen to get your feedback on this.