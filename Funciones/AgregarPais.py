import os
import pandas as pd

def agregar_pais():
    """Agrega un nuevo país al archivo Datos.csv"""
    ruta = os.path.join(os.path.dirname(__file__), "..", "DB", "Datos.csv")
    ruta = os.path.abspath(ruta)

    try:
        # Cargar el archivo existente
        try:
            df = pd.read_csv(ruta, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(ruta, encoding="latin-1")

        print("\n=== AGREGAR NUEVO PAÍS ===")
        nombre = input("Nombre del país: ").strip()
        poblacion = input("Población: ").strip()
        superficie = input("Superficie (km²): ").strip()
        continente = input("Continente: ").strip()

        # Verificar si ya existe
        if df['Nombre'].str.lower().eq(nombre.lower()).any():
            print(f" El país '{nombre}' ya existe en la base de datos.")
            return

        # Agregar nueva fila
        nuevo = pd.DataFrame([{
            "Nombre": nombre,
            "Poblacion": poblacion,
            "Superficie": superficie,
            "Continente": continente
        }])

        df = pd.concat([df, nuevo], ignore_index=True)

        # Guardar nuevamente el CSV
        df.to_csv(ruta, index=False, encoding="utf-8-sig")
        print(f" País '{nombre}' agregado correctamente.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo Datos.csv en DB/")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

