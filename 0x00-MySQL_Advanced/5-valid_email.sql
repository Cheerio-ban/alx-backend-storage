-- Creates a trigger and reset the value valid_email
DELIMITER $$
DROP TRIGGER IF EXISTS check_valid_email$$
CREATE
TRIGGER check_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
IF NEW.email != OLD.email
THEN SET NEW.valid_email = 0;
END IF;
$$
