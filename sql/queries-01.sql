select result,count(*) from test.access group by result order by result;

select request, received from test.access where result = 200 order by received desc;

select count(*) as c, request from test.access where result = 200 group by request order by c desc;

