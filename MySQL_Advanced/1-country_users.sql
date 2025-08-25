-- 1. In and out
-- Create table `users` with:
--   id INT NOT NULL AUTO_INCREMENT PRIMARY KEY
--   email VARCHAR(255) NOT NULL UNIQUE
--   name VARCHAR(255)
--   country ENUM('US','CO','TN') NOT NULL DEFAULT 'US'
-- If the table already exists, do not fail. This script can run on any database.
-- Create the table if it does not exist
CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255),
  country ENUM('US','CO','TN') NOT NULL DEFAULT 'US',
  UNIQUE (email)
);
