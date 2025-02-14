import pyodbc

# Configuración de la cadena de conexión
connectionString = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-M0K32LOH;"
    "DATABASE=BAUART;"
    "Trusted_Connection=yes;"
    
)

def get_connection():
    """
    Establece y retorna una conexión a la base de datos.
    """
    print(f"Conectando con: {connectionString}")
    try:
        return pyodbc.connect(connectionString)
    except pyodbc.Error as ex:
        print("Error al conectar a la base de datos:", ex)
        return None
