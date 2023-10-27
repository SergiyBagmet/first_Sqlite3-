--9.Знайти список курсів, які відвідує студент.
SELECT sub.name, s.fullname
FROM grades as g
LEFT JOIN  
	students as s on g.student_id = s.id, 
	subjects as sub on g.subject_id = sub.id
WHERE s.id == 24
GROUP BY sub.name;