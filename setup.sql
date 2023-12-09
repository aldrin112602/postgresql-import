CREATE SCHEMA order_schema;

CREATE TABLE order_schema."sales" (
    order_id VARCHAR(50),
    product VARCHAR(255),
    quantity_ordered VARCHAR(255),
    price_each VARCHAR(255),
    order_date VARCHAR(255),
    purchase_address VARCHAR(500)
);

-- To allow null values
ALTER TABLE
    order_schema."sales"
ALTER COLUMN
    order_id DROP NOT NULL,
ALTER COLUMN
    product DROP NOT NULL,
ALTER COLUMN
    quantity_ordered DROP NOT NULL,
ALTER COLUMN
    price_each DROP NOT NULL,
ALTER COLUMN
    order_date DROP NOT NULL,
ALTER COLUMN
    purchase_address DROP NOT NULL;