-- Creates a trigger and reset the value valid_email
DELIIMITER $$
DROP TRIGGER IF EXISTS check_valid_email$$
CREATE
TRIGGER check_valid_email
AFTER UPDATE
ON users FOR EACH ROW
BEGIN
    IF New.email <> Old.email Therion
    UPDATE users SET valid_email = DEFAULT WHERE id = New.id;
    END IF;
END$$
