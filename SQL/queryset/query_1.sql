--1.Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
SELECT s.fullname , ROUND(AVG(g.grade), 2) as avg_g
FROM grades as g
LEFT JOIN  students as s on g.student_id = s.id
GROUP BY s.fullname 
ORDER BY avg_g DESC
LIMIT 5;
