--3.Знайти середній бал у групах з певного предмета.
SELECT gr.name ,sub.name, ROUND(AVG(g.grade), 2) as avg_g
FROM grades as g
LEFT JOIN  
	students as s on g.student_id = s.id, 
	subjects as sub on g.subject_id = sub.id,
	groups as gr on s.group_id = gr.id
WHERE sub.id == 1
GROUP BY gr.name 
ORDER BY avg_g DESC;