# 3. DELETE AND UPDATE

1.1 删除特定的行

```
DELETE FROM clown_info
WHERE
activities = 'yellong,dancing'
AND name = 'Clarabelle';
```

1.2 更新特定的行

```
UPDATE doughunt_ratings
SET column_name = newvalue   -- set new value
WHERE type = 'plain glazed';  -- the same type with select and delete
```