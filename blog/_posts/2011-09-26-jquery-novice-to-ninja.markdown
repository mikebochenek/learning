---
layout: post
title:  "jQuery Novice to Ninja"
date:   2011-09-26 19:45:33
categories: coding
---

jQuery Novice to Ninja

{%highlight html linenos=table %}
<head>
<title>Hello jQuery world!</title>
<script type=”text/javascript” src=”http://ajax.googleapis.com/
?ajax/libs/jquery/1.4.0/jquery.min.js”></script>
<script type=’text/javascript’ src=’script.js’></script>
{%endhighlight%}

Dissecting a jQuery Statement
We know that jQuery commands begin with a call to the jQuery function, or its alias.  Let’s now take out our scalpels and examine the remaining component parts of a jQuery statement.  Figure 1.3 shows both variants of the same jQuery statement (using the full function name or the $ alias).

selector  action   parameters
{%highlight javascript linenos=table %}
jQuery(‘p’)   .css   (‘color’, ‘blue’);
$(‘p’)  .css  (‘color’, ‘blue’);
{%endhighlight%}

When you write your CSS, you can hook elements by id with a hash symbol, or by class with a period:
{%highlight javascript linenos=table %}
#footer { border: 2px solid black }
.warning { color: red }

$(document).ready(function() {
alert(‘Welcome to StarTrackr! Now no longer under police …’);
});

$(function() { alert(‘Ready to do your bidding!’); });
{%endhighlight%}

Can You Be More Specific?
Just like with CSS, we can select either $(‘.data’) or the more specific $(‘table.data’).  By  specifying an element type in addition to the class, the select or will only return table elements with the class data  rather than all elements with the class data.  Also, like CSS, you can add parent container select – or sto narrow your selection even further.

http://www.sitepoint.com/books/jquery1/, the website that supports this book

We’ve selected the containing element, and from that containing element we want to pick out all the descendants that are table rows: that is, we want to specify all table rows inside the containing table. To do this, we put a space between the ancestor and the descendant

Let’s take this idea a step further. Say we wanted to select all span elements inside of p elements, which are themselves inside div elements— but only if those divs happen to have a class of fancy. We would use the selector:
{%highlight javascript linenos=table %}
$(‘div.fancy p span’)
{%endhighlight%}

common jquery methods

- .css (name value pairs);
- .addClass (css classname to be added);
- .removeClass
- .hide
- .click (event handler)

Event handlers are named for their function of handling events. Events are actions and user interactions that occur on the web page. When an event happens, we say that it has fired. And when we write some code to handle the event, we say we caught the event.

When an event fires, we will often want to refer to the element that fired it. For example, we might want to modify the button that the user has just clicked on in some way. Such a reference is available inside our event handler code via the JavaScript keyword this. To convert the JavaScript object to a jQuery object, we wrap it in the jQuery selector:

This introduces the is action. is takes any of the same selectors we normally pass to the jQuery function, and checks to see if they match the elements it was called on. In this case, we’re checking to see if our selected #disclaimer is also selected by the pseudo-selector :visible. It can also be used to check for other attributes: if a selection is a <form> or <div>, or is enabled.

jQuery performs several useful actions when you write this code: it parses the HTML into a DOM fragment and selects it—just as an ordinary jQuery selector does. That means it’s instantly ready for further jQuery processing. For example, to add a <class> to our newly created element, we can simply write:
{%highlight javascript linenos=table %}
$(‘<p>A new paragraph!</p>’).addClass(‘new’);
{%endhighlight%}

{%highlight javascript linenos=table %}
$(‘#celebs tr’).remove(‘:contains(“Singer”)’);
{%endhighlight%}
Rather than removing every <tr> in the #celebs <div>, this code will remove only those rows which contain the text “Singer.” This will come in handy when we look at some advanced effects in the next chapter.

interesting aniumation functions:  fadeout()  toggle()  slideToggle()

In JavaScript, functions that are defined inline (such as our callbacks and event handlers) are called anonymous functions. They are referred to as “anonymous” simply because they don’t have a name! You use anonymous functions when you only require the function to be run from one particular location.

In any situation where we’re using anonymous functions, it’s also possible to pass a function name yet define the function elsewhere. This is best done when the same function needs to be called in several different places. In simple cases like our examples, this can make the code a bit harder to follow, so we’ll stick with anonymous functions for the moment.

listing 2-37. chapter_02/31_hover_action/script.js(excerpt)
{%highlight javascript linenos=table %}
$(‘#celebs tbody tr’).hover(function() {
$(this).addClass(‘zebraHover’);
}, function() {
$(this).removeClass(‘zebraHover’);
});
{%endhighlight%}
