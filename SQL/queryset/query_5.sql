--5.Знайти які курси читає певний викладач.
SELECT t.fullname, sub.name
FROM subjects as sub
LEFT JOIN teachers as t on t.id = sub.teacher_id 
WHERE  t.id == 5;