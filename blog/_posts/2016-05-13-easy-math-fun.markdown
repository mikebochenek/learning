---
layout: post
title:  "Some easy math fun"
date:   2016-05-13 15:55:42
categories: math
---

Several months ago, I saw this book somewhere and later ordered it on Amazon: [Professor Stewart's Casebook of Mathematical Mysteries](https://www.amazon.co.uk/dp/1846683483/ref=pe_385721_51767431_TE_dp_1)

## the problem

Multiply the following and find the pattern and predict the next results:

- 11 x 91
- 11 x 9091
- 11 x 909091
- 11 x 90909091
- 11 x 9090909091
- 11 x 909090909091
- etc.

I had tried this on paper (since I wanted to try some traditional math) and found a pattern right away.

## trying using a modern calculator

{%highlight bash %}
Welcome to Scala version 2.10.4 (Java HotSpot(TM) 64-Bit Server VM, Java 1.7.0_79).
Type in expressions to have them evaluated.
Type :help for more information.

scala> 11 * 91
res0: Int = 1001

scala> 11 * 9091
res1: Int = 100001

scala> 11 * 909091
res2: Int = 10000001

scala> 11 * 90909091
res3: Int = 1000000001

scala> 11 * 9090909091
<console>:1: error: integer number too large
       11 * 9090909091
{%endhighlight%}

Does this mean that I am smarter than a computer?
