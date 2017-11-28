# 数据和表
## 保存所有东西的地方
列是存储在表中的一块数据。

行是一组能够描述某个事物的列的集合。

行和列构成了表。

**1 创建数据库**

1.1 创建一个名为gregs_list的数据库

```
CREATE DATABASE gregs_list;
```
1.2 使用刚刚创建的数据库

```
USE gregs_list;
```
1.3 设定表中列和数据类型

常见的数据类型有：**CHAR, VARCHAR, BLOB, INT, DEC, DATE, DATETIME**

```
CREATE TABLE doughnut_list
{
	doughnut_type VARCHAR(10),
	doughnut_name VARCHAR(6),
	last_name VARCHAR(20),
	first_name VARCHAR(20),
	email VARCHAR(20),
	location VARCHAR(40)
};
```
1.4 查看表结构

```
DESC doughnut_list;
```
1.5 删除表

```
DROP TABLE doughnut_list;
```
1.6 插入数据
插入的数据必须和列中的顺序一致
```
INSERT INTO doughnut_list
VALUES
(1,2,3,4,5,5,6,7,7,)
```

1.7 控制NULL
在创建表时就要限制条件中NUT NULL,
用DEFAULT设定默认值填补空白

```
CREATE TABLE my_contacts
(
	last_name VARCHAR(30) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	cost DEC(3,2) NOT NULL DEFAULT 1.00
);
```
















