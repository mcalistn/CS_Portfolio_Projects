/********************************************************************************************
                                        SETUP
********************************************************************************************/

// Express
let express = require('express');   // We are using the express library for the web server
let bodyParser = require("body-parser");
const path = require('path');
let app     = express();            // We need to instantiate an express object to interact with the server in our code
PORT        = 29292;                 // Set a port number at the top so it's easy to change in the future

// Database
let db = require('./db-connector')

/********************************************************************************************
                                        Routes
********************************************************************************************/
app.use(express.static(__dirname + '/public'));
app.use(express.urlencoded());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true })); 

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, '/public/index.html'));
});

app.post('/customerAdd', function(req, res) {
    const query = `INSERT INTO Customers (companyName, contactLastName, contactFirstName, phoneNumber, addressLine1, 
                    addressLine2, city, contactState, postalCode, email, specialDeliveryInst) 
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`;
    const companyName = req.body.companyName;
    const contactLastName = req.body.contactLastName;
    const contactFirstName = req.body.contactFirstName;
    const phoneNumber = req.body.phoneNumber;
    const addressLine1 = req.body.addressLine1;
    const addressLine2 = req.body.addressLine2;
    const city = req.body.city;
    const contactState = req.body.contactState;
    const postalCode = req.body.postalCode;
    const email = req.body.email;
    const specialDeliveryInst = req.body.specialDeliveryInst;
    db.pool.query(query, [companyName, contactLastName, contactFirstName, phoneNumber, addressLine1, addressLine2, city, contactState, postalCode, email, specialDeliveryInst], function(err, results){
        res.send(JSON.stringify(results))
    });
});

app.get('/customerDropDown', function(req, res) {
    const query = 'SELECT customerID, contactFirstName, contactLastName, email FROM Customers;'
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results))
    });
});

app.get('/employeeDropDown', function(req, res) {
    const query = 'SELECT employeeID, employeeFirstName, employeeLastName, email FROM Employees;'
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results))
    });
});

app.get('/productDropDown', function(req, res) {
    const query = 'SELECT productCode, productName FROM Products ORDER BY productCode asc;'
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results))
    });
});

app.get('/customerLookUp/:queryString', function(req, res) {
    const query = req.params.queryString
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results))
    });
});

app.get('/customerListAll', function(req, res) {
    query = 'SELECT * FROM Customers;';
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results))
    });
});

app.post('/customerUpdate', function(req, res) {
    const customerID = req.body.customerID;
    const companyName = req.body.companyName;
    const contactLastName = req.body.contactLastName;
    const contactFirstName = req.body.contactFirstName;
    const phoneNumber = req.body.phoneNumber;
    const addressLine1 = req.body.addressLine1;
    const addressLine2 = req.body.addressLine2;
    const city = req.body.city;
    const contactState = req.body.contactState;
    const postalCode = req.body.postalCode;
    const email = req.body.email;
    const specialDeliveryInst = req.body.specialDeliveryInst;
    const query = `UPDATE Customers SET companyName = ?, contactLastName = ?, contactFirstName = ?, 
                   phoneNumber = ?, addressLine1 = ?, addressLine2 = ?, city = ?, contactState = ?,
                   postalCode = ?, email = ?, specialDeliveryInst = ? WHERE customerID = '${customerID}'`
    db.pool.query(query, [companyName, contactLastName, contactFirstName, phoneNumber, addressLine1, addressLine2, city, contactState, postalCode, email, specialDeliveryInst], function(err, results){
        res.send(JSON.stringify(results))
    });
});

app.post('/employeeAdd', function(req, res) {
    const query = `INSERT INTO Employees (employeeLastName, employeeFirstName, phoneNumber, addressLine1, addressLine2, 
                    city, employeeState, postalCode, email, employeeStatus) 
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`;
    const employeeLastName = req.body.employeeLastName;
    const employeeFirstName = req.body.employeeFirstName;
    const phoneNumber = req.body.phoneNumber;
    const addressLine1 = req.body.addressLine1;
    const addressLine2 = req.body.addressLine2;
    const city = req.body.city;
    const employeeState = req.body.employeeState;
    const postalCode = req.body.postalCode;
    const email = req.body.email;
    const employeeStatus = req.body.employeeStatus;
    db.pool.query(query, [employeeLastName, employeeFirstName, phoneNumber, addressLine1, addressLine2, city, employeeState, postalCode, email, employeeStatus], function(err, results){
        res.send(JSON.stringify(results))
    });
});

app.get('/employeeLookUp/:queryString', function(req, res) {
    const query = req.params.queryString
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results))
    });
});

app.get('/employeeListAll', function(req, res) {
    query = 'SELECT * FROM Employees;';
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results));
    });
});

app.post('/employeeUpdate', function(req, res) {
    const employeeID = req.body.employeeID;    
    const employeeLastName = req.body.employeeLastName;
    const employeeFirstName = req.body.employeeFirstName;
    const phoneNumber = req.body.phoneNumber;
    const addressLine1 = req.body.addressLine1;
    const addressLine2 = req.body.addressLine2;
    const city = req.body.city;
    const employeeState = req.body.employeeState;
    const postalCode = req.body.postalCode;
    const email = req.body.email;
    const employeeStatus = req.body.employeeStatus;
    const query = `UPDATE Employees SET employeeLastName = ?, employeeFirstName = ?, phoneNumber = ?, addressLine1 = ?, addressLine2 = ?, 
                   city = ?, employeeState = ?, postalCode = ?, email = ?, employeeStatus = ? WHERE employeeID = '${employeeID}'`
    db.pool.query(query, [employeeLastName, employeeFirstName, phoneNumber, addressLine1, addressLine2, city, employeeState, postalCode, email, employeeStatus], function(err, results){
        res.send(JSON.stringify(results))
    });
});

