索引
===
### 索引简述
* 定义
	+ 对数据库表的一列或多列的值进行排序的一种结构(Btree方式)
	+ B树的特点：
		+ 1. 全部节点均包含：索引 + 数据 
		+ 2. 范围查询：从根节点比那里至指定数据
	+ B+树的特点：
		+ 1. 非叶子节点只保存索引{树宽度优于B树，从而降低了磁盘IO}
		+ 2. 叶子的节点保存所有索引和数据
		+ 3. 叶子节点之间相互连接，形成链表结构
* 优点
	+ 加快数据检索速度distinct语句
* 缺点
	+ 占用物理存储空间(/var/lib/mysql)
	+ 当对表中数据更新时，索引需要动态维护，降低数据维护速度
### 索引分类
* 查看索引
```mysql
1. desc 表名;  --> KEY 标志为：MUL，UNI
2. show index from 表名\G;
```

#### 主键(primary) and 自增(auto_increment)
* 使用规则
```mysql
1、只能有一个主键字段
2、所带约束 ：不允许重复,且不能为NULL
3、KEY标志(primary) ：PRI
4、通常设置记录编号字段id,能唯一锁定一条记录
```
* 创建表增加主键和自增
```mysql
create table student(
id int primary key auto_increment,
name varchar(20)
)charset=utf8,auto_increment=10000;  #设置自增长起始值
```
* 已有表增加主键suoy和自增
```mysql
1. 已有表增加主键
	alter table 表名 add primary key(id);
2. 已有表增加自增属性
	alter table 表名 modify id int auto_increment;
3. 已有表重新指定自增初始值
	alter table 表名 auto_increment=1000;  # 设置自增初始值
```
* 删除主键和自增
```mysql
1. 删除自增属性
	alter table 表名 modify id int;
2. 删除主键索引
	alter table 表名 drop primary key;
```

#### 普通(index) and 唯一(unique)
* 使用规则
```mysql#### w

1. 可设置对个字段
2. 普通索引：字段值无约束，KET标志为MUL
3. 唯一索引(unique)：字段值不允许重复，但可以为NULL，KEY标志为UNI
4. 那些字段创建索引：经常用来查询的字段，where条件判断语句，order by排序字段
```
* 创建表增加普通和唯一
```mysql
create table 表名(
字段名 数据类型，
字段名 数据类型，
index(字段名),
index(字段名),
unique(字段名biaoming)
)charset=utf8;
```
* 已有表中创建普通和唯一
```mysql
create [unique] index 索引名 on 表名 (字段名);
```
* 删除
```mysql
drop index 索引名 on 表名;  # 只能一个一个删
```
biaoming
#### 外键(foreign)
* 定义
	让当前表字段的值在另一个表的范#### 嵌套查询(子查询)
#### 多表查询围内选择
* 语法
```mysql
	foreign key 参考字段名
	references 主表(被参考字段名)
	on delete 级联动作
	on update 级联动作
```
* 使用规则
```mysql
	1. 主表，从表字段数据类型要一致
	2. 主表被参考字biaoming段：KEY的一种，一般为主键
```
***e.g.***
表1.
```mysql
id   姓名     班级     缴费金额
1   唐伯虎   AID1905     300
2   秋	  香   AID1905     300
create table master(
	id int primary key,
    name varchar(30),
    class char(10),
    money decimal(biaoming6,2)
)charset=utf8;
```
表2.
```mysql
stu_id   姓名   缴费金额
  1     唐伯虎    300
  2     秋	  香    300
  create table stuinfo(
      stu_id int,
      name varchar(30),
      money decimal(6,2)
    );
```
* 级联动作
```mysqlbiaoming
	cascade
		​数据级联删除、更新(参考字段)
	restrict
		​从表有相关联记录,不允许主表操作
	set null
		​主表删除、更新,从表相关联记录字段值为NULL
```
* 增加主键
```mysql
	create table stuinfo(
		stu_id int,
		name varchar(30),
		money decimal(6,2),
		foreign key (stu_id)
		references master(id)
		on delete cascade
		on update cabiaomingscade
	)charset=utf8;
```
* 已有表增加外键
```mysql
	alter table 表名 add foreign key(参考字段) references 主表(被参考字段) on delete 级联动作 on update 级联动作 
```
* 删除外键
```mysql
	alter table 表名 drop foreign key 外建名;   # 外键名：show create table 表名;
```





