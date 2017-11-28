 
### 6.1 CASE 
### 创建movie_table表
```
CREATE TABLE movie_table
(
	movie_id INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(20),
	rating CHAR(2),
	drama CHAR(1),
	comedy CHAR(1),
	action CHAR(1),
	gore CHAR(1),
	scifi CHAR(1),
	for_kids CHAR(1),
	cartoon CHAR(1),
	purchased VARCHAR(20),
	PRIMARY KEY(movie_id)
);
```
#### 插入数据
```
INSERT INTO movie_table
VALUES 
(1,'Monsters,INC','G','F','T','F','F','F','T','T','3-6-2002'),
(2,'THE Godfather','G','F','T','F','F','F','T','T','3-6-2002'),
(3,'Gone','G','F','T','F','F','F','T','T','3-6-2002'),
(4,'American Pie','G','F','T','F','F','F','T','T','3-6-2002'),
(5,'Nightmare','G','F','T','F','F','F','T','T','3-6-2002'),
(6,'Cosablanca','G','F','T','F','F','F','T','T','3-6-2002');
```

#### 改变列名
```
ALTER TABLE movie_table
CHANGE purchased category VARCHAR(20);
```
#### 更新数据
```
UPDATE movie_table
SET category =
CASE
	WHEN drama = 'T' THEN 'drama'
	WHEN comedy = 'T' THEN 'comedy'
	WHEN action = 'T' THEN 'action'
	WHEN gore = 'F' THEN 'horror'
	WHEN scifi = 'T' THEN 'scifi'
	WHEN for_kids = 'T' THEN 'family'
	WHEN cartoon = 'T' AND rating='G' THEN 'family'
	ELSE 'misc'
END;
```
### 6.2 ORDER BY
按照字母顺序排列查询结果。

```
SELECT title, category
FROM movie_table
WHERE
category = 'family'
ORDER BY title;
```

```
ORDER BY title DESC;  --反转排序
ORDER BY title;       --正常排序
```
### 6.3  SUM()函数

#### 创建一个表，测试sum
```
CREATE TABLE cookie_sales
(
	ID INT NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(50),
	sales INT,
	sale_date DATE,
	PRIMARY KEY(ID)
);
```
```
INSERT INTO cookie_sales
VALUES
(2,'Paris',22.20,'2002-2-2'),
(3,'Britney',2.20,'2002-2-2'),
(4,'Nicole',22.20,'2002-2-2'),
(5,'Lindsay',2.20,'2002-2-2'),
(6,'Paris',22.20,'2002-2-2'),
(7,'Britney',22.20,'2002-2-2'),
(8,'Nicole',2.20,'2002-2-2'),
(9,'Lindsay',2220,'2002-2-2'),
(10,'Paris',22.20,'2002-2-2'),
(11,'Britney',2.20,'2002-2-2'),
(12,'Nicole',22.20,'2002-2-2'),
(13,'Lindsay',22.20,'2002-2-2'),
(14,'Paris',220,'2002-2-2'),
(15,'Britney',2.20,'2002-2-2'),
(16,'Nicole',2.20,'2002-2-2');
```
#### 查询各个人的总和
```
SELECT first_name, SUM(sales)
FROM cookie_sales
GROUP BY first_name
ORDER BY SUM(sales) DESC;
```
#### 各个人的平均值
```
SELECT first_name, AVG(sales)
FROM cookie_sales
GROUP BY first_name;
```
#### 每人的最大销量
```
SELECT first_name, MAX(sales)
FROM cookie_sales
GROUP BY first_name;
```
#### 每人的最小销量
```
SELECT first_name, Min(sales)
FROM cookie_sales
GROUP BY first_name;
```
#### 每人的销售天数
```
SELECT first_name,COUNT(sale_date)
FROM cookie_sales
GROUP BY first_name;
```
####查找前两名
```
SELECT first_name, SUM(sales)
FROM cookie_sales
GROUP BY first_name
ORDER BY SUM(sales) DESC
LIMIT 2;
```
#### 直接查找第3名
 LIMIT 1,1 第一个1确定查询结果的起始处（sql以0开始），第二个1表示返回查询结果数量（这里是1个）

```
SELECT first_name, SUM(sales)
FROM cookie_sales
GROUP BY first_name
ORDER BY SUM(sales) DESC
LIMIT 1,1;
```

### 6.4 选出与众不同的值
***DISTINCT***

```
SELECT DISTINCE sale_date
FROM cookie_sales
ORDER BY sale_date;
```

### 6.5 LIMIT查询结果的限制
***只显示前两名***

```
SELECT first_name, SUM(sales)
FROM cookies_sales
GROUP BY first_name
ORDER BY SUM(sales) DESC
LIMIT 2;
```

***只显示第二名***
	
	LIMIT 0,4
	第一个 

```
SELECT first_name, SUM(sales)
FROM cookies_sales
GROUP BY first_name
ORDER BY SUM(sales) DESC
LIMIT 1，1;
```





