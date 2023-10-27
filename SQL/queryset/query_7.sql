--7.Знайти оцінки студентів у окремій групі з певного предмета.
SELECT g.grade , gr.name, sub.name
FROM grades as g
LEFT JOIN  
	students as s on g.student_id = s.id, 
	subjects as sub on g.subject_id = sub.id,
	groups as gr on s.group_id = gr.id
WHERE sub.id == 1 and gr.id == 1
GROUP BY s.fullname;