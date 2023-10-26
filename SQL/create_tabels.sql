DROP TABLE IF EXISTS [groups];
CREATE TABLE [groups] (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	name CHAR(6) UNIQUE
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	fullname VARCHAR(100)
);

DROP TABLE IF EXISTS students;
CREATE TABLE students (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	fullname VARCHAR(100),
	group_id REFERENCES [groups] (id)
);

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	name VARCHAR(255),
	teacher_id REFERENCES teachers (id)
);

DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	subject_id REFERENCES subjects (id),
	student_id REFERENCES students (id),
	grade INTEGER,
	date_of DATE
);