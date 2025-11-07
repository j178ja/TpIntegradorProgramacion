
import os
import pandas as pd
from tabulate import tabulate

"""Modulo para buscar y filtrar paises"""
def filtrar_paises():
    """Filtra países según continente, población o superficie"""
    ruta = os.path.join(os.path.dirname(__file__), "..", "DB", "Datos.csv")
    ruta = os.path.abspath(ruta)

    try:
        # Leer CSV con manejo de codificación
        try:
            df = pd.read_csv(ruta, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(ruta, encoding="latin-1")

        print("\n=== FILTROS DISPONIBLES ===")
        print("1. Por continente")
        print("2. Por rango de población")
        print("3. Por rango de superficie")
        print("0. Cancelar")

        opcion = input("\nSeleccione una opción de filtro: ").strip()

        if opcion == '1':
            continente = input("Ingrese el continente (ej: America, Europa, Asia...): ").strip().capitalize()
            filtrado = df[df["Continente"].str.lower() == continente.lower()]

        elif opcion == '2':
            try:
                minimo = int(input("Población mínima: "))
                maximo = int(input("Población máxima: "))
                filtrado = df[(df["Poblacion"] >= minimo) & (df["Poblacion"] <= maximo)]
            except ValueError:
                print("❌ Valores inválidos. Ingrese números enteros.")
                return

        elif opcion == '3':
            try:
                minimo = float(input("Superficie mínima: "))
                maximo = float(input("Superficie máxima: "))
                filtrado = df[(df["Superficie"] >= minimo) & (df["Superficie"] <= maximo)]
            except ValueError:
                print("❌ Valores inválidos. Ingrese números numéricos válidos.")
                return

        elif opcion == '0':
            print("Operación cancelada.")
            return
        else:
            print("Opción no válida.")
            return

        # Mostrar resultados
        if filtrado.empty:
            print("\n⚠️ No se encontraron países con ese criterio.")
        else:
            print("\n=== RESULTADOS DEL FILTRO ===")
            print(tabulate(filtrado, headers='keys', tablefmt='grid', showindex=False))

    except FileNotFoundError:
        print("Error: no se encontró el archivo Datos.csv en la carpeta DB/")
    except Exception as e:
        print(f"Ocurrió un error: {e}")



def buscar_pais():
    """Busca un país por coincidencia parcial o exacta en el archivo Datos.csv"""
    ruta = os.path.join(os.path.dirname(__file__), "..", "DB", "Datos.csv")
    ruta = os.path.abspath(ruta)

    try:
        # Leer CSV (manejo de codificación)
        try:
            df = pd.read_csv(ruta, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(ruta, encoding="latin-1")

        print("\n=== BÚSQUEDA DE PAÍSES ===")
        nombre = input("Ingrese el nombre o parte del nombre del país: ").strip()

        if not nombre:
            print("⚠️ No ingresó ningún texto.")
            return

        # Comparación insensible a mayúsculas
        filtro = df["Nombre"].str.lower().str.contains(nombre.lower(), na=False)

        resultados = df[filtro]

        if resultados.empty:
            print(f"\n❌ No se encontraron países que coincidan con '{nombre}'.")
        else:
            print(f"\n✅ Resultados de búsqueda para '{nombre}':")
            print(tabulate(resultados, headers='keys', tablefmt='grid', showindex=False))

    except FileNotFoundError:
        print("Error: no se encontró el archivo Datos.csv en la carpeta DB/")
    except Exception as e:
        print(f"Ocurrió un error: {e}")