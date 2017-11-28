# 2 SELECT 语句
## 取得精美包装里的数据
SELECT语句

```
SELECT * FROM my_contacts  -- 星号的意思是全部
WHERE first_name = 'Anne'; -- where 后边是限定条件
```
1.1 单引号的使用:
在单引号字符的前面加上***反斜线***能达到说明的效果。

举个例子：

```
INSERT INTO my_contacts
(location)
VALUES
('Grover\'s Mill');
```
1.2 选取特定列

```
SELECT drink_name, main, second
FROM easy_drinks;
```
1.3 AND 和 OR 的用法

```
SELECT drink_name
FROM drink_info
WHERE 
drink_name >= 'L'
AND 
drink_name <= 'M';
```

```
SELECT drink_name 
FROM easy_drinks
WHERE 
main = 'cherry juice'
OR
second = 'cherry juice';
```
1.4 NULL 的用法
```
SELECT drink_name
FROM drink_info
WHERE
calories IS NULL;
```

1.5 LIKE的用法

```
SELECT *
FROM my_contacts
WHERE location LIKE '%CA';

---------------------------
SELECT *
FROM my_contacts
WHERE location LIKE '_CA';   --占用一个字符的长度

```

1.6  BETWEEN的用法

```
SELECT drink_name 
FROM drink_info
WHERE 
calories BETWEEN 30 AND 60;   -- Equal to 30<= calories <=60
```
1.7 How to use IN (NOT IN)

```
SELECT data_name
FROM black_bool
WHERE
rating IN ('A','B','C','D')
```





















