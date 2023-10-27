--2.Знайти студента із найвищим середнім балом з певного предмета.
SELECT s.fullname,sub.name, ROUND(AVG(g.grade), 2) as avg_g
FROM grades as g
LEFT JOIN  
	students as s on g.student_id = s.id, 
	subjects as sub on g.subject_id = sub.id
WHERE sub.id == 5
GROUP BY s.fullname 
ORDER BY avg_g DESC
LIMIT 1;