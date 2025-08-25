-- SQL script that creates a table users with specified requirements
-- This script is compatible with MySQL and other SQL databases
-- The script will not fail if the table already exists

CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  UNIQUE (email)
);