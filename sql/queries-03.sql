
select * from test.user;
delete from test.usre where id = 523;
 commit;

SELECT * FROM test.item;

INSERT INTO `test`.`item` (`id`, `owner`, `donetext`, `donedate`, `createdate`, `deleted`) 
VALUES ( 1, 1, 'created new github project - idone', now(), now(), false );

INSERT INTO `test`.`item` (`id`, `owner`, `donetext`, `donedate`, `createdate`, `deleted`) 
VALUES ( 2, 1, 'finally filled in bonviva gold application', now(), now(), false );

INSERT INTO `test`.`item` (`id`, `owner`, `donetext`, `donedate`, `createdate`, `deleted`) 
VALUES ( 3, 1, 'idone basic project scaffolding', now(), now(), false );

INSERT INTO `test`.`item` (`id`, `owner`, `donetext`, `donedate`, `createdate`, `deleted`) 
VALUES ( 4, 1, 'ebanking and bonviva balance', now(), now(), false );

INSERT INTO `test`.`item` (`id`, `owner`, `donetext`, `donedate`, `createdate`, `deleted`) 
VALUES ( 5, 1, '54. Edge of Dark Water by Joe Lansdale [library]', now(), now(), false );

INSERT INTO `test`.`item` (`id`, `owner`, `donetext`, `donedate`, `createdate`, `deleted`) 
VALUES ( 6, 1, 'dealextreme order headphones, arduino, etc.', now(), now(), false );

INSERT INTO `test`.`item` (`id`, `owner`, `donetext`, `donedate`, `createdate`, `deleted`) 
VALUES ( 7, 1, 'mikey320b account on codewars.com and first two catas completed', now(), now(), false );

/*
use test;

delimiter $$

CREATE TABLE `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owner` int(11) DEFAULT NULL,
  `donetext` text DEFAULT NULL,
  `donedate` DATETIME DEFAULT NULL,
  `createdate` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `deleted` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=latin1$$
*/


drop table  `test.user`

delimiter $$

CREATE TABLE `user` (
  `id` bigint(20) NOT NULL,
  `createdate` datetime DEFAULT NULL,
  `deleted` bit(1) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `settings` longtext,
  `username` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `openidtoken` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1$$
