# 保护你的资产

### 12.1 使用GRANT语句可以控制用户对表和列可执行的操作。

```
GRANT SELECT On 　　　　# 某个用户被授予SELECT权限
clown_info              # 该权限使用于本处指定的表。
TO elsie;            # 获得权限的用户名称是 elsie。
```
#### 每次授予权限都要写一段GRANT语句。
```
GRANT SELECT ON activities TO elsie;
GRANT SELECT ON location TO elsie;
GRANT SELECT ON info_activities TO elsie;
GRANT SELECT ON info_location TO elsis;
```
### 例子
```
GRANT INSERT ON magic_animals TO doc;  # 授予Doc插入内容至magic_animals表的权限
GRANT DELETE ON chores TO happy, sleep; # 授予Happy与sleep删除(delete)chores 表内容的权限
GRANT DELETE ON chores TO happy, sleep WITH GRANT OPTION; # 授予Happy与sleep删除(delete)chores 表内容的权限并把这个权限授予其他人
GRANT SELECT(chore_name) ON chores TO dopey; # 让Dopey只能从chores表中选择(SELECT)chores_name列。
GRANT SELECT, INSERT ON talking_animals TO sneezyy; # 授予Sneezy选择(SELECT)与插入(INSERT)内容至talking_animals表的权限。
GRANT ALL ON talking_animals TO bashful; # 授予bashful选择、更新、插入、删除talking_animals表内容的权限。
```
### 12.2 撤销用户权限
```
REMOVE SELECT ON clown_info FROM elsie;
REMOVE INSERT, DELETE ON locations FROM elsie;
REMOVE INSERT, DELETE, UPDATE ON clown_info FROM elsie;
REMOVE INSERT ON activities FROM elsie;
REMOVE DELETE on info_location FROM elsie CASCADE;
REMOVE GRANT INSERT(location), DELETE ON location FROM elsie;
```

### 12.3 设定根用户密码
```
SET PASSWORD FOR root@localhost = PASSWORD('123231231');
```
### 12.4 创建用户Frank
```
CREATE USER Frank IDENTIFIED BY '0000000000';
```
### 12.5 赋予员工不同的权限
```
GRANT SELECT ON ..... TO Frank;
GARNT DELETE ON ///// TO Frank;

GRANT INSERT ON ..... TO Jim;
GRANT UPDATE ON ///// TO Jim;

GARNT SELECT ON ///// TO Joe;
```

***CREATE USER*** ：使用这个语句创建用户并设置密码

***GRANT*** :根据授予用户的权限，精确控制用户对数据库的操作范围

***REVOKE***: 用于撤销用户的权限。

***WITH GRANT OPTION*** :让用户把自己获得的权限授予其他人。

***ROLE***:
角色指一组权限。角色能把一组特定权限一次授予多名用户。

***WITH ADMIN OPTION*** ：
让有角色的用户把同一个角色授予其他人。