---
layout: post
title:  "Running Brakeman"
date:   2015-03-13 06:43:48
categories: coding
---

[Brakeman](http://brakemanscanner.org/) is a Rails Security Scanner.  To be exact, it is a "static analysis security scanner for Ruby on Rails".  Amongst others, it covers the [OWASP Ruby on Rails Cheatsheet](https://www.owasp.org/index.php/Ruby_on_Rails_Cheatsheet)

my unix commands to run brakeman:
{%highlight bash linenos %}
sudo gem install brakeman
brakeman

cd ~/github/arvados/apps/workbench
brakeman -o /tmp/workbench-report.html
cd ../../services/api
brakeman -o /tmp/api-report.html
{%endhighlight%}

The scanner found a couple of interesting issues:

- see [Arvados API report]({{ site.url }}/blog/downloads/arvados-api-brakeman-report.html)
- see [Arvados Workbench report]({{ site.url }}/blog/downloads/arvados-workbench-brakeman-report.html)
