--12.Оцінки студентів у певній групі з певного предмета на останньому занятті.
SELECT g.grade, g.date_of as [date], s.fullname as students , gr.name as [group], sub.name as subject
FROM grades as g
LEFT JOIN  
	students as s on g.student_id = s.id, 
	subjects as sub on g.subject_id = sub.id,
	groups as gr on s.group_id = gr.id
WHERE sub.id == ? and gr.id == ? 
	and g.date_of == (
					SELECT MAX(g.date_of) 
					FROM grades as g 
					WHERE g.student_id = s.id AND g.subject_id = sub.id
					)
ORDER BY [date] ASC;               