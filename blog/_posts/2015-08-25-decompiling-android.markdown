---
layout: post
title:  "Decompiling Android"
date:   2015-08-24 23:45:12
categories: coding
---

I've been wanting to try to decompile some Android applications for a while, and I finally got around to experimenting with it.  I don't plan on becoming an expert, and my time was severly limited.

Googling I found some answers on stackoverflow: [answer #1](http://stackoverflow.com/questions/5257830/how-to-use-dextojar/19954951#19954951), 
[answer #2](http://stackoverflow.com/questions/21010367/how-to-decompile-a-apk-or-dex-file-on-android-platform) and this repo on [github](https://github.com/dirkvranckaert/AndroidDecompiler)

## Attempt #1 - Simplify: Generic Android Deobfuscator

{%highlight bash %}
git clone https://github.com/CalebFenton/simplify
sudo apt-get install gradle
gradle shadowJar
{%endhighlight%}

## Attempt #2 - jadx: Dex to Java decompiler

{%highlight bash %}
git clone https://github.com/skylot/jadx
gradle dist
cd ~/github/jadx/build/jadx/bin
./jadx-gui
{%endhighlight%}


At first, I had issues building jadx:
{%highlight bash %}
Could not find method jcenter() for arguments [] on repository container
{%endhighlight%}

But that was quickly overcome by the hints from [stackoverflow](http://stackoverflow.com/questions/27470443/could-not-find-method-jcenter-for-arguments-on-repository-container)

And I also realized that I had been using the wrong (old) version of gradle

{%highlight bash %}
[ Mon Aug 24 22:35:01 ~/github/jadx ] gradle -version

------------------------------------------------------------
Gradle 1.4
------------------------------------------------------------

Gradle build time: Monday, September 9, 2013 8:44:25 PM UTC
Groovy: 1.8.6
Ant: Apache Ant(TM) version 1.9.3 compiled on April 8 2014
Ivy: non official version
JVM: 1.7.0_75 (Oracle Corporation 24.75-b04)
OS: Linux 3.13.0-37-generic amd64
{%endhighlight%}

And what I really wanted was a newer version of gradle

{%highlight bash %}

[ Mon Aug 24 22:40:11 ~/github/jadx ] ~/tools/gradle-2.6/bin/gradle -version

------------------------------------------------------------
Gradle 2.6
------------------------------------------------------------

Build time:   2015-08-10 13:15:06 UTC
Build number: none
Revision:     233bbf8e47c82f72cb898b3e0a96b85d0aad166e

Groovy:       2.3.10
Ant:          Apache Ant(TM) version 1.9.3 compiled on December 23 2013
JVM:          1.7.0_79 (Oracle Corporation 24.79-b02)
OS:           Linux 3.13.0-37-generic amd64
{%endhighlight%}

## Helpful links and resources:

- [One way of downloading APKs](http://apk-dl.com/)
- [dex 2 jar](https://github.com/pxb1988/dex2jar)
- [apktool](https://code.google.com/p/smali/) and [apktool docs](http://ibotpeaches.github.io/Apktool/documentation/)
- [java decompiler](http://jd.benow.ca/)
- [android cracking blog](http://androidcracking.blogspot.ch/2011/02/writing-large-amounts-of-smali.html)


![jadx-gui screenshot]({{ site.url }}/blog/downloads/jadx-gui-screen.png)
