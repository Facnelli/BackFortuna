CREATE DATABASE IF NOT EXISTS finance_database;

CREATE TABLE IF NOT  EXISTS `finance_database`.`users` (
    id BIGINT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(255) NOT NULL, 
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    primary key (id)
);

