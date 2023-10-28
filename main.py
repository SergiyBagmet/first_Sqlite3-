from tabulate import tabulate

import typing as t

from db_manager import DatabaseManager, CRUDManager



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
    params = [(), (1,), (1,), (), (1,), (1,), (1, 1), (1,), (24,), (1,1), (1,1), (1,1)]
    for i in range(12):
        sql_script=f"./SQL/queryset/query_{i+1}.sql"
        print(show_query(crud_manager, sql_script=sql_script, param=params[i]))
        input("press any to next >>>")
        
if __name__ == "__main__":
    main()
    
    