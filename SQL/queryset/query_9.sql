--9.Знайти список курсів, які відвідує студент.
SELECT sub.name as subjects, s.fullname as student
FROM grades as g
LEFT JOIN  
	students as s on g.student_id = s.id, 
	subjects as sub on g.subject_id = sub.id
WHERE s.id == ?
GROUP BY sub.name;