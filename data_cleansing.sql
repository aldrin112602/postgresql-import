-- first remove null values
DELETE FROM
    order_schema."sales"
WHERE
    order_id IS NULL
    AND product IS NULL
    AND quantity_ordered IS NULL
    AND price_each IS NULL
    AND order_date IS NULL
    AND purchase_address IS NULL;

-- Remove duplicate rows, keeping only the one with the lowest order_id
DELETE FROM
    order_schema."sales"
WHERE
    (
        order_id,
        product,
        quantity_ordered,
        price_each,
        order_date,
        purchase_address
    ) IN (
        SELECT
            order_id,
            product,
            quantity_ordered,
            price_each,
            order_date,
            purchase_address
        FROM
            (
                SELECT
                    order_id,
                    product,
                    quantity_ordered,
                    price_each,
                    order_date,
                    purchase_address,
                    ROW_NUMBER() OVER (
                        PARTITION BY order_id
                        ORDER BY
                            order_id
                    ) AS row_num
                FROM
                    order_schema."sales"
            ) AS subquery
        WHERE
            row_num > 1
    );

-- Standardize text data in product column to lowercase
UPDATE
    order_schema."sales"
SET
    product = LOWER(product);

-- Replace missing values 
UPDATE
    order_schema."sales"
SET
    quantity_ordered = COALESCE(quantity_ordered, '0'),
    price_each = COALESCE(price_each, '0'),
    purchase_address = COALESCE(purchase_address, 'No address');