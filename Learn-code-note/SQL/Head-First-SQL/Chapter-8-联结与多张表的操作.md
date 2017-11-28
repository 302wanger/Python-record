### 8.1 复制第一项兴趣并将其存储到 interest1列：

#### code1 和code2将interests中的兴趣分别复制到新的列中

```
code1：
UPDATE my_contacts
SET interest1 = SUBSTRING_INDEX(interests, ',',1); 
# interests为要截取数据的列名，要查找的分隔符,本处为逗号，查找第一个逗号
```
```
 code2:
UPDATE my_contacts
SET interests = SUBSTR(interests, LENGTH(interest1)+2);
```

### 将父表中的数据填入新表
有三种方式
#### 方式1：CREATE TABLE,然后利用SELECT 进行INSERT
```
CREATE TABLE profession
(
	id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	profession VARCHAR(20)
);
INSERT INTO profession(profession)
	SELECT profession FROM my_contacts
	GROUP BY profession
	ORDER BY profession;
```	
#### 方法2：利用SELECT 进行 CREATE TABLE,然后 ALTER 以添加主键
```
CREATE TABLE profession AS
	SELECT profession FROM my_contacts
	GROUP BY profession
	ORDER BY profession;
ALTER TABLE profession
ADD COLUMN id INT NOT NULL AUTO_INCREMENT FIRST,
ADD PRIMARY KEY(id);
```
#### 方法3：CREATE TABLE 的同时设置主键并利用SELECT填入数据
```
CREATE TABLE profession
(
	id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	profession VARCHAR(20)
) AS 
  SELECT profession FROM my_contacts
  GROUP BY profession
  ORDER BY profession;
```


#### 8.2 INNER JOIN:
内连接。任何使用条件结合来自两张表的记录的联接。

#### 8.3 NATRUAL JOIN:
自然连接 不适用on子句的内连接。只有在联接的两张表中有同名列时才能顺利运作。
#### 8.4 EQUIJOIN 与NON-EQUI-JOIN ：
相等联接与不等联接。两者均为内联接的一种。相等联接返回相等的行，不等联接返回不相等的行。
#### 8.5 CROSS JOIN 交叉联接:
返回一张表的每一行与另一张表的每一行所有可能的搭配结果。
(其他常见名称还包括笛卡尔联接与NO JOIN.)
#### 8.6 COMMA JOIN： 
与CROSS JOIN 相同，只不过以逗号取代关键字CROSS JOIN.