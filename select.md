查询
===
## MySQL普通查询(优先级)
```mysql
3. select ... 聚合函数 from 表名
1. where ... 
2. group by ...
4. having...
5. order by..
6. limit. 
```
### 一．聚合函数
| 方法 | 功能 |
|---|---|
| avg(字段名) | 该字段的平均值 |
| max(字段名) | 该字段的最大值 |
| min(字段名)| 该字段的最小值 |
| sum(字段名)| 该字段所有记录的和 |
| count(字段名)| 统计该字段记录的个数 |

### 二．group by(分组查询)
* group by 后字段名必须未select 后的字段
* 查询字段和group by后字段不一致，则必须对该字段进行聚合处理(聚合处理)

### 三．having (对分组聚合后的结果进行筛选)
* having语句通常与group by联合使用
* having语句存在弥补了where关键字不能与聚合函数联合使用的不足，where只能操作表中实际存在的字段，having操作的是聚合函数生成的显示列

### 四．distinct (不显示重复值)
* distinct 和 from 之间所有字段都相同才会去重
* distinct 不能对任何字段做聚合处理

### 五．查询表记录时做数学运算
* + - * / % ** ...
* 只会在查询的时候显示，不会实际跟新到数据库中，除非用update

## MySQL高级查询
### 一．嵌套查询(子查询)
* 定义
	把内层的查询结果作为外层的查询条件
* 语法格式
```mysql
	select ... from 表名 where 条件 (select ...);
```
* 示例
```mysql
1、把攻击值小于平均攻击值的英雄名字和攻击值显示出来
  select name,attack from sanguo where attack < (select avg(attack) from sanguo);
 2、找出每个国家攻击力最高的英雄的名字和攻击值(子查询)
  select name, attack from sanguo where (country, attack) in (select country,max(attack) from sanguo group by country);
```

### 二．多表查询
* 笛卡尔积
```mysql
	select 字段名列表 from 表名列表;
\e.g.
	select tt1.name tt2.name from tt1, tt2;
```
* 多表查询
```mysql
	select 字段名列表 from 表名列表 where 条件;
\e.g.
	select tt1.name tt2.name from 表名列表 where tt1.id=1;
```

### 三．连接查询
* 内连接(结果同多表查询，显示匹配到的记录)
```mysql
	select 字段名 from 表1 join 表2 on 表1表2相等条件 join 表3 on 表2表3相等条件
\e.g.
	select * from province join city pid=cp_id join county on cid=copid;
```
* 左外连接
```mysql
	select 字段名 from 表1 left join 表2 on 表1表2相等条件 left join 表3 on 表2表3相等条件
\e.g.
	select * from province left join city on pid=cp_id left join county on cid=copid;
```
* 右外连接
```mysql
	select 字段名 from 表1 right join 表2 on 表1表2相等条件 right join 表3 on 表2表3相等条件
\e.g.
	select * from province left join city on pid=cp_id left join county on cid=copid;
```