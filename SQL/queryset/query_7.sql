--7.Знайти оцінки студентів у окремій групі з певного предмета.
SELECT g.grade as grades, s.fullname as students , gr.name as [group], sub.name as subject
FROM grades as g
LEFT JOIN  
	students as s on g.student_id = s.id, 
	subjects as sub on g.subject_id = sub.id,
	groups as gr on s.group_id = gr.id
WHERE sub.id == ? and gr.id == ?;