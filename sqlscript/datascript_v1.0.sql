/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2026/1/27 10:39:57                           */
/*==============================================================*/


drop table if exists class;

drop table if exists grade;

drop table if exists operator;

drop table if exists operatorlog;

drop table if exists operatorpermission;

drop table if exists permission;

drop table if exists student;

/*==============================================================*/
/* Table: class                                                 */
/*==============================================================*/
create table class
(
   classno              varchar(40) not null,
   classname            varchar(40),
   year                 year(4),
   flag                 int comment '0：正常，1：已删除',
   createtime           datetime,
   updatetime           datetime,
   primary key (classno)
);

/*==============================================================*/
/* Table: grade                                                 */
/*==============================================================*/
create table grade
(
   id                   varchar(32) not null,
   stuno                varchar(20),
   classno              varchar(40),
   operatorid           varchar(32),
   chinese              decimal(5,2),
   mathematics          decimal(5,2),
   english              decimal(5,2),
   physics              decimal(5,2),
   chemistry            decimal(5,2),
   biology              decimal(5,2),
   politics             decimal(5,2),
   history              decimal(5,2),
   geography            decimal(5,2),
   flag                 int comment '0：正常，1：已删除',
   createtime           datetime,
   updatetime           datetime,
   primary key (id)
);

/*==============================================================*/
/* Table: operator                                              */
/*==============================================================*/
create table operator
(
   operatorid           varchar(32) not null,
   operatorname         varchar(32),
   operatorsex          varchar(4),
   operatorage          int comment '只有：男、女',
   responsibility       varchar(32),
   operatortel          varchar(32),
   operatormail         varchar(128),
   idnumber             varchar(128),
   createtime           datetime,
   updatetime           datetime,
   flag                 int comment '0：正常，1：已删除',
   primary key (operatorid)
);

/*==============================================================*/
/* Table: operatorlog                                           */
/*==============================================================*/
create table operatorlog
(
   operatorid           varchar(32),
   logid                varchar(32) not null,
   operatortype         varchar(16),
   opercontent          text,
   operatortime         datetime,
   primary key (logid)
);

/*==============================================================*/
/* Table: operatorpermission                                    */
/*==============================================================*/
create table operatorpermission
(
   operatorid           varchar(32),
   permissionid         varchar(32)
);

/*==============================================================*/
/* Table: permission                                            */
/*==============================================================*/
create table permission
(
   permissionid         varchar(32) not null,
   permissionname       varchar(32),
   createtime           datetime,
   updatetime           datetime,
   flag                 int comment '0：正常，1：已删除',
   primary key (permissionid)
);

/*==============================================================*/
/* Table: student                                               */
/*==============================================================*/
create table student
(
   id                   varchar(32) not null,
   stuno                varchar(20) not null,
   name                 varchar(20),
   sex                  varchar(4) comment '只有：男、女',
   age                  int,
   height               varchar(16),
   weight               varchar(16),
   telephone            varchar(32),
   flag                 int comment '0：正常，1：已删除',
   createtime           datetime,
   updatetime           datetime,
   primary key (id, stuno)
);

alter table grade add constraint FK_Reference_1 foreign key (classno)
      references class (classno) on delete restrict on update restrict;

alter table grade add constraint FK_Reference_2 foreign key (id, stuno)
      references student (id, stuno) on delete restrict on update restrict;

alter table grade add constraint FK_Reference_3 foreign key (operatorid)
      references operator (operatorid) on delete restrict on update restrict;

alter table operatorlog add constraint FK_Reference_5 foreign key (operatorid)
      references operator (operatorid) on delete restrict on update restrict;

alter table operatorpermission add constraint FK_Reference_6 foreign key (operatorid)
      references operator (operatorid) on delete restrict on update restrict;

alter table operatorpermission add constraint FK_Reference_7 foreign key (permissionid)
      references permission (permissionid) on delete restrict on update restrict;

