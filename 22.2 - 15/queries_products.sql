-- Comments in SQL Start with dash-dash --
INSERT INTO products (name, price, can_be_returned)
VALUES ('chair', '44.00', 'f');
INSERT INTO products (name, price, can_be_returned)
VALUES ('stool', '25.99', 't');
INSERT INTO products (name, price, can_be_returned)
VALUES ('table', '124.00', 'f');
SELECT *
FROM products;
SELECT name
FROM products;
SELECT name,
    price
FROM products;
INSERT INTO products (name, price, can_be_returned)
VALUES ('nightstand', '224.78', 'f');
SELECT *
FROM products
WHERE can_be_returned = TRUE;
SELECT *
FROM products
WHERE price < 44;
SELECT *
FROM products
WHERE price BETWEEN 22.50 AND 99.99;
UPDATE products
SET price = price - 20.00;
DELETE FROM products
WHERE price < 25.00;
UPDATE products
SET can_be_returned = 't';