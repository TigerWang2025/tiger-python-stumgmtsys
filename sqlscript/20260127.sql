/*
SQLyog Ultimate v12.3.1 (64 bit)
MySQL - 8.0.19 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

create table `operator` (
	`operatorid` varchar (96),
	`operatorname` varchar (96),
	`operatorsex` varchar (12),
	`operatorbirthdate` date ,
	`responsibility` varchar (96),
	`operatortel` varchar (96),
	`operatormail` varchar (384),
	`idnumber` varchar (384),
	`createtime` datetime ,
	`updatetime` datetime ,
	`flag` int (11),
	`isdel` varchar (12)
); 
insert into `operator` (`operatorid`, `operatorname`, `operatorsex`, `operatorbirthdate`, `responsibility`, `operatortel`, `operatormail`, `idnumber`, `createtime`, `updatetime`, `flag`, `isdel`) values('GMgR2KCLiFCr3wRPEP20GMygzEoWJKHz','Admin','M','1996-05-27','G','19951023158','test.test@126.com','322100199605275411','2026-01-27 15:15:49','2026-01-27 15:15:49','0','N');
