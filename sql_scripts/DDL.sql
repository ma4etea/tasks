CREATE DATABASE test;

DROP DATABASE test;

CREATE SCHEMA product;

DROP SCHEMA public;

CREATE TABLE product.users(id serial PRIMARY KEY,
name char(10));

CREATE TABLE product.products(id serial PRIMARY KEY,
name char(10));

DROP SCHEMA product CASCADE;

ALTER TABLE product.users ADD COLUMN email varchar(255);

ALTER TABLE product.users ADD COLUMN age integer;

CREATE INDEX users_age ON
product.users(age);

DROP INDEX product.users_age;

CREATE INDEX users_age1 ON
product.users
	USING hash (age);

INSERT
	INTO
	product.users(name,
	email,
	age)
VALUES('Alex', 'alex@alex.com', 33);

SELECT
	*
FROM
	product.users;

TRUNCATE
	TABLE product.users;

CREATE TYPE product.user_roles AS ENUM ('user',
'admin');

ALTER TABLE product.users 
ADD COLUMN ROLE product.user_roles NOT NULL DEFAULT 'user';

SELECT
	*
FROM
	product.users u ;

ALTER TABLE product.users
ALTER COLUMN name TYPE varchar(10);