-- 4. Buy buy buy
-- Create a trigger that decreases the quantity of an item after adding a new order
-- Requirements:
--   - Quantity in table `items` can be negative
--   - Should run on any database
--   - Orders table: (item_name VARCHAR(255), number INT)
--   - Items table: (name VARCHAR(255), quantity INT)
-- The trigger updates items.quantity by subtracting NEW.number when a row is inserted into orders

-- Drop trigger if it already exists to avoid failure on re-run
DROP TRIGGER IF EXISTS decrease_quantity_after_insert;

-- Create the trigger
DELIMITER $$
CREATE TRIGGER decrease_quantity_after_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  -- Decrease the quantity of the ordered item by the ordered amount
  UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END $$
DELIMITER ;
