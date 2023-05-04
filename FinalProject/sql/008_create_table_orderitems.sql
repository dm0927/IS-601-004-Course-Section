CREATE TABLE
    IS601_Orderitemss(
        id int auto_increment PRIMARY KEY,
        product_id int,
        quantity int,
        price int,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )