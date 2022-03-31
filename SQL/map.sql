| map to learning : SQLdata definition language
+-----------------+
#last update 2022/03/24

#DDL - data definition language
#DML - data manipulation language

#types:
##
#num(
#	int : [TinyInt, SmallInt, Int, MediumInt, BigInt]
#	real : [Decimal, Float, Double, Real]
#	logic : [Bit, Boolean]
#	);
##
#date/time( : [Date, DateTime, TimeStamp, Time, Year])
##
#literal(
#	character : [Char, Varchar]
#	text : [TinyText, Text, MediumText, LongText]
#	binary : [TinyBlob, Blob, MediumBlob, LongBlob]
#	collection : [enum, set]
##

drop database example;                   -> use to delete database

use example;                             -> use for manipulate database

create database example                  -> to create a database
default character set uft8               -> setting utf8 in database
default collate utf8_general_ci;

create table alien (                     -> to create a table in database
	id int not null auto_increment,  -> id
	name varchar(30) not null,       -> to add any name,'not null' cannot be empty
	birthday date,
	gender enum('M','F'),            -> to add only 'M' or 'F'
	weight decimal(5,2) default '0.0',
	height decimal(3,2) default '0.0',
	nationality varchar(20) default 'Brazil',
	primary key (id)                 -> key using id
);default charset = utf8                 -> to set utf8 charset

insert into alien                        -> to add records in db, next line can be skipped if values are completed
(id, name, birthday, gender, weight, height, nacionality)
values                                   -> to set records for add
(default,'Travis Scott','1992-04-30','M',default,default,'EUA'),
(default,'Eminem','1972-10-17','M',default,default,'EUA'),
(default,'Billie Eilish','2001-12-18','F',default,default,'EUA'),
(default,'Yunk Vino','1997-06-07','M',default,default,'BR'),
(default,'30PRAUM','2014-00-00','M',default,default,'BR'),
(default,'Labirinth','1989-01-04','M',default,default,'UK'),
(default,'Skeler','2017-04-21','M',default,default,'IDK'),
('666','Ghostemane','1991-04-15','M',default,default,'EUA');

#if u wanna view this change
select * from alien                      -> to view all in table alien
show tables                              -> to view all tables in db

