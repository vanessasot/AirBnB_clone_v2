-- This script that prepares a MySQL server...

-- Create an hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create a new user hbnb_dev (on localhost)
-- The password for hbnb_dev must be set to hbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- hbnb_dev must have all privileges on the hbnb_dev_db database
GRANT SELECT ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- hbnb_dev must have SELECT privilege on the performance_schema database.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
