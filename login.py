from db.conexion import DAO
import mysql.connector

dao = DAO()

def verificar_credenciales(usuario, contrasena):
    if usuario == "admin" and contrasena == "admin123":  # Cambia esto por las credenciales reales del admin
        return "admin"
    
    # Verificar si es médico
    connection = dao.get_conn()
    cursor = dao.get_cursor()
    try:
        cursor.execute("SELECT rut_medico FROM medicos WHERE rut_medico = %s", (usuario,))
        resultado = cursor.fetchone()
        
        if resultado:
            contrasena_correcta = f"corona{usuario[:4]}"
            if contrasena == contrasena_correcta:
                return "medico"
    except mysql.connector.Error as err:
        print(f"Error al verificar credenciales: {err}")
    finally:
        cursor.close()
        connection.close()
    
    return None