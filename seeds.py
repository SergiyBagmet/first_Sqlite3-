from datetime import datetime
from random import randint

from faker import Faker

from db_manager import CRUDManager, DatabaseManager




class UniverSeeder:
    def __init__(self, crud_manager: CRUDManager):
        self.crud = crud_manager
        self.fake = Faker()

    def seed_teachers(self, number_teachers):
        sql = "INSERT INTO teachers (fullname) VALUES (?)"
        teachers = [self.fake.name() for _ in range(number_teachers)]
        data_teachers = zip(teachers, )
        self.crud.execute_many_sql(sql, data_teachers)

    def seed_subjects(self, subjects, number_teachers):
        sql = "INSERT INTO subjects (name, teacher_id) VALUES (?, ?)"
        data_subjects = zip(subjects, iter(randint(1, number_teachers) for _ in range(len(subjects))))
        self.crud.execute_many_sql(sql, data_subjects)
        
    def seed_groups(self, groups):
        sql = "INSERT INTO groups (name) VALUES (?)"
        data_groups = zip(groups, )
        self.crud.execute_many_sql(sql, data_groups)
    
    def seed_students(self, groups, number_students):
        sql = "INSERT INTO students (fullname, group_id) VALUES (?, ?)"
        students = [self.fake.name() for _ in range(number_students)]
        data_students = zip(students, iter(randint(1, len(groups))for _ in range(number_students)))
        self.crud.execute_many_sql(sql, data_students)
    
    def _random_date(self) -> str:
        start_date = datetime(2023, 9, 1)  # Начало учебного года
        end_date = datetime(2024, 6, 30)  # Конец учебного года
        while True:
            fake_date : datetime = self.fake.date_between_dates(start_date, end_date)
            if fake_date.isoweekday() < 6:
                return fake_date.strftime("%Y-%m-%d")
    
    def seed_grades(self, subjects , number_students):
        sql = "INSERT INTO grades (subject_id, student_id, grade, date_of ) VALUES (?, ?, ?, ?)"
        
        grades = []
        grade_counters = {student_id: 0 for student_id in range(1, number_students + 1)}
        
        while any(count < 20 for count in grade_counters.values()):
            subject_id = randint(1, len(subjects))
            student_id = randint(1, number_students)
            grade = randint(1, 12)
            date = self._random_date()
            
            if grade_counters[student_id] < 20:
                grades.append((subject_id, student_id, grade, date))
                grade_counters[student_id] += 1
                   
        self.crud.execute_many_sql(sql, grades)

if __name__ == "__main__":
    pass
    


