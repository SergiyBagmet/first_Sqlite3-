--2.Знайти студента із найвищим середнім балом з певного предмета.
SELECT s.fullname as student, sub.name as subject, ROUND(AVG(g.grade), 2) as average
FROM grades as g
LEFT JOIN  
	students as s on g.student_id = s.id, 
	subjects as sub on g.subject_id = sub.id
WHERE sub.id == ?
GROUP BY s.fullname 
ORDER BY average DESC
LIMIT 1;