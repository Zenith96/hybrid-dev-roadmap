use sql_store;
-- OUTER join between multiple tables 
SELECT c.customer_id,c.first_name,o.order_id,sh.name AS shipper FROM customers c LEFT JOIN orders o
ON c.customer_id = o.customer_id 
LEFT JOIN shippers sh ON o.shipper_id = sh.shipper_id
ORDER BY customer_id;
-- EXCERCISE
SELECT o.order_date , o.order_id ,c.first_name as customer  ,  sh.name as Shipper , os.name as Status
FROM orders o JOIN customers c 
ON o.customer_id = c.customer_id 
LEFT JOIN shippers sh
ON o.shipper_id = sh.shipper_id
LEFT  JOIN order_statuses os
ON o.status = os.order_status_id;
-- Self outer joins
USE sql_hr;
SELECT e.employee_id,e.first_name,m.first_name as Manager 
FROM employees e 
LEFT JOIN employees m
ON e.reports_to = m.employee_id;
