-- Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL UNIQUE AUTO_INCREMENT,
    state_id NOT NULL FOREING KEY (state_id) REFERENCE states (id),
    name VARCHAR(256) NOT NULL
);
