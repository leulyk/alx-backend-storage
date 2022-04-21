-- Create a table to hold data of Users
CREATE TABLE IF NOT EXISTS users
(id INT AUTO_INCREMENT NOT NULL, 
 email varchar(255) NOT NULL UNIQUE,
 name varchar(255),
 PRIMARY KEY(id)
)
