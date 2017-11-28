# 查询中的查询

### 9.1 子查询示范：

```
SELECT last_name, first_name
FROM my_contacts
WHERE zip_code = (
					SELECT zip_code 
					FROM zip_code
					WHERE city = 'Memphis' AND state = 'TN'
);
#
SELECT mc.first_name, mc.last_name,
(SELECT state
FROM zip_code
WHERE mc.zip_code = zip_code
) AS state
FROM my_contacts mc;
# 
SELECT mc.first_name, mc.last_name, jc.salary 
FROM
my_contacts AS mc 
NATRUAL JOIN job_current AS jc
WHERE
jc.salary > ( SELECT jc.salary
			  FROM my_contacts mc
			  NATRUAL JOIN job_current jc
			  WHERE email = 'www.good.com'
);
```
#### 几个内查询的例子
#### 1:列出薪资等于job_listings 表中最高薪资的职务名称
```
SELECT title FROM job_listings
WHERE salary = (SELECT MAX(salary)
				FROM job_listings);
```
#### 2:列出薪资高于平均薪资者的姓名
```
SELECT mc.first_name, mc.last_name
FROM my_contacts mc
NATRUAL JOIN job_current jc
WHERE jc.salary > (SELECT AVG(salary) FROM job_current);
```
#### 3:寻找网页设计员，但只列出其邮政编码与任何一个网站设计职缺的邮政编码相同的设计员
```
SELECT mc.first_name, mc.last_name, mc.phone
FROM my_contacts mc
NATRUAL JOIN job_current jc
WHERE jc.title = 'web design' 
AND mc.zip_code in (SELECT zip
					FROM job_listings
					WHERE title='web design');
```
#### 4.列出每个邮政编码涵盖的地区中当前薪资最高的人
```
SELECT last_name, first_name
FROM my_contacts			
WHERE zip_code 	IN (SELECT mc.zip_code
					FROM my_contacts mc
					NATRUAL JOIN job_current jc 
					WHERE jc.salary = (SELECT MAX(salary)
									   FROM job_current));
									   
```


