--6.Знайти список студентів у певній групі.
SELECT s.fullname, g.name 
FROM students as s
LEFT JOIN groups as g on s.group_id = g.id 
WHERE g.id == 1
GROUP BY s.fullname;