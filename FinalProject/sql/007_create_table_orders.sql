CREATE TABLE
    IS601_Orders(
        id int auto_increment PRIMARY KEY,
        user_id int,
        money_received int,
        total_price int,
        address TEXT,
        payment_method VARCHAR(50),
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )