-- 7. Average score
-- Create a stored procedure ComputeAverageScoreForUser(user_id INT)
-- Behavior:
--   - Compute AVG(score) from corrections for the given user_id
--   - Store the result (can be decimal) into users.average_score
-- Re-runnable: drop procedure if it exists

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
  DECLARE v_avg FLOAT;

  SELECT AVG(score) INTO v_avg
  FROM corrections
  WHERE user_id = p_user_id;

  UPDATE users
  SET average_score = IFNULL(v_avg, 0)
  WHERE id = p_user_id;
END $$
DELIMITER ;
