drop database example;
create database example
default character set utf8
default collate utf8_general_ci;

use example;

create table alien (
	id int not null auto_increment,
	name varchar(30) not null,
	birthday date,
	gender enum('M','F'),
	weight decimal(5,2) default '00.0',
	height decimal(3,2) default '0.00',
	nacionality varchar(20) default 'Brazil',
	primary key (id)
) default charset = utf8;
