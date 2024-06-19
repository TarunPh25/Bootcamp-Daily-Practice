--JOINS
---> As the word suggests, Joins are used to combine two or more tables to get specific data/information
-- Join is mainly of 6 types:
--1. Inner Join
--2. Left Outer Join
--3. Right Outer Join
--4. Full Outer Join
--5. Self Join
--6. Cross Join

-- Creating database
CREATE DATABASE zomato;

-- Using database
USE zomato;

-- Creating table Restaurants - rid, rname, location
CREATE TABLE restaurants (
    rid INT PRIMARY KEY,
    rname VARCHAR(50) NOT NULL,
    location VARCHAR(50) NOT NULL
);

-- Creating table Customers - cid, cname, age, addr
CREATE TABLE customers (
    cid INT PRIMARY KEY,
    cname VARCHAR(50) NOT NULL,
    age INT,
    addr VARCHAR(100)
);

-- Creating table Orders - oid, cid, rid, amount
CREATE TABLE orders (
    oid INT PRIMARY KEY,
    cid INT,
    rid INT,
    amount INT NOT NULL,
    FOREIGN KEY (cid) REFERENCES customers(cid),
    FOREIGN KEY (rid) REFERENCES restaurants(rid)
);

-- Creating table Payment - pay_id, oid, amount, mode (upi, credit, debit), status
CREATE TABLE payment (
    pay_id INT PRIMARY KEY,
    oid INT,
    amount INT NOT NULL,
    mode VARCHAR(30) CHECK (mode IN ('upi', 'credit', 'debit')),
    status VARCHAR(30),
    FOREIGN KEY (oid) REFERENCES orders(oid)
);

-- Creating table Employee - eid, ename, phone_no, department, manager_id
CREATE TABLE employee (
    eid INT PRIMARY KEY,
    ename VARCHAR(50) NOT NULL,
    phone_no BIGINT NOT NULL,
    department VARCHAR(50) NOT NULL,
    manager_id INT
);


-- Inserting values into Restaurants table
INSERT INTO restaurants VALUES (1, 'Pizza Hut', 'Mumbai');
INSERT INTO restaurants VALUES (2, 'Dominos', 'Delhi');
INSERT INTO restaurants VALUES (3, 'KFC', 'Bangalore');
INSERT INTO restaurants VALUES (4, 'Burger King', 'Mumbai');
INSERT INTO restaurants VALUES (5, 'Subway', 'Delhi');

-- Inserting values into Customers table
INSERT INTO customers VALUES (101, 'Ravi', 30, 'Mumbai');
INSERT INTO customers VALUES (102, 'Rahul', 25, 'Delhi');
INSERT INTO customers VALUES (103, 'Simran', 32, 'Bangalore');
INSERT INTO customers VALUES (104, 'Purvesh', 28, 'Mumbai');
INSERT INTO customers VALUES (105, 'Sanjana', 22, 'Delhi');

-- Inserting values into Orders table
INSERT INTO orders VALUES (1001, 101, 1, 500);
INSERT INTO orders VALUES (1002, 102, 2, 300);
INSERT INTO orders VALUES (1003, 103, 3, 200);
INSERT INTO orders VALUES (1004, 104, 4, 400);
INSERT INTO orders VALUES (1005, 105, 5, 150);

-- Inserting values into Payment table
INSERT INTO payment VALUES (1, 1001, 500, 'upi', 'completed');
INSERT INTO payment VALUES (2, 1002, 300, 'credit', 'completed');
INSERT INTO payment VALUES (3, 1003, 200, 'debit', 'in process');

-- Inserting values into Employee table
INSERT INTO employee VALUES (201, 'Rohan', 9876543210, 'Sales', 205);
INSERT INTO employee VALUES (202, 'Rahul', 8765432109, 'Delivery', 206);
INSERT INTO employee VALUES (203, 'Shyam', 7654321098, 'Delivery', 202);
INSERT INTO employee VALUES (204, 'Neha', 6543210987, 'Sales', 202);
INSERT INTO employee VALUES (205, 'Sanjana', 5432109876, 'HR', 204);
INSERT INTO employee VALUES (206, 'Sanjay', 4321098765, 'Tech', NULL);

--Different Types of Joins:
--1) Inner Join: Matching values from both tables should be present
-- Example 1: Get customer names who placed orders
SELECT customers.cid, cname, orders.oid FROM orders
INNER JOIN customers ON orders.cid = customers.cid;

-- Example 2: Get customer names and restaurant names from orders
SELECT customers.cid, cname, restaurants.rid, rname, oid FROM orders
INNER JOIN restaurants ON orders.rid = restaurants.rid
INNER JOIN customers ON orders.cid = customers.cid;
--2)Left outer Join: All the rows from the left table should be present and matching rows from the right table are present.
-- Example: Get all restaurants and their order amounts (if any)
SELECT restaurants.rid, rname, amount, orders.oid FROM restaurants
LEFT JOIN orders ON orders.rid = restaurants.rid;
--3)Right Join: All the rows from the right table should be present and only matching rows from the left table are present.
-- Example: Get all order details and their payment status
SELECT * FROM payment
RIGHT JOIN orders ON orders.oid = payment.oid;
--4) Full outer Join: All the rows from both the table should be present 
-- Note: MySQL does not support FULL OUTER JOIN directly
-- Using UNION of LEFT JOIN and RIGHT JOIN

