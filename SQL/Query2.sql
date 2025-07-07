USE store;
SELECT * FROM order_items oi JOIN sql_inventory.products p ON oi.product_id = p.product_id;

USE sql_inventory;
SELECT * FROM store.order_items oi JOIN products p ON oi.product_id = p.product_id;

USE sql_hr;
SELECT e.employee_id,e.first_name,m.first_name as manager FROM employees e JOIN employees m ON e.reports_to = m.employee_id;



