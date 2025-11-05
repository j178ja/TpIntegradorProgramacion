import os
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt #para mostrar graficos si es necesario

def mostrar_estadisticas():
    """Muestra estadísticas generales del archivo Datos.csv"""
    ruta = os.path.join(os.path.dirname(__file__), "..", "DB", "Datos.csv")
    ruta = os.path.abspath(ruta)

    try:
        # Leer CSV con manejo de codificación
        try:
            df = pd.read_csv(ruta, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(ruta, encoding="latin-1")

        if df.empty:
            print("⚠️ No hay datos en la base de datos.")
            return

        print("\n=== ESTADÍSTICAS GENERALES ===")

        total_paises = len(df)
        total_poblacion = df["Poblacion"].sum()
        total_superficie = df["Superficie"].sum()

        pais_mayor_pob = df.loc[df["Poblacion"].idxmax(), "Nombre"]
        pais_menor_pob = df.loc[df["Poblacion"].idxmin(), "Nombre"]

        # Agrupar por continente
        promedio_por_continente = df.groupby("Continente")["Poblacion"].mean().reset_index()
        promedio_por_continente.rename(columns={"Poblacion": "Poblacion Promedio"}, inplace=True)

        # Mostrar resumen general
        print(f"\nCantidad total de países: {total_paises}")
        print(f"Población total: {total_poblacion:,}")
        print(f"Superficie total: {total_superficie:,} km²")
        print(f"País con mayor población: {pais_mayor_pob}")
        print(f"País con menor población: {pais_menor_pob}")

        # Mostrar promedio por continente
        print("\n=== Población promedio por continente ===")
        print(tabulate(promedio_por_continente, headers='keys', tablefmt='grid', showindex=False))

        plt.bar(promedio_por_continente["Continente"], promedio_por_continente["Poblacion Promedio"])
        plt.title("Población promedio por continente")
        plt.xlabel("Continente")
        plt.ylabel("Población promedio")
        plt.tight_layout()
        plt.show()


    except FileNotFoundError:
        print("Error: no se encontró el archivo Datos.csv en la carpeta DB/")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

