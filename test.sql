CREATE DATABASE car_dealership; 

/** CREATING TABLE */

CREATE TABLE Employees
(
    Employee_ID integer NOT NULL,
    Employee_Name VARCHAR(255),
    Roles VARCHAR(100),
    Emp_Contact_Num integer,
    Address VARCHAR(300),
    PRIMARY KEY (Employee_ID)
)

CREATE TABLE Customers
(
    Customer_ID integer NOT NULL,
    Inventory_ID integer,
    C_FName VARCHAR(255),
    C_LName VARCHAR(255),
    Address VARCHAR(500),
    Date_of_Purchase date,
    PRIMARY KEY (Customer_ID),
    FOREIGN KEY (Inventory_ID)
        REFERENCES Inventory (Inventory_ID)
)


CREATE TABLE Inventory
(
    Inventory_ID integer NOT NULL,
    Employee_ID integer,
    Model_Number VARCHAR(255),
    Accessories_ID integer,
    Manufacturing_Date date,
    PRIMARY KEY (Inventory_ID),
    FOREIGN KEY (Employee_ID)
        REFERENCES Employees (Employee_ID)
)


CREATE TABLE Appointment
(
    Appointment_ID integer NOT NULL,
    Customer_ID integer,
    Employee_ID integer,
    Appointment_Date date,
    Appointment_Time TIME,
    PRIMARY KEY (Appointment_ID),
    FOREIGN KEY (Customer_ID)
        REFERENCES Customers (Customer_ID),
    FOREIGN KEY (Employee_ID)
        REFERENCES Employees (Employee_ID)
)

CREATE TABLE Service
(
    Service_ID integer NOT NULL,
    Appointment_ID integer,
    Employee_ID integer,
    Issue_ID integer,
    PRIMARY KEY (Service_ID),
    FOREIGN KEY (Appointment_ID)
        REFERENCES Appointment (Appointment_ID),
    FOREIGN KEY (Employee_ID)
        REFERENCES Employees (Employee_ID),
    FOREIGN KEY (Issue_ID)
        REFERENCES Issues (Issue_ID)
)

CREATE TABLE Issues
(
    Issue_ID integer NOT NULL,
    Accessories_ID integer,
    Report VARCHAR(500),
    PRIMARY KEY (Issue_ID),
    FOREIGN KEY (Accessories_ID)
        REFERENCES Accessories (Accessories_ID) 
)


CREATE TABLE Accessories
(
    Accessories_ID integer NOT NULL,
    Windscreen VARCHAR(255),
    Wheels VARCHAR(255),
    Engine VARCHAR(255),
    Acc_MDate date,
    PRIMARY KEY (Accessories_ID)
)

/** SQL Sample Data*/

INSERT INTO Employees
VALUES (3001, 'CHARLES GOH', 'SALESPERSON', 66554477, 'JALAN JALN2');

INSERT INTO Employees
VALUES (3002, 'LIM PENG PENG', 'SERVICE REPRESENTATIVE', 66554499, 'JALAN JALAN3');


INSERT INTO Customers
VALUES (1001, 2001, 'Zhang Yu', 'Goh', 'Jalan Jalan', '1/1/20');

INSERT INTO Customers
VALUES (1002, 2002, 'Charles', 'James Goh', 'Jalan Jalan2', '2/1/20');


INSERT INTO Inventory
VALUES (2001, 3001, '530i', 6001, '1/6/19');

INSERT INTO Inventory
VALUES (2002, 3002, '645i', 6002, '1/6/19');


INSERT INTO Appointment
VALUES (4001, 1001, 3002, '1/1/21', '09:00');

INSERT INTO Appointment
VALUES (4002, 1002, 3002, '2/1/21', '10:00');

INSERT INTO Service
VALUES (5001, 4001, 3002, 7001);

INSERT INTO Service
VALUES (5002, 4002, 3002, 7002);


INSERT INTO Issues
VALUES (7001, 6001, 'Four Wheel drive faulty');

INSERT INTO Accessories
VALUES (7002, 6002, 'Aircon not cold, brake squeeking sound');


INSERT INTO Accessories
VALUES (6001, 'Razer Screen', '15inch wheels', 'twin turbo', '8/9/19');

INSERT INTO Accessories
VALUES (6002, 'Tough Screen', '18inch wheels', 'twin turbo', '9/9/19');
