-- !***********************************************************************************************!
-- !****************************************** CUSTOMERS ******************************************!
-- !***********************************************************************************************!
-- Add new customer (/customerAdd):
INSERT INTO Customers (companyName, contactLastName, contactFirstName, phoneNumber, addressLine1, addressLine2, city, contactState, postalCode, email, specialDeliveryInst) 
    VALUES (:CREATE_companyName, :CREATE_contactLastName, :CREATE_contactFirstName, :CREATE_phoneNumber, :CREATE_addressLine1,:CREATE_addressLine2, :CREATE_city, 
            :CREATE_contactState, :CREATE_postalCode, :CREATE_email, :CREATE_specialDeliveryInst)

-- Look-up customers with the provided information (/customerLookUp):
SELECT * FROM Customers WHERE companyName = :READ_companyName AND contactLastName = :READ_contactLastName AND contactFirstName = :READ_contactFirstName AND phoneNumber = :READ_phoneNumber AND
                              addressLine1 = :READ_addressLine1 AND addressLine2 = :READ_addressLine2 AND city = :READ_city AND contactState = :READ_contactState AND postalCode = :READ_postalCode AND 
                              email = :READ_email AND specialDeliveryInst = :READ_specialDeliveryInst

-- Look-up all customers (/customerListAll):
SELECT * FROM Customers

-- Update specific customer information (/customerUpdate):
UPDATE Customers SET companyName = :UPDATE_companyName, contactLastName = :UPDATE_contactLastName, contactFirstName = :UPDATE_contactFirstName, phoneNumber = :UPDATE_phoneNumber,
                     addressLine1 = :UPDATE_addressLine1, addressLine2 = :UPDATE_addressLine2, city = :UPDATE_city, contactState = :UPDATE_contactState,
                     postalCode = :UPDATE_postalCode, email = :UPDATE_email, specialDeliveryInst = :UPDATE_specialDeliveryInst
                 WHERE customerID = :UPDATE_customerID


-- !***********************************************************************************************!
-- !****************************************** EMPLOYEES ******************************************!
-- !***********************************************************************************************!
-- Add new employee (/employeeAdd):
INSERT INTO Employees (employeeLastName, employeeFirstName, phoneNumber, addressLine1, addressLine2, city, employeeState, postalCode, email, employeeStatus) 
    VALUES (:CREATE_employeeLastName, :CREATE_employeeFirstName, :CREATE_phoneNumber, :CREATE_addressLine1, :CREATE_addressLine2, :CREATE_city, 
            :CREATE_employeeState, :CREATE_postalCode, :CREATE_email, :CREATE_employeeStatus)

-- Look-up employees with the provided information (/employeeLookUp):
SELECT * FROM Employees WHERE employeeLastName = :READ_employeeLastName AND employeeFirstName = :READ_employeeFirstName AND phoneNumber = :READ_phoneNumber AND addressLine1 = :READ_addressLine1 AND
                              addressLine2 = :READ_addressLine2 AND city = :READ_city AND employeeState = :READ_employeeState AND postalCode = :READ_postalCode AND email = :READ_email AND
                              employeeStatus = :READ_employeeStatus

-- Look-up all employees (/employeeListAll):
SELECT * FROM Employees

-- Update specific employee information (/employeeUpdate):
UPDATE Employees SET employeeLastName = :UPDATE_employeeLastName, employeeFirstName = :UPDATE_employeeFirstName, phoneNumber = :UPDATE_phoneNumber, addressLine1 = :UPDATE_addressLine1,
                     addressLine2 = :UPDATE_addressLine2, city = :UPDATE_city, employeeState = :UPDATE_employeeState, postalCode = :UPDATE_postalCode, email = :UPDATE_email,
                     employeeStatus = :UPDATE_employeeStatus
                 WHERE employeeID = :UPDATE_employeeID


-- !***********************************************************************************************!
-- !******************************************* PRODUCTS ******************************************!
-- !***********************************************************************************************!

-- Add new product (/productAdd):
INSERT INTO Products (productName, productDescription, legacyProduct)
    VALUES (:CREATE_productName, :CREATE_productDescription, :CREATE_productLegacy)

-- Look-up products with the provided information (/productLookUp):
SELECT * FROM Products WHERE productName = :READ_productName AND productDescription = :READ_productDescription AND legacyProduct = :READ_productLegacy

-- Update specific product information (/productUpdate):
UPDATE Products SET productName = :UPDATE_productName, productDescription = :UPDATE_productDescription, legacyProduct = :UPDATE_productLegacy
                WHERE productCode = :UPDATE_productCode

