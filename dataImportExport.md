数据的导入和导出
===
## 数据库的备份
```mysql
	mysqldump -u root -p 需要备份的数据库名 > 存储位置及格式
\e.g.
	mysqldump -u root -p smile > /usr/SA/smile.sql
```
## 数据库的恢复
```mysql
	mysql -u root -p 需要恢复到的数据库名(没有的话需自己创建) > 存储位置及格式
	\e.g.
	mysql -u root -p smile > /usr/SA/smile.sql
```
## 数据库中表的导出
### 查看数据库存放路径
```mysql
	mysql> show variables like 'secure_file_priv';
```
### 导出数据到系统指定的文件夹中
```mysql
	select ... from 表名
	into outfile '/var/lib/mysql-files/文件名'
	fields terminated by '分隔符(,)'
	lines terminated by '分隔符(\n)';
```
## 数据库中表的导入
* 数据导入前需要创建对应的数据表
```mysql
	1. 创建数据表
		create table 表名(
			字段名 字段类型,
			字段名 字段类型
		);
	2. 执行数据导入语句
		load data infile '/var/lib/mysql-files/文件名'
		into table 表名
		fields terminated by ','
		lines terminated by '\n';
```