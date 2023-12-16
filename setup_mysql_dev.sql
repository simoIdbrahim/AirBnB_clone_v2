-- Creates a MySQL server with:
--   Database hbnb_dev_db.
--   User hbnb_dev with password hbnb_dev_pwd in localhost.
--   Grants all privileges for hbnb_dev on hbnb_dev_db.
--   Grants SELECT privilege for hbnb_dev on performance.

-- Create the database if NOT exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if NOT exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all Permissions to user hbnb_dev on localhost
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant // Give all permission to control perfomance shema to user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges // reload system to apply changes
FLUSH PRIVILEGES;