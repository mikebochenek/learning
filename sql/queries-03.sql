
SELECT * FROM test.item;

INSERT INTO `test`.`item` (`id`, `owner`, `donetext`, `donedate`, `createdate`, `deleted`) 
VALUES ( 1, 1, 'created new github project - idone', now(), now(), false );

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
