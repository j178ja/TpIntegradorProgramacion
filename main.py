

from Funciones.MostrarTodo import  mostrar_datos
from Funciones.AgregarPais import agregar_pais
from Funciones.EliminarElemento import eliminar_pais
from Funciones.ActualizarDatos import actualizar_pais
from Funciones.BuscarPorParametro import filtrar_paises
from Funciones.BuscarPorParametro import buscar_pais
from Funciones.MostrarEstadisticas import mostrar_estadisticas
from Funciones.MostrarVideo import ver_video
from Funciones.LimpiezaPantalla import limpiar_pantalla


# MENU PRINCIPAL DE LA APLICACIÓN

def mostrar_menu():
    """Muestra el menu principal de la aplicacion"""
    print("")
    print("=== MENU PRINCIPAL ===")
    
    print("1. Mostrar listado completo de Paices")
    print("2. Agregar un pais")
    print("3. Eliminar un Pais")
    print("4. Actualizar los datos de Poblacion y Superfice de un Pais")
    print("5. Buscar un pais por nombre (coincidencia parcial o exacta).")
    print("6. Filtrar paises.")
    print("7. Mostrar estadisticas.")
    print("8. Video tutorial.")
    print("0. Salir.")
    
def ejecutar_opcion(opcion):
    """Llama a la funcion correspondiente segun opcion ingresada"""
    if opcion == '1':
        mostrar_datos()

    elif opcion == '2':
       agregar_pais()

    elif opcion == '3':
        eliminar_pais()

    elif opcion == '4':
        actualizar_pais()

    elif opcion == '5':
        buscar_pais()

    elif opcion == '6':
         filtrar_paises()

    elif opcion == '7':
       mostrar_estadisticas()

    elif opcion == '8':
       ver_video()

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