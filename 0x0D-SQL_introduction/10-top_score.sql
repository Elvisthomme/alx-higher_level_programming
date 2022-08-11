-- List all records of the table second_table
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)

-- Command: SELECT column1, column2, ... FROM table_name [ORDER BY columnX] [ASC|DESC];
SELECT score, name FROM second_table ORDER BY score DESC;
