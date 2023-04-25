CREATE TABLE
    IS601_CART(
        id int auto_increment PRIMARY KEY,
        customer_id int,
        product_id int,
        quantity int,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )