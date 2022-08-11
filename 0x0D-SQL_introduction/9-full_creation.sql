-- Create a table second_table in the database hbtn_0c_0

-- command CREATE TABLE table_name(c1 type1, c2 type2, ...)
CREATE TABLE second_table(id INT, name VARCHAR(256), score INT);

-- Insert multiples row to the table

-- command INSERT INTO table_name(c1, c2, ...) VALUES(v1, v1, ...)
INSERT INTO second_table(id, name, score) VALUES(1, 'John', 10);
INSERT INTO second_table(id, name, score) VALUES(2, 'Alex', 3);
INSERT INTO second_table(id, name, score) VALUES(3, 'Bob', 14);
INSERT INTO second_table(id, name, score) VALUES(4, 'George', 8);
