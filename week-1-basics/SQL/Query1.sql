USE sql_store;
SELECT first_name , points , (points+10) *100 AS discount_factor from customers ;
SELECT name , unit_price , (unit_price) * 1.1 AS 'new price' FROM products;
SELECT * FROM customers WHERE birth_date > '1990-01-01' or points > 2000;
SELECT * FROM order_items WHERE order_id = 6 and  (quantity*unit_price) > 30 ;
SELECT * FROM customers WHERE state in ('VA','FL');
SELECT * FROM customers WHERE state NOT IN ('VA','FL');
SELECT * FROM products WHERE quantity_in_stock IN (49,38,72);
SELECT * FROM customers WHERE points BETWEEN 1000 and 3000 ;
SELECT * FROM customers WHERE  last_name LIKE 'b%';
SELECT * FROM customers WHERE  last_name LIKE '_____y' ;
SELECT * FROM customers WHERE birth_date BETWEEN '1990-01-01' and '2000-01-01' ;
SELECT * FROM customers WHERE phone IS NULL;
SELECT * FROM orders WHERE shipper_id IS NULL;
SELECT * FROM customers ORDER BY first_name;
SELECT * FROM customers ORDER BY first_name DESC;
SELECT * FROM customers ORDER BY state DESC , first_name;
SELECT * , (quantity*unit_price) AS 'Total Price' FROM order_items WHERE order_id = 2 ORDER BY 'Total Price' DESC;
SELECT * FROM customers LIMIT 3;
SELECT * FROM customers LIMIT 6 , 3;
SELECT * FROM customers ORDER BY points DESC LIMIT 3;
SELECT first_name,last_name,order_id,o.customer_id FROM orders o JOIN customers c ON o.customer_id = c.customer_id;
SELECT o.product_id , name , quantity , o.unit_price  FROM order_items o JOIN products p ON o.product_id = p.product_id;




