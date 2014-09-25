

INSERT INTO `test`.`item` (`owner`, `donetext`, `donedate`, `createdate`, `doneDay`) 
VALUES ( 1, 'resume working on idone - two small java commits', now(), now(), 2014093 );

SELECT * FROM test.item;

SELECT donetext, doneday, id FROM test.item order by id;


update test.item set doneday = 2014064 where id in (5,6,7);
update test.item set doneday = 2014063 where id in (1,2,3,4);



select * from test.user;
insert into test.user 
-- delete from test.user where id = 523;
 commit;

SELECT * FROM test.item;

INSERT INTO `test`.`user`
(`username`,`password`,`email`)
VALUES
('test','test','mike@test.com');


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



SELECT count(*), municipality, year 
FROM test.incomes 
where municipality = 'Zollikon'
group by municipality, year;

SELECT income_group, tax_rate, num_taxpayers
FROM test.incomes 
where municipality = 'Zollikon' and year = 2010
order by income_group asc;

SELECT income_group, sum(num_taxpayers)
FROM test.incomes 
where municipality like /*'Zollikon'*/ 'Z%rich' and year = 2010
group by income_group
order by income_group asc;

select municipality, count(*) as cc
FROM test.incomes 
WHERE municipality <> 'MUNICIPALITY'
group by municipality
order by cc desc;

SELECT sum(num_taxpayers)
FROM test.incomes 
where municipality like 'Zollikon' and year = 2010
