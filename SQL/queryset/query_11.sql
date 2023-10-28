--11.Середній бал, який певний викладач ставить певному студентові.
SELECT s.fullname as student, t.fullname as teacher, ROUND(AVG(g.grade)) as average
FROM grades as g 
LEFT JOIN 
	students as s on g.student_id = s.id,
	subjects as sub on g.subject_id = sub.id,
	teachers as t on sub.teacher_id = t.id
WHERE s.id == ? and t.id == ?;