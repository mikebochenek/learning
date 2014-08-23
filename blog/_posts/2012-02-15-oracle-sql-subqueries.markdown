---
layout: post
title:  "Oracle SQL Subqueries"
date:   2012-02-15 19:23:42
categories: coding
---

A commonly encountered problem to query a min/max per group or some other criteria – can be solved with subqueries

“A subquery is a query within a query. In Oracle, you can create subqueries within your SQL statements. These subqueries can reside in the WHERE clause, the FROM clause, or the SELECT clause.”
[reference 1](http://www.techonthenet.com/oracle/subqueries.php)
[reference 2](http://www.xaprb.com/blog/2006/12/07/how-to-select-the-firstleastmax-row-per-group-in-sql/)

{% highlight sql linenos %}
select id, startdate 
from employee, (SELECT grade, min(startdate) as minentrydate
  from employee
  GROUP BY rank) subquery
where subquery.minentrydate = employee.startdate 
and employee.grade = subquery.grade;
{% endhighlight %}
