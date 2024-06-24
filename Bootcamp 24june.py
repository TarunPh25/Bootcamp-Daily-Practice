-- Create database
create database zomato;

use zomato;

-- Restaurants - rid, rname, location
create table restaurants
(
    rid int(3) primary key,
    rname varchar(50) not null,
    location varchar(30)
);

-- Customers - cid, cname, age, addr
create table customers
(
    cid int(3) primary key,
    cname varchar(30) not null,
    age int(3),
    addr varchar(50)
);

-- Menu Items - mid, rid, mname, price, stock
create table menu_items
(
    mid int(3) primary key,
    rid int(3),
    mname varchar(50) not null,
    price int(10) not null,
    stock int(5),
    foreign key(rid) references restaurants(rid)
);

-- Orders - oid, cid, mid, quantity
create table orders
(
    oid int(3) primary key,
    cid int(3),
    mid int(3),
    quantity int(5),
    foreign key(cid) references customers(cid),
    foreign key(mid) references menu_items(mid)
);

-- Payments - pay_id, oid, amount, mode, status
create table payments
(
    pay_id int(3) primary key,
    oid int(3),
    amount int(10) not null,
    mode varchar(30) check(mode in('upi','credit','debit')),
    status varchar(30),
    foreign key(oid) references orders(oid)
);

# Inserting values into restaurants table
insert into restaurants values(1, 'Burger King', 'Mumbai');
insert into restaurants values(2, 'Pizza Hut', 'Delhi');
insert into restaurants values(3, 'Subway', 'Mumbai');
insert into restaurants values(4, 'KFC', 'Delhi');

# Inserting values into customers table
insert into customers values(101, 'Ravi', 30, 'Mumbai');
insert into customers values(102, 'Rahul', 25, 'Delhi');
insert into customers values(103, 'Simran', 32, 'Mumbai');
insert into customers values(104, 'Purvesh', 28, 'Delhi');
insert into customers values(105, 'Sanjana', 22, 'Mumbai');

# Inserting values into menu_items table
insert into menu_items values(1, 1, 'Whopper', 200, 50);
insert into menu_items values(2, 2, 'Pepperoni Pizza', 500, 30);
insert into menu_items values(3, 3, 'Sub Sandwich', 150, 20);
insert into menu_items values(4, 4, 'Fried Chicken', 300, 40);

# Inserting values into orders table
insert into orders values(1001, 101, 1, 2);
insert into orders values(1002, 102, 2, 1);
insert into orders values(1003, 103, 3, 3);
insert into orders values(1004, 104, 4, 1);

# Inserting values into payments table
insert into payments values(1, 1001, 400, 'upi', 'completed');
insert into payments values(2, 1002, 500, 'credit', 'completed');
insert into payments values(3, 1003, 450, 'debit', 'in process');
insert into payments values(4, 1004, 300, 'upi', 'completed');


-- TCL (Transaction control language) Commands
/*
TCL commands are used to manage transactions, maintain ACID properties, and control the flow of data modifications.
TCL commands ensure the consistency and durability of data in a database.
For example, if an operation fails during a transaction, the transaction is rolled back.
When a transaction is committed, its changes are permanent, even if the system fails or restarts.
TCL commands also ensure that all operations within a transaction are executed as a single unit.
*/

-- commit
/*
Commit: Saves a transaction to the database
*/
commit;
-- rollback
/*
Rollback: Undoes a transaction or change that hasn't been saved to the database
*/
rollback;

-- savepoint
/*
Savepoint: Temporarily saves a transaction for later rollback 
*/
savepoint a;
-- here it will store that as a
-- after we can call that by rollback to a
rollback to a;

-- any operation performed on table using dml
-- insert,delete,update every command is transaction 

/*
In mysql it is having auto commit so is doesnot make anysense transaction commands in mysql
for this we have to use command start transaction
*/

-- Triggers 

-- Trigger is a statement that a system executes automatically when there is any modification to the database
-- Triggers are used to specify certain integrity constraints and referential constraints that cannot be specified using the constraint mechanism of SQL

-- Trigers are 6 types 
/*
1)after insert -- activated after data is inserted into the table.
2)after update -- activated after data in the table is modified. 
3)after delete -- activated after data is deleted/removed from the table. 
4)before insert -- activated before data is inserted into the table. 
5)before update -- activated before data in the table is modified.
6)before delete --  activated before data is deleted/removed from the table. 
*/
-- Delimiters are necessary when creating stored procedures or triggers
-- Delimiters are used in MySQL to avoid conflicts with semicolons within SQL statements

-- "SQL Trigger for Logging Product Insertions"
-- after insert
DELIMITER //
CREATE TRIGGER products_after_insert
AFTER INSERT ON products
FOR EACH ROW
BEGIN
  INSERT INTO product_log (pid, pname, price, stock, location, inserted_at)
  VALUES (NEW.pid, NEW.pname, NEW.price, NEW.stock, NEW.location, NOW());
