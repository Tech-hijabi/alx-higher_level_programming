-- Task: Convert hbtn_0c_0 database, first_table table, and name field to UTF8
-- Use the specified database
USE hbtn_0c_0;

-- Convert the table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
