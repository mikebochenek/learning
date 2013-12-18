-- http://stackoverflow.com/questions/1043096/how-to-list-active-open-connections-in-oracle

select
       substr(a.spid,1,9) pid,
       substr(b.sid,1,5) sid,
       substr(b.serial#,1,5) ser#,
       substr(b.machine,1,6) box,
       substr(b.username,1,10) username,
--       b.server,
       substr(b.osuser,1,8) os_user,
       substr(b.program,1,30) program
from v$session b, v$process a
where
b.paddr = a.addr
and type='USER'
order by spid; 


SELECT username FROM v$session 
WHERE username IS NOT NULL 
ORDER BY username ASC;


-- total count sorted by total count..
select b.machine, b.username, count(*) as cnt
from v$session b, v$process a
where b.paddr = a.addr and type='USER'
group by b.machine, b.username
order by cnt desc; 

-- total count ordered by machine
select b.machine, b.username, count(*) as cnt
from v$session b, v$process a
where b.paddr = a.addr and type='USER'
group by b.machine, b.username
order by machine; 

-- total count of connections 
select count(*) as cnt
from v$session b, v$process a
where b.paddr = a.addr and type='USER';