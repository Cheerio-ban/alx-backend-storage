-- Creates a trigger and reset the value valid_email
DELIIMITER $$
DROP TRIGGER IF EXISTS check_valid_email$$
CREATE
TRIGGER check_valid_email
BEFORE UPDATE
ON users FOR EACH ROW
IF New.email <> Old.email THEN
SET New.valid_email = 0;
END IF;
$$