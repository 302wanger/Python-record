### 10.1 外联接、自联接与联合

#### 自联接
***使用一个表两次***

```
SELECT c1.name, c2.name AS boss
FROM clown_info c1
INNER JOIN clown_info c2
ON c1.boss_id = c2.id;
```

#### 联合 UNION,将多个查询结果合并到一张表中
```
SELECT title FROM job_current
UNION
SELECT title FROM job_desired
UNION
SELECT title FROM job_listings;
```
### SQL联合规则
	1.每个SELECT 语句中列的数量必须一致。不可以由第一条语句选取了两列，其他语句却选取一列
	2.每个SELECT语句包含的表达式与统计函数也必须相同。
	3.SELECT语句顺序不重要，不会改变结果。
	4.SQL默认会清除联合的结果中的重复值。
	5.列的数据类型必须相同或可以相互转换。
	6. 如果处于某些原因需查看重复数据，可以使用UNION ALL 运算符。
	7. 这个运算符返回每个相符的数据，而不只是没有重复的数据。

### 10.2 从联合创建表
CREATE TABLE my_union AS
SELECT title FROM job_current
UNION
SELECT title FROM job_desired
UNION
SELECT title FROM job_listings;

####  INTERSECT(交集)与EXCEPT(差集)同UNION的用法基本相同

#### 交集
```
SELECT title FROM job_current
INTERSECT
SELECT title FROM job_desired;
```
#### 差集
```
SELECT title FROM job_current
EXCEPT
SELECT title FROM job_desired;
```
#### 把子查询转换为联接
#### 例子1.子查询列子
```
SELECT mc.first_name, mc.last_name, mc.phone, jc.title
FROM job_current AS jc 
NATRUAL JOIN my_contacts AS mc
WHERE jc.title IN (SELECT title
				   FROM job_listings);
```
#### 例子1.转换为联接
```
SELECT mc.first_name, mc.last_name, mc.phone, jc.title
FROM job_current AS jc
NATRUAL JOIN my_contacts AS mc
INNER JOIN job_listings jl ON jc.title = jl.title;
```
#### 例子2.子查询
```
SELECT title
FROM job_listings
WHERE salary = (SELECT MAX(salary)
				FROM job_listings);
```				
				
#### 例子2.联接
#### 使用联接比子查询更方便
```
SELECT title 
FROM job_listings
ORDER BY salary DESC
LIMIT 1;
```
# 子查询和联接可以互相转换，视情况而定看哪个比较好用就用哪个