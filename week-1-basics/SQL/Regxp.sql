USE sql_store;
SELECT * FROM customers WHERE 	last_name REGEXP '^field';
SELECT * FROM customers WHERE 	last_name REGEXP 'field$';
SELECT * FROM customers WHERE 	last_name REGEXP 'field|mac|rose';
SELECT * FROM customers WHERE 	last_name REGEXP '[gim]e';
SELECT * FROM customers WHERE 	last_name REGEXP '[a-m]l';
SELECT * FROM customers WHERE 	first_name REGEXP 'elka|ambur';
SELECT * FROM customers WHERE 	last_name REGEXP 'EY$|ON$';
SELECT * FROM customers WHERE 	last_name REGEXP '^MY|SE';
SELECT * FROM customers WHERE 	last_name REGEXP 'b[ru]';




