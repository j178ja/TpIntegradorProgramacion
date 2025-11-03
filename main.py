# MENU PRINCIPAL DE LA APLICACIÓN

def mostrar_menu():
    """Muestra el menu principal de la aplicacion"""
    print("=== MENU PRINCIPAL ===")
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
        print("Funcionalidad para agregar un pais.")
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

salir = False
while not salir:
    """Bucle principal para mostrar reiteradamente el menu"""
    mostrar_menu()
    opcion = input("Ingresa tu opcion (1-6): ")
    salir = ejecutar_opcion(opcion) == '0'