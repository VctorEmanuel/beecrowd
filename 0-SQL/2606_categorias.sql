SELECT p.id ,p.name
FROM products as p
INNER JOIN CATEGORIES as c
ON p.id_categories = c.id
WHERE c.name LIKE 'super%';