#from decouple import config
import pyodbc

"""

SERVER = config('SQL_SERVER')
DATABASE = config('SQL_DATABASE')
USERNAME = config('SQL_USERNAME')
PASSWORD = config('SQL_PASSWORD')
DRIVER = config('SQL_DRIVER')


connectionString = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'



"""


connectionString = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=SRV009\FASTBAUART;DATABASE=BAUART;UID=sa;PWD=Flu1G$$32;MARS_Connection=yes"



def get_connection():
    print(f"Esta es la conexión: {connectionString}")
    try:
        return pyodbc.connect(connectionString, autocommit=True)  # Activa autocommit
    except pyodbc.Error as ex:
        print("Error al conectar a la base de datos:", ex)

def ejecutar_query(db, query):
    try:
        with db.cursor() as cursor:  # Usamos 'with' para cerrar el cursor automáticamente
            cursor.execute(query)
            row = cursor.fetchone()
            return print(row)
    except Exception as ex:
        print("Error al ejecutar consulta: ", ex)



