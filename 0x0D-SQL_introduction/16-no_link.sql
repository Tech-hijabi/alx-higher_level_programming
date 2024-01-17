-- Task: List all records of the table second_table excluding rows without a name value
-- Records are listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
