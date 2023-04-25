CREATE TABLE
    IS601_Product(
        id int auto_increment PRIMARY KEY,
        product_name VARCHAR(100) UNIQUE,
        prodct_description TEXT,
        category VARCHAR(30),
        stock INT,
        unit_price INT,
        visibility BOOLEAN,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )