---
layout: post
title:  "Increasing weblogic ejb transaction timeout"
date:   2011-09-02 14:13:54
categories: coding
---

While doing remote debugging with eclipse, I tend to run into annoying EJB transaction timeouts quite a lot.  Is there an easy way to increase this timeout in weblogic?  I am using the weblogic that came with JAP 5.0 and I am seeing exceptions like this:
weblogic.transaction.internal.TimedOutException: Transaction timed out after 30 seconds

The weblogic documentation suggests that you could individually increase the timeout per EJB, but that doesn’t help since I have lots of them and the ejb-jar.xml is generated.  In the jboss/tomcat world, I seem to remember that there was one setting that would override this.

The <transaction-descriptor> element of weblogic-ejb-jar.xml allows the transaction timeout to be customized for an EJB’s container-managed transactions.

{%highlight  xml linenos=table %}
<weblogic-enterprise-bean>
  <ejb-name>MyEJBImpl</ejb-name>
  <transaction-descriptor>
  <trans-timeout-seconds>100</trans-timeout-seconds>
  </transaction-descriptor>
</weblogic-enterpise-bean>
{%endhighlight%}

This setting applies only to new transactions started by container when the EJB is called. It has no effect for calls to the EJB that use an existing transaction, so the EJB’s @TransactionAttribute must either be REQUIRES_NEW or REQUIRED (the default value), and in the latter case the there must not be an existing transaction when the call to the EJB is made. You may need to use the <transaction-descriptor> element to increase the transaction timeout for an EJB that performs a lengthy database operation, or for a message-driven bean that uses transaction batching. It is better to relax the transaction timeout for specific EJBs than to increase the global default for the whole WebLogic domain.

