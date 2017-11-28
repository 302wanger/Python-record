# ALTER 
## 改写历史

### 1.1 修改表
	CHANGE: 可同时更改现有列的名称和数据类型。
	MODIFY: 修改现有列的数据类型或位置
	ADD   : 在当前表中添加一列---可自选类型
	DROP  : 从表中删除某列
	
	
### 1.2 修改表名称

```
ALTER TABLE projects
RENAME TO project_list;
```
### 1.3 ALTER AND CHANGE

把number列名改为proj_id，并把它设置为AUTO_INCEEMENT，然后把它标注为主键。
```
ALTER TABLE project_list
CHANGE COLUMN number proj_id INT NOT NULL AUTO_INCREMENT,
ADD PRIMARY KEY (proj_id);
```
