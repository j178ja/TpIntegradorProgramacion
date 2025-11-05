

from Funciones.MostrarTodo import  mostrar_datos

from Funciones.LimpiezaPantalla import limpiar_pantalla


# MENU PRINCIPAL DE LA APLICACIÓN

def mostrar_menu():
    """Muestra el menu principal de la aplicacion"""
    print("")
    print("=== MENU PRINCIPAL ===")
    
    print("1. Mostrar listado completo de Paices")
    print("1. Agregar un pais")
    print("2. Actualizar los datos de Poblacion y Superfice de un Pais")
    print("3. Buscar un pais por nombre (coincidencia parcial o exacta).")
    print("4. Filtrar paises.")
    print("5. Mostrar estadisticas.")
    print("6. Video tutorial.")
    print("0. Salir.")
    
def ejecutar_opcion(opcion):
    """Llama a la funcion correspondiente segun opcion ingresada"""
    if opcion == '1':
        mostrar_datos()
    elif opcion == '2':
        print("Funcionalidad para actualizar datos de poblacion y superficie.")
    elif opcion == '3':
        print("Funcionalidad para buscar un pais por nombre.")
    elif opcion == '4':
        print("Funcionalidad para filtrar paises.")
    elif opcion == '5':
        print("Funcionalidad para mostrar estadisticas.")
    elif opcion == '6':
        print("Funcionalidad para mostrar video tutorial.")
    elif opcion == '0':
        print("Saliendo de la aplicacion.")
    else:
        print("Opcion no valida. Por favor, intente de nuevo.")
    return opcion

salir = False
while not salir:
    """Bucle principal para mostrar reiteradamente el menu"""
    # limpiar_pantalla()
    mostrar_menu()   # muestra el menu de opciones
    opcion = input("\nIngresa tu opcion (1-6) o 0 para Salir: ")
    salir = ejecutar_opcion(opcion) == '0'