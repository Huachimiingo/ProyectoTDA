from db.conexion import DAO
from funciones import *
from login import *

dao = DAO()

def menuGeneral():
    while True:
        print("\nBienvenido al sistema de gestión médica")
        print("1. Iniciar sesión en el sistema")
        print("2. Manual de instrucciones")
        print("3. Términos y condiciones del sistema")
        print("4. Salir del sistema")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            menuLogin()
        elif opcion == "2":
            mostrar_manual()
        elif opcion == "3":
            mostrar_terminos()
        elif opcion == "4":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def menuLogin():
    print("Bienvenido al sistema")
    while True:
        print("\n--- Login ---")
        usuario = input("Usuario (RUT): ")
        contrasena = input("Contraseña: ")
        
        tipo_usuario = verificar_credenciales(usuario, contrasena)
        
        if tipo_usuario == "admin":
            print("Bienvenido, Administrador")
            menuAdmin()
            break
        elif tipo_usuario == "medico":
            print(f"Bienvenido, Dr./Dra. {usuario}")
            menuMedico()
            break
        else:
            print("Credenciales incorrectas. Intente nuevamente.")


def menuMedico():
    print('\nMenú Médico')
    while True:
        print('''\nSeleccione una opción:
            1.- Crear ficha médica
            2.- Buscar fichas médicas de paciente
            3.- Salir''')
        opcion = input('>>> ')
        if opcion == '1':
            try:
                print('Ingrese los siguientes datos para la ficha médica:')
                rut_paciente = input('RUT del paciente: ')
                fecha_consulta = input('Fecha de consulta (YYYY-MM-DD): ')
                diagnostico = input('Diagnóstico: ')
                tratamiento = input('Tratamiento: ')
                crear_ficha_medica(rut_paciente, fecha_consulta, diagnostico, tratamiento)
            except Exception as e:
                print(f"Error inesperado: {e}")
        elif opcion == '2':
            rut_paciente = input('Ingrese el RUT del paciente: ')
            buscar_fichas_medicas(rut_paciente)
        elif opcion == '3':
            print('Saliendo del menú médico...')
            break
        else:
            print('Opción inválida')

