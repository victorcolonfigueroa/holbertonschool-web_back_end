-- 6. Add bonus
-- Create a stored procedure AddBonus(user_id INT, project_name VARCHAR(255), score INT)
-- Behavior:
--   - Ensure a project with name = project_name exists (create it if missing)
--   - Insert a new row into corrections(user_id, project_id, score)
-- This script can be executed on any database

-- Drop the procedure if it already exists so re-runs don't fail
DROP PROCEDURE IF EXISTS AddBonus;

-- Create the stored procedure
DELIMITER $$
CREATE PROCEDURE AddBonus(IN p_user_id INT, IN p_project_name VARCHAR(255), IN p_score INT)
BEGIN
  DECLARE v_project_id INT;

  -- Try to find existing project id by name
  SELECT id INTO v_project_id
  FROM projects
  WHERE name = p_project_name
  LIMIT 1;

  -- If not found, create the project and capture its id
  IF v_project_id IS NULL THEN
    INSERT INTO projects(name) VALUES (p_project_name);
    SET v_project_id = LAST_INSERT_ID();
  END IF;

  -- Insert the correction
  INSERT INTO corrections(user_id, project_id, score)
  VALUES (p_user_id, v_project_id, p_score);
END $$
DELIMITER ;
