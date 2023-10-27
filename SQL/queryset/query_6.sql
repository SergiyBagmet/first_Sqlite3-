--6.Знайти список студентів у певній групі.
SELECT s.fullname as students, g.name as [group]
FROM students as s
LEFT JOIN [groups] as g on s.group_id = g.id 
WHERE g.id == ?
GROUP BY s.fullname;