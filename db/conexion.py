import mysql.connector
from mysql.connector import Error

class DAO:
    def __init__(self):
        self.conexion = None
        self.connect()

    def connect(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                database='tda'
            )
            print("Conexión a MySQL establecida")
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")

    def get_conn(self):
        if self.conexion is None or not self.conexion.is_connected():
            print("La conexión no está activa. Intentando reconectar...")
            self.connect()
        return self.conexion

    def get_cursor(self):
        try:
            return self.get_conn().cursor()
        except Error as e:
            print(f"Error al obtener el cursor: {e}")
            self.connect()
            return self.get_conn().cursor()

    def close(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")