def menuAdmin():
    print('\nMenu administrador')
    while True:
        print('''\nSeleccione una opción:
            1.- Administrar medico
            2.- Administrar bodega
            3.- Administrar examenes
            4.- Administrar especialidades
            5.- Salir''')
        opcion = input('>>> ')
        if opcion == '1':
            while True:
                print('''Seleccione una opción:
                    1.- Crear médico
                    2.- Ver médicos
                    3.- Actualizar médico
                    4.- Eliminar médico
                    5.- Volver''')
                x = input('>>> ')
                if x == '1':
                    try:
                        print('Ingrese los siguientes datos del médico:')
                        rut_medico = input('RUT: ')
                        nombre_medico = input('Nombre: ')
                        apellido_medico = input('Apellido: ')
                        id_especialidad = input('ID de especialidad: ')
                        crear_usuario_medico(rut_medico, nombre_medico, apellido_medico, id_especialidad)
                    except Exception:
                        print(f"Error inesperado:")
                elif x == '2':
                    print('\nLista de médicos: ')
                    leer_usuarios_medicos()
                elif x == '3':
                    rut_medico = input('Ingrese el RUT del médico: ')
                    print('Ingrese los siguientes datos a modificar: ')
                    print('(Dejar en blanco los espacios que no se modificarán)')
                    nuevo_nombre = input('Nombre: ')
                    nuevo_apellido = input('Apellido: ')
                    nueva_especialidad = input('Id de especialidad: ')
                    actualizar_usuario_medico(rut_medico, nuevo_nombre if nuevo_nombre else None, nuevo_apellido if nuevo_apellido else None, nueva_especialidad if nueva_especialidad else None)
                elif x == '4':
                    print('Ingrese el RUT del médico a eliminar')
                    rut_medico = input('>>> ')
                    eliminar_usuario_medico(rut_medico)
                elif x == '5':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opcion inválida')
        elif opcion == '2':
            while True:
                print('''Seleccione una opción:
                    1.- Agregar producto
                    2.- Ver productos
                    3.- Modificar stock
                    4.- Eliminar producto
                    5.- Volver''')
                x = input('>>> ')
                if x == '1':
                    try:
                        print('Ingrese los siguientes datos del producto:')
                        id_producto = input('ID del producto: ')
                        nombre_producto = input('Nombre del producto: ')
                        cantidad = input('Cantidad: ')
                        precio_producto = input('Valor del producto: ')
                        crear_producto(id_producto, nombre_producto, cantidad, precio_producto)
                    except Exception:
                        print(f"Error inesperado:")
                elif x == '2':
                    print('\nLista de productos: ')
                    leer_productos()
                elif x == '3':
                    try:
                        id_producto = input('Ingrese el ID del producto: ')
                        print('Ingrese los siguientes datos a modificar: ')
                        print('(Dejar en blanco los espacios que no se modificarán)')
                        nuevo_nombre = input('Nombre del producto: ')
                        nueva_cantidad = input('Cantidad: ')
                        nuevo_precio = input('Nuevo valor del producto: ')
                        actualizar_producto(id_producto, nuevo_nombre if nuevo_nombre else None, nueva_cantidad if nueva_cantidad else None, nuevo_precio if nuevo_precio else None)
                    except Exception:
                        print(f"Error inesperado:")
                elif x == '4':
                    print('Ingrese el ID del producto a eliminar')
                    id_producto = input('>>> ')
                    eliminar_producto(id_producto)
                elif x == '5':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opcion inválida')
        elif opcion == '3':
            while True:
                print('''\nSeleccione una opción:
                1.- Crear examen
                2.- Ver exámenes
                3.- Actualizar examen
                4.- Eliminar examen
                5.- Volver''')
                x = input('>>> ')
                if x == '1':
                    try:
                        print('Ingrese los siguientes datos del examen:')
                        id_examen = input('ID del examen: ')
                        nombre_examen = input('Nombre del examen: ')
                        precio_examen = input('Valor del examen: ')
                        crear_examen(id_examen, nombre_examen, precio_examen)
                    except Exception:
                        print(f"Error inesperado:")
                if x == '2':
                    print('\nLista de exámenes: ')
                    leer_examenes()
                if x == '3':
                    try:
                        id_examen = input('Ingrese el ID del examen: ')
                        print('Ingrese los siguientes datos a modificar: ')
                        print('(Dejar en blanco los espacios que no se modificarán)')
                        nuevo_nombre = input('Nuevo nombre del examen: ')
                        nuevo_precio = input('Nuevo valor del examen: ')
                        actualizar_examen(id_examen, nuevo_nombre if nuevo_nombre else None, nuevo_precio if nuevo_precio else None)
                    except Exception:
                        print(f"Error inesperado:")
                if x == '4':
                    print('Ingrese el ID del examen a eliminar')
                    id_examen = input('>>> ')
                    eliminar_examen(id_examen)
                elif x == '5':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opcion inválida')
        elif opcion == '4':
            while True:
                print('''\nSeleccione una opción:
                    1.- Crear especialidad
                    2.- Ver especialidades
                    3.- Actualizar especialidad
                    4.- Eliminar especialidad
                    5.- Volver''')
                x = input('>>> ')
                if x == '1':
                    print('Ingrese los siguientes datos de la especialidad: ')
                    id_especialidad = input('Asigne una ID: ')
                    nombre_especialidad = input('Nombre de la especialidad: ')
                    crear_especialidad(id_especialidad, nombre_especialidad)
                elif x == '2':
                    print('\nLista de especialidades: ')
                    leer_especialidades()
                elif x == '3':
                    try:
                        id_especialidad = input('Ingrese el ID de la especialidad: ')
                        print('Ingrese los siguientes datos a modificar: ')
                        print('(Dejar en blanco los espacios que no se modificarán)')
                        nuevo_nombre = input('Nuevo nombre de la especialidad: ')
                        actualizar_especialidad(id_especialidad, nuevo_nombre if nuevo_nombre else None)
                    except Exception:
                        print(f"Error inesperado:")
                elif x == '4':
                    print('Ingrese el ID de la especialidad')
                    id_especialidad = input('>>> ')
                    eliminar_especialidad(id_especialidad)
                elif x == '5':
                    print('Volviendo al menú principal...')
                    break
                else:
                    print('Opcion inválida')
        elif opcion == '5':
            print('Cerrando la conexión...')
            dao.close()
            print('Saliendo del programa...')
            break
        else:
            print('Ingrese una opción válida...')

menuGeneral()