app.post('/orderDetailsAdd', function(req,res) {
    const query = `INSERT INTO OrderDetails (orderNumber, productCode, quantityOrdered) 
                   VALUES (?, ?, ?)`;
    const orderNumber = req.body.orderNumber;
    const productCode = req.body.productCode;
    const quantityOrdered = req.body.quantityOrdered;
    db.pool.query(query, [orderNumber, productCode, quantityOrdered], function(err, results){
        res.send(JSON.stringify(results))
    });                   
});

app.get('/orderDetailsLookUp/:queryString', function(req, res) {
    const query = req.params.queryString
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results))
    });
});

app.get('/orderDetailsListAll', function(req, res) {
    query = 'SELECT orderNumber, productName, quantityOrdered FROM OrderDetails INNER JOIN Products on Products.productCode = OrderDetails.productCode ORDER BY orderNumber, productName;';
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results));
    });
});

app.post('/orderDetailsUpdate', function(req, res) {   
    const orderNumber = req.body.orderNumber;
    const productCode = req.body.productCode;
    const quantityOrdered = req.body.quantityOrdered;
    const query = `UPDATE OrderDetails SET quantityOrdered = '${quantityOrdered}' WHERE orderNumber = '${orderNumber}' AND productCode = '${productCode}'`
    db.pool.query(query, function(err, results){
        res.send(JSON.stringify(results))
    });
});

app.delete('/orderDetailsDelete', function(req, res) {   
    const orderNumber = req.body.orderNumber;
    const productCode = req.body.productCode; 
    query = 'DELETE FROM OrderDetails WHERE orderNumber = ' + orderNumber + ' AND productCode = ' + productCode + ';'
    db.pool.query(query, function(err, results){
        res.send(JSON.stringify(results))
    });
});

app.post('/orderAdd', function(req,res) {
    const query = `INSERT INTO Orders (orderDate, requiredDate, shippedDate, orderStatus, comments, customerID, employeeID) 
                   VALUES (?, ?, ?, ?, ?, ?, ?)`;
    const orderDate = req.body.orderDate;
    const requiredDate = req.body.requiredDate;
    const shippedDate = req.body.shippedDate;
    const orderStatus = req.body.orderStatus;
    const comments = req.body.comments;
    const customerID = req.body.customerID;
    const employeeID = req.body.employeeID;
    db.pool.query(query, [orderDate, requiredDate, shippedDate, orderStatus, comments, customerID, employeeID], function(err, results){
        res.send(JSON.stringify(results))
    });                   
});

app.get('/orderLookUp/:queryString', function(req, res) {
    const query = req.params.queryString
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results))
    });
});
    
app.get('/orderListAll', function(req, res) {
    query = `SELECT orderNumber, DATE_FORMAT(orderDate, '%Y-%m-%d') AS orderDate, DATE_FORMAT(requiredDate, '%Y-%m-%d') AS requiredDate, DATE_FORMAT(shippedDate, '%Y-%m-%d') AS shippedDate, orderStatus, comments, contactFirstName, contactLastName, employeeFirstName, employeeLastName FROM Orders INNER JOIN Customers on Customers.customerID = Orders.customerID LEFT JOIN Employees on Employees.employeeID = Orders.employeeID ORDER BY orderNumber;`;
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results))
    });
});

app.post('/orderUpdate', function(req, res) {
    const orderNumber = req.body.orderNumber;
    const orderDate = req.body.orderDate;
    const requiredDate = req.body.requiredDate;
    const shippedDate = req.body.shippedDate;
    const orderStatus = req.body.orderStatus;
    const comments = req.body.comments;
    const customerID = req.body.customerID;
    const employeeID = req.body.employeeID;
    query = `UPDATE Orders SET orderDate = ?, requiredDate = ?, shippedDate = ?, orderStatus = ?, comments = ?, customerID = ?, employeeID = ? 
             WHERE orderNumber = ${orderNumber}`
    db.pool.query(query, [orderDate, requiredDate, shippedDate, orderStatus, comments, customerID, employeeID], function(err, results){
        res.send(JSON.stringify(results))
    });                   
});

app.post('/productAdd', function(req, res) {
    const query = `INSERT INTO Products (productName, productDescription, legacyProduct) 
                 VALUES (?, ?, ?)`;
    const productName = req.body.productName;
    const productDescription = req.body.productDescription;
    const legacyProduct = req.body.legacyProduct;
    db.pool.query(query, [productName, productDescription, legacyProduct], function(err, results){
        res.send(JSON.stringify(results))
    });
});

app.get('/productLookUp/:queryString', function(req, res) {
    const query = req.params.queryString
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results))
    });
});

app.get('/productListAll', function(req, res) {
    query = 'SELECT * FROM Products;';
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results));
    });
});

app.get('/productReport/:queryString', function(req, res) {
    const query = req.params.queryString
    db.pool.query(query, function(err, results, fields){
        res.send(JSON.stringify(results))
    });
});

app.post('/productUpdate', function(req, res) {
    const productCode = req.body.productCode;
    const productName = req.body.productName;
    const productDescription = req.body.productDescription;
    const legacyProduct = req.body.legacyProduct;
    const query = `UPDATE Products SET productName = ?, productDescription = ?, 
                   legacyProduct = ? WHERE productCode = ${productCode}`
    db.pool.query(query, [productName, productDescription, legacyProduct], function(err, results){
        res.send(JSON.stringify(results))
    });
});
/********************************************************************************************
                                        LISTENER
********************************************************************************************/
app.listen(PORT, function(){            // This is the basic syntax for what is called the 'listener' which receives incoming requests on the specified PORT.
    console.log('Express started on http://localhost:' + PORT + '; press Ctrl-C to terminate.')
});