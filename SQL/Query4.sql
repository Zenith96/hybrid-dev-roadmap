USE sql_store;
SELECT * FROM order_items oi
JOIN order_item_notes oin
ON oi.order_id = oin.order_id 
AND oi.product_id = oin.product_id;
-- Original Syntax(explicit)
SELECT * FROM orders o JOIN customers c ON o.customer_id = c.customer_id;
-- Implicit Join syntax
SELECT * FROM orders o , customers c WHERE o.customer_id = c.customer_id;
