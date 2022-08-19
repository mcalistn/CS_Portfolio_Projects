DROP TABLE IF EXISTS `Customers`;

CREATE TABLE `Customers` (
    `customerID` int(5) unsigned UNIQUE NOT NULL AUTO_INCREMENT,
    `companyName` varchar(50),
    `contactFirstName` varchar(50) NOT NULL,
    `contactLastName` varchar(50) NOT NULL,
    `phoneNumber` varchar(12),
    `addressLine1` varchar(50) NOT NULL,
    `addressLine2` varchar(50),
    `city` varchar(50) NOT NULL,
    `contactState` varchar(2) NOT NULL,
    `postalCode` varchar(5) NOT NULL,
    `email` varchar(50) NOT NULL,
    `specialDeliveryInst` varchar(200),
    PRIMARY KEY (`customerID`),
    UNIQUE (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

LOCK TABLES `Customers` WRITE;
INSERT INTO `Customers` VALUES 
    (1, 'Furry Fiesta', 'Nathan', 'McAlister', '555-555-0000', '744 Belmont Pl E', 'Studio 302A', 'Seattle', 'WA', '98102', 'mcalistn@gmail.com', 'Please use the keypad code 653 to contact store clerk'),
    (2, 'Fuzzy Wuzzy Pet Store', 'Emiko', 'Nagashima', '555-555-0001', '2601 Bettle Dr', NULL, 'Seattle', 'WA', '98102', 'emi5764385@gmail.com', NULL),
    (3, NULL, 'Staci', 'Ihori', '555-555-0002', '9954 Stone St.', 'APT #302', 'Dallas', 'OR', '97338', 'ihoris@gmail.com', 'Leave outside apartment door'),
    (4, 'Pounce n Play Pet Store', 'Natasha', 'Woodruff', '555-555-0003', '4454 Jinx Cr', NULL, 'Portland', 'OR', '97035', 'iamwoodruff@yahoo.com', 'Home bussiness - leave on front porch'),
    (5, 'Pounce n Play Pet Store', 'Chris', 'Vilhauer', '555-555-0003', '4454 Jinx Cr', NULL, 'Portland', 'OR', '97035', 'iamvilhauer@yahoo.com', 'Home bussiness - leave on main house front porch'),
    (6, NULL, 'Richard', 'Alanis', '555-555-0005', '543 Blackrock Ln', NULL, 'Salem', 'OR', '97301', 'alanisr@gmail.com', NULL),
    (7, NULL, 'Ivan', 'Gomez', '555-555-0006', '3498 Center St.', 'APT #120', 'Tacoma', 'WA', '98402', 'gomeyluvpets@hotmail.com', NULL),
    (8, 'Puppy Paws Pets', 'Megan', 'Johnson', '555-555-0007', '6234 Lasas Dr.', NULL, 'Olympia', 'WA', '98501', 'iheartchris@yahoo.com', NULL),
    (9, NULL, 'Pete', 'Mitchell', '555-555-0008', '1532 Hawaii St', 'APT #451', 'Seattle', 'WA', '98102', 'maverick@gmail.com', 'Just leave on back porch'),
    (10, NULL, 'Nick', 'Bradshaw', '555-555-0009', '1532 Hawaii St', 'APT #452', 'Seattle', 'WA', '98102', 'goose@gmail.com', 'Just leave on back porch'),
    (11, NULL, 'Tom', 'Kazansky', '555-555-0010', '1532 Hawaii St', 'APT #453', 'Seattle', 'WA', '98102', 'iceman@gmail.com', NULL),
    (12, 'We Love Pets', 'John', 'Keating', '555-555-0011', '4123 Welton Cr', NULL, 'Portland', 'OR', '97035', 'ocaptain@gmail.com', 'Please deliver bewtten 11-2'),
    (13, 'Ace Pet', 'Hallie', 'Parker', '555-555-0012', '7564 Fransico St.', NULL, 'Tacoma', 'WA', '98402', 'partrap1@gmail.com', NULL),
    (14, 'Ace Pet', 'Annie', 'James', '555-555-0013', '7564 Fransico St.', NULL, 'Tacoma', 'WA', '98402', 'partrap2@gmail.com', NULL),
    (15, 'Fluffy Puppy', 'Olive', 'Breslin', '555-555-0014', '4321 Redondo Cr.', NULL, 'Eugene', 'OR', '97401', 'lilSunshine@gmail.com', 'Dont leave packages with Grandpa.'),
    (16, NULL, 'Annie', 'Walker', '555-555-0015', '5623 Milwaukee Dr.', 'APT #531', 'Corvallis', 'OR', '97330', 'bstbridesmaid@gmail.com', NULL),
    (17, 'Pet World', 'Bruce', 'Wayne', '555-555-0016', '2323 York St', 'Studio C', 'Corvallis', 'OR', '97330', 'catluver@gmail.com', 'Studio parking inbetween two buildings on right'),
    (18, NULL, 'Clark', 'Kent', '555-555-0017', '6424 Cook Dr.', 'APT #111', 'Spokane', 'WA', '99201', 'kryptonite@gmail.com', NULL),
    (19, NULL, 'Peter', 'Parker', '555-555-0018', '34123 Queens Ln.', NULL, 'Spokane', 'WA', '99201', 'redshirtguy@gmail.com', NULL);
UNLOCK TABLES;

DROP TABLE IF EXISTS `Employees`;

CREATE TABLE `Employees` (
    `employeeID` int(3) unsigned UNIQUE NOT NULL AUTO_INCREMENT,
    `employeeFirstName` varchar(50) NOT NULL,
    `employeeLastName` varchar(50) NOT NULL,
    `phoneNumber` varchar(12),
    `addressLine1` varchar(50) NOT NULL,
    `addressLine2` varchar(50),
    `city` varchar(50) NOT NULL,
    `employeeState` varchar(2) NOT NULL,
    `postalCode` varchar(5) NOT NULL,
    `email` varchar(50) NOT NULL,
    `employeeStatus` varchar(6) NOT NULL,
    PRIMARY KEY (`employeeID`),
    UNIQUE(`email`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

LOCK TABLES `Employees` WRITE;
INSERT INTO `Employees` VALUES 
    (1, 'Vincent', 'Vega', '555-555-1000', '6324 Pulp St', NULL, 'Corvallis', 'OR', '97330', 'snuggles@caninemunchies.com', 'active'),
    (2, 'Mia', 'Wallace', '555-555-2000', '9954 Fiction St.', 'APT #302', 'Dallas', 'OR', '97338', 'cuddles@caninemunchies.com', 'active'),
    (3, 'Julia', 'Winnfield', '555-555-3000', '44 Tablerock Cr', NULL, 'Corvallis', 'OR', '97330', 'smooches@caninemunchies.com', 'active'),
    (4, 'Jamie', 'Lannister', '555-555-4000', '322 Hollow Ln', 'APT #132', 'Corvallis', 'OR', '97330', 'nuzzles@caninemunchies.com', 'termed'),
    (5, 'Catelyn', 'Stark', '555-555-5000', '2222 Huckleberry Ln', NULL, 'Corvallis', 'OR', '97330', 'nestles@caninemunchies.com', 'termed');
UNLOCK TABLES;


DROP TABLE IF EXISTS `Products`;

CREATE TABLE `Products` (
    `productCode` int(3) unsigned UNIQUE NOT NULL AUTO_INCREMENT,
    `productName` varchar(50) NOT NULL,
    `productDescription` varchar(250) NOT NULL,
    `legacyProduct` boolean NOT NULL,
    PRIMARY KEY (`productCode`),
    UNIQUE(`productName`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

LOCK TABLES `Products` WRITE;
INSERT INTO `Products` VALUES 
    (1,'BaconYoMouthWater',"A perfect blend of salty and sweet, this deliciously soft treat is made with hickory-smoked bacon from pasture raised pigs, and syrup from the big-leaf maple in the Pacific Northwest. Your dog's mouth will water!", FALSE), 
    (2,'Beef Bites',"Savory, tender dog treats made with real beef and filet mignon infused with a natural smoke flavor.", FALSE),
    (3,'Bibbidi-Bobbidi-Boo',"These pumpkin biscuits are concocted with fresh organic pumpkins, roasted chickpea flour, all-natural peanut butter, and a dash of fresh ground ginger.  Bibbidi-Bobbidi-Boo's magical biscuits will leave your dog wanting more!", FALSE), 
    (4,'Canine Jerky Chips',"Our signature jerky chips are produced using USDA beef raised in the Pacific Northwest.  The all-natural beef is sliced thin to produce the crispy goodness dogs love.  These chips are a great option for dogs with food allergies.", FALSE),
    (5,'Cheese Please',"We mix barley flour, maple syrup, roasted chicken, and Tillamook cheddar cheese to create this soft chewy treat. Your dog will be cheesing after tasting these!", FALSE),
    (6,"Danner's Favorite", "Made with old-fashion rolled-oats, wheat bran, blueberries, local honey freshly harvested from the hive.  These cookies are a favorite of one of our beloved pups!", FALSE),
    (7,"Munchin' Minis","These soft, mouthwatering meatballs are made with high-quality USA sourced lamb, pea flour, maple syrup, sweet potatoes, and carrots.  Munchin' Minis will get your dog's tail moving.", FALSE),
    (8,'Nutz for Nuts!',"Calling all peanut butter lovers!  Our fresh ground peanut butter is mixed with sweet ripe bananas and old-fashioned rolled oats to create a blast of nutty goodness that your dogs will love.", FALSE), 
    (9,'Ocean Blue',"Wild Pacific King Salmon makes a splash in this treat.  Sustainably harvested in the Pacific Northwest, these fish are combined with premium sweet potatoes grown by Oregon State University Master Gardeners.", FALSE), 
    (10,'Pooch Quackers',"Dogs love the crunch of our Pooch Quackers.  These crackers are made from premium-quality oven-roasted duck combined with fresh green peas and carrots.", FALSE);
UNLOCK TABLES;


DROP TABLE IF EXISTS `Orders`;

CREATE TABLE `Orders` (
    `orderNumber` int(5) unsigned UNIQUE NOT NULL AUTO_INCREMENT,
    `orderDate` date NOT NULL,
    `requiredDate` date NOT NULL,
    `shippedDate` date NOT NULL,
    `orderStatus` varchar(9) NOT NULL,
    `comments` varchar(200),
    `customerID` int(5) unsigned NOT NULL,
    `employeeID` int(3) unsigned,
    PRIMARY KEY (`orderNumber`),
    FOREIGN KEY (`customerID`) REFERENCES Customers (`customerID`),
    FOREIGN KEY (`employeeID`) REFERENCES Employees (`employeeID`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

LOCK TABLES `Orders` WRITE;
INSERT INTO `Orders` VALUES 
    (1,'2022-02-12','2022-02-22', '2022-02-13', 'shipped', NULL, 1, NULL), 
    (2,'2022-02-12','2022-02-22', '2022-02-13', 'shipped', NULL, 2, 1),
    (3,'2022-02-12','2022-02-22', '2022-02-13', 'shipped', NULL, 3, 1),
    (4,'2022-02-12','2022-02-22', '2022-02-13', 'shipped', NULL, 4, 2),
    (5,'2022-02-12','2022-02-22', '2022-02-13', 'shipped', NULL, 5, NULL),
    (6,'2022-02-13','2022-02-23', '2022-02-14', 'shipped', NULL, 6, 3),
    (7,'2022-02-13','2022-02-23', '2022-02-14', 'shipped', NULL, 7, 4),
    (8,'2022-02-13','2022-02-23', '2022-02-14', 'shipped', NULL, 8, 5),
    (9,'2022-02-13','2022-02-23', '2022-02-14', 'shipped', NULL, 9, 5),
    (10,'2022-02-13','2022-02-23', '2022-02-14', 'cancelled', 'Cancelled per customer request on 2/15/2022.', 7, 2);
UNLOCK TABLES;


DROP TABLE IF EXISTS `OrderDetails`;

CREATE TABLE `OrderDetails` (
    `orderNumber` int(5) unsigned NOT NULL,
    `productCode` int(3) unsigned NOT NULL,
    `quantityOrdered` int(2) unsigned NOT NULL,
    PRIMARY KEY (`orderNumber`,`productCode`),
    FOREIGN KEY (`orderNumber`) REFERENCES Orders (`orderNumber`),
    FOREIGN KEY (`productCode`) REFERENCES Products (`productCode`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

LOCK TABLES `OrderDetails` WRITE;
INSERT INTO `OrderDetails` VALUES 
    (1, 1, 1), 
    (1, 2, 2), 
    (1, 5, 7),
    (2, 1, 1), 
    (3, 5, 2),
    (3, 10, 1),
    (4, 4, 4),
    (4, 8, 2),
    (5, 5, 1),
    (6, 3, 2),
    (6, 2, 1),
    (6, 8, 4),
    (7, 10, 10),
    (8, 4, 2),
    (9, 1, 5),
    (9, 3, 1),
    (9, 7, 1),
    (9, 9, 3),
    (9, 10, 1),
    (10, 10, 6);
UNLOCK TABLES;