END //
DELIMITER ;

-- create an SQL trigger to automatically update product stock levels after each new order is inserted into the 'orders' table?
DELIMITER //
CREATE TRIGGER orders_after_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE products
  SET stock = stock - 1
  WHERE pid = NEW.pid;
END //
DELIMITER ;


-- after update 

-- SQL trigger to log changes made to product information whenever an update occurs in the 'products' table?
DELIMITER //
CREATE TRIGGER products_after_update
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
  IF OLD.pid <> NEW.pid OR OLD.pname <> NEW.pname OR OLD.price <> NEW.price OR OLD.stock <> NEW.stock OR OLD.location <> NEW.location THEN
    INSERT INTO product_log (pid, pname, price, stock, location, updated_at)
    VALUES (OLD.pid, OLD.pname, OLD.price, OLD.stock, OLD.location, NOW());
  END IF;
END //
DELIMITER ;


-- after delete 

-- SQL trigger to prevent the deletion of a product from the 'products' table if there are existing orders referencing that product in the 'orders' table?
DELIMITER //
CREATE TRIGGER products_after_delete
AFTER DELETE ON products
FOR EACH ROW
BEGIN
  -- Log information about deleted product (optional)
  -- INSERT INTO product_log (pid, pname, price, stock, location, deleted_at)
  -- VALUES (OLD.pid, OLD.pname, OLD.price, OLD.stock, OLD.location, NOW());

  -- Check if there are existing orders referencing the deleted product
  DECLARE has_orders INT DEFAULT (0);

  SELECT COUNT(*) INTO has_orders
  FROM orders
  WHERE pid = OLD.pid;

  IF has_orders > 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete product with existing orders. Update or delete orders first.';
  END IF;
END //
DELIMITER ;

-- before insert

#Trigger for Automatic Payment Status on Payment Insert
DELIMITER //

CREATE TRIGGER set_default_payment_status
BEFORE INSERT ON payment
FOR EACH ROW
BEGIN
  IF NEW.status IS NULL THEN
    SET NEW.status = 'Pending';
  END IF;
END //

DELIMITER ;

/*
While SQL Workbench and many database management tools don't natively support BEFORE UPDATE and BEFORE DELETE triggers
*/

/*
													Uses of tirggers
Enforcing Data Integrity and Business Rules:

Data Validation: Triggers can validate data before it's inserted or updated, ensuring it adheres to specific rules. 
For example, a trigger can prevent negative product stock values or enforce a minimum age requirement for customer entries.

Maintaining Referential Integrity: Triggers can automatically maintain relationships between tables. 
When a record is deleted from a parent table (e.g., customers), a trigger can cascade the deletion to related child records (e.g., orders) or prevent deletion if dependent records exist.

Enforcing Business Logic: Triggers can implement complex business rules that might not be easily achievable with standard SQL statements. 
For instance, a trigger could automatically calculate discounts based on order amount or apply loyalty point adjustments upon successful purchases.

security:Triggers can enforce data access restrictions or security checks on specific events within the database.

Performance Impact: Triggers can introduce overhead to data manipulation operations. Analyze their impact on performance and optimize them if necessary.

Trigger Order: When using multiple triggers, their execution order can be important. Define the order in which triggers fire to ensure desired results.

*/

-- Triggers

-- Trigger to update stock after an order is placed
DELIMITER //
CREATE TRIGGER update_stock_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE menu_items
    SET stock = stock - NEW.quantity
    WHERE mid = NEW.mid;
END //
DELIMITER ;

-- Trigger to check stock availability before inserting an order
DELIMITER //
CREATE TRIGGER check_stock_before_order
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE available_stock INT;
    SELECT stock INTO available_stock FROM menu_items WHERE mid = NEW.mid;
    IF available_stock < NEW.quantity THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Insufficient stock for this menu item';
    END IF;
END //
DELIMITER ;

-- Trigger to set default payment status
DELIMITER //
CREATE TRIGGER set_default_payment_status
BEFORE INSERT ON payments
FOR EACH ROW
BEGIN
    IF NEW.status IS NULL THEN
        SET NEW.status = 'Pending';
    END IF;
END //
DELIMITER ;

-- Views

-- View to display customers with their corresponding orders
CREATE VIEW CustomerOrders AS
SELECT c.cid, c.cname, o.oid, o.quantity, m.mname
FROM customers c
JOIN orders o ON c.cid = o.cid
JOIN menu_items m ON o.mid = m.mid;

-- View to show payment details with order and customer information
CREATE OR REPLACE VIEW PaymentOrderCustomerDetails AS
SELECT p.pay_id, p.oid, o.cid, c.cname, c.age, c.addr, p.amount, p.mode, p.status
FROM payments p
JOIN orders o ON p.oid = o.oid
JOIN customers c ON o.cid = c.cid;

-- Drop view if exists
DROP VIEW IF EXISTS PaymentOrderCustomerDetails;
