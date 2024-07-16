from decouple import config
import pyodbc

SERVER = config('SQL_SERVER')
DATABASE = config('SQL_DATABASE')
USERNAME = config('SQL_USERNAME')
PASSWORD = config('SQL_PASSWORD')
DRIVER = config('SQL_DRIVER')

connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'



def get_connection():
    print(f"Esta es la conexcion {connectionString}")
    try:
        return pyodbc.connect(connectionString)
    except pyodbc.Error as ex:
        print("Error al conectar a la base de datos:", ex)

def ejecutar_query(db,query):
    try:
        cursor = db.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        return print(row)
    except Exception as ex:
        print("Error al ejecutar consulta: ", ex)




