-- Creates a trigger that decreases a quantity after update.
DELIMITER $$
DROP TRIGGER IF EXISTS reduce_item$$
CREATE
TRIGGER reduce_item
AFTER INSERT ON orders 
FOR EACH ROW
BEGIN
UPDATE items
SET quantity = quantity - New.number
WHERE name = New.item_name;
END$$
