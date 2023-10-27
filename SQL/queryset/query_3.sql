--3.Знайти середній бал у групах з певного предмета.
SELECT gr.name as [groups] ,sub.name as subject, ROUND(AVG(g.grade), 2) as average
FROM grades as g
LEFT JOIN  
	students as s on g.student_id = s.id, 
	subjects as sub on g.subject_id = sub.id,
	groups as gr on s.group_id = gr.id
WHERE sub.id == ?
GROUP BY gr.name
ORDER BY average DESC;