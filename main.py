from tabulate import tabulate

import typing as t

from db_manager import DatabaseManager, CRUDManager
from seeds import UniverSeeder

NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50

subjects = [
    "Математика",
    "Теоретична інформатика",
    "Архітектура комп'ютерів",
    "Алгоритми та структури даних",
    "Мови програмування",
    "Бази даних",
    "Інформаційні мережі",
    "Криптографія та інформаційна безпека"
]

groups = ["мт-11-3", "мм-13-1", "кн-12-2"]

def show_query(crud_manager: CRUDManager, sql_script, param: t.Iterable[t.Any]=()):
    with open(sql_script, "r", encoding="utf-8") as f:
        titel = f.readline()
        
    res = crud_manager.execute_select_from_file(sql_script, param)
    tabl = tabulate(tabular_data=res[1:], headers=res[0], tablefmt="heavy_outline")
    return f"\n{titel}\n{tabl}\n"

def main():
    database = 'university.db'
    dbm = DatabaseManager(database)
    crud_manager = CRUDManager(dbm)
    crud_manager.execute_sql_script("./SQL/create_tabels.sql")
    
    seeder = UniverSeeder(crud_manager)
    seeder.seed_teachers(NUMBER_TEACHERS)
    seeder.seed_subjects(subjects, NUMBER_TEACHERS)
    seeder.seed_groups(groups)
    seeder.seed_students(groups, NUMBER_STUDENTS)
    seeder.seed_grades(subjects, NUMBER_STUDENTS)
    
    params = [(), (1,), (1,), (), (1,), (1,), (1, 1), (1,), (24,), (1,1), (1,1), (1,1)]
    for i in range(12):
        sql_script=f"./SQL/queryset/query_{i+1}.sql"
        print(show_query(crud_manager, sql_script=sql_script, param=params[i]))
        input("press any to next >>>")
        
if __name__ == "__main__": 
    main()
    
    