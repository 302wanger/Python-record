### 11.1 检查约束：加入CHECK
```
CREATE TABLE pigg_bank
(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	coin CHAR(1) CHECK (coin IN ('P','N','D','Q')) # 用CHECK约束来限定插入coin的值。
);												   # 如果插入的值无法通过CHECK条件，则出现错误信息。
```

#### 例子
```
CREATE TABLE mystery_table
(
	column1 INT(4) CHECK (column1 > 2000),                    # 输入的值必须大于2000
	column2 CHAR(1) CHECK (column2 NOT IN ('x', 'y', 'z')),   # 只要不是字符x,y,z，都可以
	column3 VARCHAR(3) CHECK ('A' = SUBSTRING(column_3,1,1)), # 字符串的第一个字符必须为 A
	column4 VARCHAR(3) CHECK ('A' = SUBSTRING(column_4,1,1) AND '9' = SUBSTRING(column_4,2,1))
	# 字符串的第一个字符必须为 A，第二字符必须是9
);
```

### 11.2 视图：将一些重复的查询转换为视图，方便查询
#### 创建两个视图
```
CREATE VIEW web_designers AS
SELECT mc.first_name, mc.last_name, mc.phone, mc.email
FROM my_contacts mc
NATRUAL JOIN joc_desired jd
WHERE jd.title = 'Web Designer';
#
CREATE VIEW tech_writer_jobs AS
SELECT title.salary, description, zip
FROM job_listings
WHERE title = 'Technical Writer';
```

#### 调用视图
```
SELECT * FROM web_designers;
SELECT * FROM tech_writer_jobs;
```
#### 删除视图
```
DROP VIEW web_designers;
```
### 11.3 事务：一群可完成一组工作的SQL语句。
书中以ATM机的两个例子很好的诠释了事务的作用

### 经典ACID检测
	# 1.原子性：事务里的每一个步骤都必须完成，否则只能都不完成。不能只执行部分事务。
	# 2.一致性：事务完成后应该维持数据库的一致性。在完成两组金钱事务后，钱的数量应该符合账户余额的情况
	
	在第一个案例中，钱应该转入存款账户；在第二个案例中，前应该换成现金，不应该有钱消失的情况
	# 3.隔离性：表示每次事务都会看到具有一致性的数据库，无论其他事务有什么行动。
	# 4.持久性：事务完成后，数据库需要正确的存储数据并免收断电或其他威胁的伤害。


# 有三种SQL事务工具可以保障账户的安全。


	START TRANSACTION;    # 持续追踪后续所有SQL语句，直到输入COMMIT 或ROLLBACK为止
	COMMIT                # 等到我们满意后再提交所有代码造成的改变。
	ROLLBACK              # 如果改变结果不太对，就回滚，回到事务开始前的状态