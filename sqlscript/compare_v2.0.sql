ALTER TABLE permission ADD COLUMN permissiondes TEXT;

# 删除原有的age字段
ALTER TABLE student DROP COLUMN age;
ALTER TABLE student ADD COLUMN birthdate DATE;
ALTER TABLE student ADD COLUMN nation VARCHAR(4);
ALTER TABLE student ADD COLUMN stunum VARCHAR(32);
ALTER TABLE student ADD COLUMN stucontent text;