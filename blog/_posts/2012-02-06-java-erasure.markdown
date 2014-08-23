---
layout: post
title:  "Java Erasure"
date:   2012-02-06 21:01:32
categories: coding
---

“When a generic type is instantiated, the compiler translates those types by a technique called type erasure — a process where the compiler removes all information related to type parameters and type arguments within a class or method. Type erasure enables Java applications that use generics to maintain binary compatibility with Java libraries and applications that were created before generics.”

“The Java compiler employs type erasure when objects are instantiated except when objects are instantiated from anonymous classes.” [reference 1](http://www.jquantlib.org/index.php/Using_TypeTokens_to_retrieve_generic_parameters)

Motivated by HX question on using reflection [reference 2](http://help.csintra.net/questions/20621/can-we-use-reflection-on-local-variables-in-java/20631#20631)

{% highlight java linenos %}
public class TryReflection {
   public static void main(String[] args) {
      List stringList = new ArrayList() {};
      List bdList = new ArrayList() {};
      List intList = new ArrayList() {};
      List pList = new ArrayList() {};
      System.out.println(getName(stringList)); //output should be String
      System.out.println(getName(bdList)); //output should be BigDecimal
      System.out.println(getName(intList)); //output should be Integer
      System.out.println(getName(pList)); //output should be Properties}
   }
   public static String getName(List list2) {
      return list2.getClass().getGenericSuperclass().toString();
   }
}
{% endhighlight %}
