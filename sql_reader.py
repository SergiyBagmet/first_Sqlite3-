
def get_sql_scripts(script_file):
    with open(script_file, 'r') as sql_file:
        sql_scripts = sql_file.read()
    
    return [f'{script.strip()};' for script in sql_scripts.split(";") if script.strip()]

if __name__ == "__main__":
    pass