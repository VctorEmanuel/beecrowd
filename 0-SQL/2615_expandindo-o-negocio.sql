SELECT m.id, m.name
FROM movies as m 
left JOIN genres as g
ON g.id = m.id_genres
WHERE g.description like 'Action'