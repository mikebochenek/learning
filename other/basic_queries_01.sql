select * from users;
update users set is_admin = true where id = 3;
update users set is_active = true where id = 4;

commit;


select * from groups;
select * from traits;

select owner_uuid from api_clients;