--8.Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.fullname as teacher, sub.name as subjects, ROUND(AVG(g.grade), 2) as average
FROM grades as g
LEFT JOIN
	subjects as sub on g.subject_id = sub.id,
	teachers as t on t.id = sub.teacher_id 
WHERE t.id == ?
GROUP BY sub.name
ORDER BY average DESC;