use sql_store;
SELECT c.customer_id,c.first_name,o.order_id FROM customers c JOIN orders o
ON c.customer_id = o.customer_id 
ORDER BY customer_id;

-- OUTER JOIN OF ABOVE INNER JOIN
-- 	LEFT JOIN = return all from left side(Here c) , right_join = return all from right side(Here o)
-- Returns all customer columns 
SELECT c.customer_id,c.first_name,o.order_id FROM customers c LEFT JOIN orders o
ON c.customer_id = o.customer_id 
ORDER BY customer_id;
-- Returns all orders_id
SELECT c.customer_id,c.first_name,o.order_id FROM customers c   RIGHT JOIN orders o
ON c.customer_id = o.customer_id 
ORDER BY customer_id;
-- Returns all  customer_id and first_name 
SELECT c.customer_id,c.first_name,o.order_id FROM orders o  RIGHT JOIN customers c
ON c.customer_id = o.customer_id 
ORDER BY customer_id;
-- Exercise
SELECT p.product_id , p.name , oi.quantity FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id;