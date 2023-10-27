--8.Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.fullname, sub.name, ROUND(AVG(g.grade), 2) as avg_g
FROM grades as g
LEFT JOIN
	subjects as sub on g.subject_id = sub.id,
	teachers as t on t.id = sub.teacher_id 
WHERE t.id == 1
GROUP BY sub.name 
ORDER BY avg_g DESC;