-- Product Report (Lists total quantity purchased for each active product):
SELECT Products.productName, SUM(IFNULL(OrderDetails.quantityOrdered,0)) AS qty FROM OrderDetails RIGHT JOIN Products ON Products.productCode = OrderDetails.productCode WHERE Products.legacyProduct = 'active' GROUP BY Products.productName ORDER BY qty DESC


-- !***********************************************************************************************!
-- !******************************************* ORDERS ********************************************!
-- !***********************************************************************************************!

-- Add new order (/orderAdd):
INSERT INTO Orders (orderDate, requiredDate, shippedDate, orderStatus, comments, customerID, employeeID) 
    VALUES (:CREATE_orderDate, :CREATE_requiredDate, :CREATE_shippedDate, :CREATE_orderStatus, :CREATE_comments, :CREATE_customerID, :CREATE_employeeID)

-- Look-up orders with the provided information (/orderLookUp): (DATE_FORMAT not used here since this is in the .html page)
SELECT orderNumber, orderDate, requiredDate, shippedDate, orderStatus, comments, contactFirstName, contactLastName, employeeFirstName, employeeLastName FROM Orders 
    INNER JOIN Customers ON Customers.customerID = Orders.customerID
    LEFT JOIN Employees ON Employees.employeeID = Orders.employeeID
    WHERE Orders.orderNumber = :READ_orderNumber AND Orders.orderDate = :READ_orderDate AND Orders.requiredDate = :READ_requiredDate AND Orders.shippedDate = :READ_shippedDATE AND Orders.orderStatus = :READ_orderStatus AND Orders.comments = :READ_comments AND Orders.customerID = :READ_customerID AND Orders.employeeID = :READ_employeeID
    ORDER BY orderNumber

-- Look-up all Orders (/orderListAll):
SELECT orderNumber, DATE_FORMAT(orderDate, '%Y-%m-%d') AS orderDate, DATE_FORMAT(requiredDate, '%Y-%m-%d') AS requiredDate, DATE_FORMAT(shippedDate, '%Y-%m-%d') AS shippedDate, orderStatus, comments, contactFirstName, contactLastName, employeeFirstName, employeeLastName FROM Orders
    INNER JOIN Customers ON Customers.customerID = Orders.customerID
    LEFT JOIN Employees ON Employees.employeeID = Orders.employeeID
    ORDER BY orderNumber

-- Update specific order information (/orderUpdate):
UPDATE Orders SET orderDate = :UPDATE_orderDate, requiredDate = :UPDATE_requiredDate, shippedDate = :UPDATE_shippedDate, orderStatus = :UPDATE_orderStatus, comments = :UPDATE_comments, customerID = :UPDATE_customer, employeeID = :UPDATE_employeeID WHERE orderNumber = :UPDATE_orderNumber

-- Customer foreign key drop down (/customerDropDown):
SELECT customerID, contactFirstName, contactLastName, email FROM Customers

-- Employee foreign key drop down (/employeeDropDown):
SELECT employeeID, employeeFirstName, employeeLastName, email FROM Employees

-- !***********************************************************************************************!
-- !**************************************** ORDER DETAILS ****************************************!
-- !***********************************************************************************************!

-- Add new orderDetails (/orderDetailsAdd):
INSERT INTO OrderDetails (orderNumber, productCode, quantityOrdered) 
    VALUES (:CREATE_orderNumber, :CREATE_productCode, :CREATE_quantityOrdered)

-- Look-up orderDetails with the provided information (/orderDetailsLookUp):
SELECT orderNumber, productName, quantityOrdered FROM OrderDetails
    INNER JOIN Products on Products.productCode = OrderDetails.productCode
    WHERE OrderDetails.orderNumber = :READ_orderNumber AND OrderDetails.productCode = :READ_productCode AND OrderDetails.quantityOrdered = :READ_quantityOrdered
    ORDER BY orderNumber, productName

-- Look-up all OrderDetails (/orderDetailsListAll):
SELECT orderNumber, productName, quantityOrdered FROM OrderDetails
    INNER JOIN Products on Products.productCode = OrderDetails.productCode
    ORDER BY orderNumber, productName

-- Update specific orderDetails information (/orderDetailsUpdate):
UPDATE OrderDetails SET quantityOrdered = :UPDATE_quantityOrdered WHERE orderNumber = :UPDATE_orderNumber AND productCode = :UPDATE_productCode

-- Delete an orderDetails:
DELETE FROM OrderDetails WHERE orderNumber = :UPDATE_orderNumber AND productCode = :UPDATE_productCode

-- Product foreign key drop down (/productDropdown):
SELECT productCode, productName FROM Products