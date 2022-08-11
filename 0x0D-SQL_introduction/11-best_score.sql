-- List all records with a score >= 10 in the table second_table

-- Command: SELECT c1, c2, ... FROM table_name [WHERE condition]
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
