#Data Definition Language (DDL) commands in SQL are used to define and modify the database structure. Here are the primary DDL commands
--1)CREATE: Used to create a new database object such as a table, view, or index.
-- Create a new table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthDate DATE
);
--2)ALTER: Used to modify an existing database object, such as adding or dropping columns from a table.
-- Add a new column to the Employees table
ALTER TABLE Employees
ADD Email VARCHAR(100);

-- Drop a column from the Employees table
ALTER TABLE Employees
DROP COLUMN BirthDate;
--3)DROP: Used to delete an existing database object, like a table, view, or index.
-- Drop the Employees table
DROP TABLE Employees;
--4)TRUNCATE: Used to remove all records from a table, but the table structure remains.
-- Remove all records from the Employees table
TRUNCATE TABLE Employees;
--5)RENAME: Used to rename a database object.
-- Rename the Employees table to Staff
ALTER TABLE Employees
RENAME TO Staff;
--6)COMMENT: Used to add comments to the data dictionary.
-- Add a comment to the Employees table
COMMENT ON TABLE Employees IS 'Table for storing employee details';
--Example of DDL commands:
-- 1. Create a new table named Employees
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    BirthDate DATE
);

-- 2. Add a new column named Email to the Employees table
ALTER TABLE Employees
ADD Email VARCHAR(100);

-- 2. Drop the BirthDate column from the Employees table
ALTER TABLE Employees
DROP COLUMN BirthDate;

-- 4. Remove all records from the Employees table
TRUNCATE TABLE Employees;

-- 5. Rename the Employees table to Staff
ALTER TABLE Employees
RENAME TO Staff;

-- 6. Add a comment to the Employees table
COMMENT ON TABLE Staff IS 'Table for storing employee details';

--Data Manipulation Language (DML) commands in SQL are used to manage data within the database. The main DML commands include:
-- 1)INSERT: Adds new records into a table.
-- Insert a new employee into the Employees table
INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID, Salary)
VALUES (1, 'John', 'Doe', 101, 60000);

--2)UPDATE: Modifies existing records in a table.
-- Update the salary of employee with EmployeeID 1
UPDATE Employees
SET Salary = 65000
WHERE EmployeeID = 1;
--3)DELETE: Removes records from a table.
-- Delete the employee with EmployeeID 1 from the Employees table
DELETE FROM Employees
WHERE EmployeeID = 1;
--4)MERGE (if supported by the database, such as in SQL Server):
-- Merge data from a source table into a target table based on a matching condition
MERGE INTO TargetTable AS T
USING SourceTable AS S
ON T.KeyColumn = S.KeyColumn
WHEN MATCHED THEN
    UPDATE SET T.ColumnToUpdate = S.NewValue
WHEN NOT MATCHED THEN
    INSERT (KeyColumn, Column1, Column2)
    VALUES (S.KeyColumn, S.Value1, S.Value2)
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
- Create the Employees table
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT,
    Salary DECIMAL(10, 2)
);

-- Create the NewEmployees table
CREATE TABLE NewEmployees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT,
    Salary DECIMAL(10, 2)
);

-- Insert new employees into the Employees table
INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID, Salary)
VALUES (1, 'John', 'Doe', 101, 60000),
       (2, 'Jane', 'Smith', 102, 70000),
       (3, 'Jim', 'Brown', 103, 50000);

-- Update the salary of employee with EmployeeID 1
UPDATE Employees
SET Salary = 65000
WHERE EmployeeID = 1;

-- Delete the employee with EmployeeID 3 from the Employees table
DELETE FROM Employees
WHERE EmployeeID = 3;

-- Insert new and updated employees into the NewEmployees table
INSERT INTO NewEmployees (EmployeeID, FirstName, LastName, DepartmentID, Salary)
VALUES (1, 'John', 'Doe', 101, 65000), -- Existing employee, same details
       (2, 'Jane', 'Smith', 102, 72000), -- Existing employee, updated salary
       (4, 'Sara', 'Connor', 104, 80000); -- New employee