-- Example: Get all orders and restaurant details
SELECT orders.oid, restaurants.rid, rname, amount FROM orders
LEFT JOIN restaurants ON orders.rid = restaurants.rid
UNION
SELECT orders.oid, restaurants.rid, rname, amount FROM orders
RIGHT JOIN restaurants ON orders.rid = restaurants.rid;
--5)Self Join: It is a regular join, but the table is joined by itself.
-- Example: Get employees and their managers
SELECT e1.ename AS Employee, e2.ename AS Manager FROM employee e1
INNER JOIN employee e2 ON e1.manager_id = e2.eid;
--6)Cross Join: It is used to view all the possible combinations of the rows of one table and with all the rows from second table.
-- Example: Get all combinations of customers and their orders where amount is greater than 200
SELECT customers.cid, cname, orders.oid, amount FROM customers
CROSS JOIN orders ON customers.cid = orders.cid
WHERE amount > 200;
--Quires: 
-- Display details of all orders which were delivered from "Mumbai"
SELECT * FROM orders 
INNER JOIN restaurants ON orders.rid = restaurants.rid
WHERE location = 'Mumbai';

-- Display details of all orders whose payment was made through "UPI"
SELECT * FROM orders
INNER JOIN payment ON orders.oid = payment.oid
WHERE mode = 'upi';

-- Display oid, amount, cname, payment mode of orders which were made by people below 30 years
SELECT orders.oid, amount, cname, mode FROM orders
INNER JOIN payment ON orders.oid = payment.oid
INNER JOIN customers ON orders.cid = customers.cid
WHERE age < 30;

-- Display oid, amount, cname, payment mode of orders which were made by people below 30 years and payment was made through "Credit"
SELECT orders.oid, amount, cname, mode FROM orders
INNER JOIN payment ON orders.oid = payment.oid
INNER JOIN customers ON orders.cid = customers.cid
WHERE age < 30 AND mode = 'credit';

-- Display oid, amount, cname, rname, location of the orders whose payment is still pending or in process
SELECT orders.oid, amount, cname, rname, location FROM orders
INNER JOIN restaurants ON orders.rid = restaurants.rid
INNER JOIN customers ON orders.cid = customers.cid
INNER JOIN payment ON orders.oid = payment.oid
WHERE status IN ('in process', 'pending');

-- Display details of orders, products ordered, and details of the customer who placed the order
SELECT orders.oid, cname, rname FROM orders
INNER JOIN customers ON orders.cid = customers.cid
INNER JOIN restaurants ON orders.rid = restaurants.rid;

--Normalization: Normalization is a process used in databases to organize data to reduce redundancy and improve data integrity. The goal is to decompose a database into smaller, more manageable pieces while maintaining relationships between data.

--Types of normalization:
--1)First normal form:
--> Multi valued attr should not be present
--> Primary key is present in the table
--> Repeating groups
--> Duplicate rows should not be there
-- Un-normalized Table:
/*
CustomerID   	Name	          Orders
1	          John Doe	         101, 102, 103
2	         Jane Smith	         04, 105

--1NF:
CustomerID	      Name	    OrderID
1	          John Doe	     101
1	          John Doe	     102
1	          John Doe	     103
2	          Jane Smith	 104
2	          Jane Smith	 105
*/
--2)Second Normal Form(2NF):
/*
-> Should be in 1NF
-> No partial dependency - 
All non key attr should be completely dependent
on primary key
1NF Table:
OrderID    	CustomerID	CustomerName
101	          1	          John Doe
102		      1           John Doe
103		      1           John Doe
104		      2           Jane Smith
105		      2           Jane Smith

2NF:
Orders Table:
OrderID	     CustomerID
101	           1
102            1
103	           1
104	           2
105	           2
Customers Table:
CustomerID	         CustomerName
1	                  John Doe
2	                  Jane Smith
*/
--3)Third Normal Form: Meet all the requirements of 2NF and all the attributes are functionally dependent only on the primary key.
/*2NF Orders Table:
OrderID   	CustomerID	     OrderDate	    SalesRep
101	          1	             2023-01-10	     Rep1
102	          1	             2023-01-15	     Rep1
103	          1	             2023-01-20	     Rep1
104	          2	             2023-02-10    	 Rep2
105	          2	             2023-02-15	     Rep2

3NF (Decomposed into three tables):
Orders Table:
OrderID	    CustomerID	   OrderDate
101	            1	        2023-01-10
102	            1	        2023-01-15
103	            1	        2023-01-20
104	            2	        2023-02-10
105	            2	        2023-02-15
Customers Table:
CustomerID	       CustomerName
1	                 John Doe
2	                 Jane Smith
SalesReps Table:
SalesRep	     CustomerID
Rep1                1
Rep2	            2
*/
--4)Boyce-Code Normal Form (BCNF):
/*
-->It is in 3NF.
-->Every non-trivial functional dependency X -> Y, X is a superkey.
--5)Fourth Normal Form (4NF):
-->It is in BCNF.
-->It has no multi-valued dependencies.
--6)Fifth Normal Form (5NF):
-->It is in 4NF.
-->It has no join dependency that is not implied by the candidate keys.
*/
