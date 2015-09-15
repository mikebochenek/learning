---
layout: post
title:  "Setting up GWT"
date:   2009-02-16 13:15:51
categories: coding
---

Steps I followed to set up GWT

1. download eclipse 3.4
2. download gwt 1.5.3

{%highlight bash %}
http://code.google.com/webtoolkit/gettingstarted.html
applicationCreator -eclipse MyProject com.mycompany.client.MyApplication
cd \dev\gwt-windows-1.5.3
projectCreator -eclipse hcmLite
applicationCreator -eclipse hcmLite ca.bochenek.client.hcmLite
mkdir hcmLite
{%endhighlight%}
 
http://code.google.com/docreader/#p=google-web-toolkit-doc-1-5&s=google-web-toolkit-doc-1-5&t=DevGuideHostedMode

Tip: If you are using Eclipse, you can also create a launch configuration file when creating a new project with applicationCreator by using the -eclipse flag.
If you didn’t use applicationCreator to create an application-specific hosted mode shell script, you can manually run the main class in com.google.gwt.dev.GWTShell found (depending on your OS) in gwt-dev-windows.jar, gwt-dev-linux.jar, or gwt-dev-mac.jar.
