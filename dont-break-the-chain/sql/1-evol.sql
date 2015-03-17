# --- First database schema

# --- !Ups


CREATE TABLE done (
  id int(11) NOT NULL  primary key,
  owner int(11) DEFAULT NULL,
  donetext text,
  donedate datetime DEFAULT NULL,
  createdate timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  deleted tinyint(1) DEFAULT NULL,
  category bigint(20) NOT NULL,
  doneDay bigint(20) NOT NULL
) ;

CREATE TABLE user (
  id bigint(20) NOT NULL  primary key,
  createdate datetime DEFAULT NULL,
  lastlogindate datetime DEFAULT NULL,
  deleted bit(1) DEFAULT NULL,
  password varchar(255) DEFAULT NULL,
  settings longtext,
  username varchar(255) DEFAULT NULL,
  email varchar(255) DEFAULT NULL,
  type varchar(255) DEFAULT NULL,
  openidtoken varchar(255) DEFAULT NULL
) ;

create sequence done_seq start with 1000;

INSERT INTO user (id, password, username, email) 
VALUES (1, 'test', 'mike', 'mike@test.com' );

# --- !Downs

drop table if exists done;
drop sequence if exists done_seq;
drop table if exists user;