-- Merge data from NewEmployees into Employees
MERGE INTO Employees AS E
USING NewEmployees AS N
ON E.EmployeeID = N.EmployeeID
WHEN MATCHED THEN
    UPDATE SET E.FirstName = N.FirstName,
               E.LastName = N.LastName,
               E.DepartmentID = N.DepartmentID,
               E.Salary = N.Salary
WHEN NOT MATCHED THEN
    INSERT (EmployeeID, FirstName, LastName, DepartmentID, Salary)
    VALUES (N.EmployeeID, N.FirstName, N.LastName, N.DepartmentID, N.Salary)
WHEN NOT MATCHED BY SOURCE THEN
    DELETE;
--DQL (Data Query Language) is a subset of SQL (Structured Query Language) used to query data from databases. The most common DQL command is SELECT, which retrieves data from a database. Here are some essential SELECT command usages and options:
--1)Basic SELECT:
SELECT column1, column2, ...
FROM table_name;
--Retrieves specified columns from a table.
SELECT All Columns:
SELECT *
FROM table_name;
--Retrieves all columns from a table.
--SELECT with WHERE Clause:
SELECT column1, column2, ...
FROM table_name
WHERE condition;
--Retrieves rows that meet the specified condition.
SELECT with ORDER BY:
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC];
--Sorts the result set by the specified column in ascending or descending order.
SELECT with JOIN:
SELECT table1.column1, table2.column2, ...
FROM table1
JOIN table2
ON table1.common_field = table2.common_field;
--Retrieves data from multiple tables based on a related column between them.
SELECT with GROUP BY:
SELECT column1, COUNT(*)
FROM table_name
GROUP BY column1;
--Groups rows that have the same values in specified columns into summary rows.
SELECT with HAVING:
SELECT column1, COUNT(*)
FROM table_name
GROUP BY column1
HAVING COUNT(*) > value;
--Filters groups based on a specified condition.
SELECT DISTINCT:
SELECT DISTINCT column1
FROM table_name;
--Retrieves unique values from the specified column.
SELECT with LIMIT:
SELECT column1, column2, ...
FROM table_name
LIMIT number;
--Limits the number of rows returned.
--BASIC SELECT:

--Quieries:
--1)How do you retrieve the first name and last name from the employees table?
SELECT first_name, last_name
FROM employees;
--2)How do you retrieve all columns from the employees table?
SELECT *
FROM employees;
--3)How do you retrieve the first name and last name of employees who work in the Sales department?
[6/18, 3:20 PM] Tarun Phogat: SELECT first_name, last_name
FROM employees
WHERE department = 'Sales';
--4)How do you retrieve the first name and last name of employees, sorted by last name in ascending order?
SELECT first_name, last_name
FROM employees
ORDER BY last_name ASC;
--5)How do you retrieve the first name, last name, and department name by joining the employees and departments tables on the department_id field?
SELECT employees.first_name, employees.last_name, departments.department_name
FROM employees
JOIN departments ON employees.department_id = departments.department_id;
--6)How do you group employees by department and count the number of employees in each department?
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
--7)How do you retrieve departments with more than 10 employees by grouping the employees and applying the HAVING clause?
SELECT department, COUNT(*)
FROM employees
GROUP BY department
HAVING COUNT(*) > 10;
--8)How do you retrieve the first 5 rows from the employees table?
SELECT first_name, last_name
FROM employees
LIMIT 5;
--9)How do you retrieve unique department names from the employees table?
SELECT DISTINCT department
FROM employees;
--10)How do you retrieve the first name, last name, and department name of unique employees who work in the Sales department, sort them by last name in ascending order, limit the result to 10 rows, and ensure each department has more than 5 employees?
SELECT DISTINCT e.first_name AS fname, e.last_name AS lname, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE d.department_name = 'Sales'
GROUP BY e.first_name, e.last_name, d.department_name
HAVING COUNT(e.employee_id) > 5
ORDER BY e.last_name ASC
LIMIT 10;
