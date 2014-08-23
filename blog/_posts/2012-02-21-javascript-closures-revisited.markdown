---
layout: post
title:  "Javascript Closures revisited"
date:   2012-02-21 15:33:52
categories: coding
---

High level concepts to remember

1. Functions can refer to variables defined in outer scopes.
2. Closures can outlive the function that creates them.
3. Closures internally store references to their outer variables, and can both read and update their stored variables.

Example #1

{% highlight javascript linenos %}
function sandwichMaker(magicIngredient) { 
   return function(filling) { 
     return magicIngredient + " and " + filling; 
   }; 
}
{% endhighlight %}

Example #2

{% highlight javascript linenos %}
function box() { 
   var val = undefined; 
   return { 
      set: function(newVal) { 
         val = newVal; 
      }, 
      get: function() { 
         return val; 
      }, 
      type: function() { 
         return typeof val; 
      } 
   }; 
} 

var b = box(); 
b.type(); // "undefined" 
b.set(98.6); 
b.get(); // 98.6 
b.type(); // "number"
{% endhighlight %}

This example produces an object containing three closures, its set, get, and type properties. Each of these closures shares access to the val variable. The set closure updates the value of val, and subsequently calling get and type sees the results of the update.
