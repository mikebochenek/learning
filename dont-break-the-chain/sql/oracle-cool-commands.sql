
-- the below seem like good directives to use in general...
WHENEVER OSERROR EXIT 2
WHENEVER SQLERROR EXIT SQL.SQLCODE
set serveroutput ON
set heading off
set echo off
set feedback off


set define off
-- to escape amersand etc. (&)


select '====> start script: ' || to_char(sysdate,'yyyy.mm.dd hh24:mi:ss') from dual;

select 1/0 from dual where upper(sys_context( 'userenv', 'current_schema' )) <> 'DAK';
-- Error report:
-- SQL Error: ORA-01476: divisor is equal to zero


select a.spid, b.sid, b.machine, b.username, b.osuser, b.program
from v$session b, v$process a
where b.paddr = a.addr and b.username = 'AUG'
and type='USER'
order by spid; 

