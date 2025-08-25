-- 5. Email validation to sent
-- Create a trigger that resets valid_email ONLY when the email has changed
-- Table: users(id INT AI PK, email VARCHAR(255) NOT NULL, name VARCHAR(255), valid_email BOOLEAN NOT NULL DEFAULT 0)
-- Re-runnable: drop trigger if it already exists
-- Use BEFORE UPDATE so we can modify NEW.valid_email
-- Create the trigger
DROP TRIGGER IF EXISTS reset_valid_email_on_email_change;
DELIMITER $$
CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  -- If the email value is actually changing, reset the validation flag
  IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
  END IF;
END $$
DELIMITER ;
