--10.Список курсів, які певному студенту читає певний викладач
SELECT sub.name as subjects, s.fullname as student, t.fullname as teacher
FROM grades as g
LEFT JOIN  
	students as s on g.student_id = s.id, 
	subjects as sub on g.subject_id = sub.id,
	teachers as t on t.id = sub.teacher_id
WHERE s.id == 1 and t.id == 1
GROUP BY sub.name;