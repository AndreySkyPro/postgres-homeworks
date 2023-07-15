-- SQL-команды для создания таблиц
CREATE TABLE employees(
	first_name varchar(255),
	last_name varchar(255),
	title varchar(255),
	birth_date date,
	notes text,
	employees_id serial PRIMARY KEY
);

CREATE TABLE customers(
	customer_id varchar(255) PRIMARY KEY,
	company_name varchar(255),
	contact_name varchar(255)
);

CREATE TABLE orders(
	order_id int PRIMARY KEY,
	customer_id varchar(255) REFERENCES customers(customer_id),
	employee_id smallserial REFERENCES employees(employees_id),
	order_date date,
	ship_city varchar(255)
);
