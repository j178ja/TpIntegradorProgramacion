import os
import pandas as pd
from tabulate import tabulate

def eliminar_pais():
    """Elimina un país y sus datos del archivo Datos.csv"""
    ruta = os.path.join(os.path.dirname(__file__), "..", "DB", "Datos.csv")
    ruta = os.path.abspath(ruta)

    try:
        # Leer CSV
        try:
            df = pd.read_csv(ruta, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(ruta, encoding="latin-1")

        # Mostrar contenido actual
        print("\n=== LISTADO ACTUAL DE PAÍSES ===")
        print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))

        # Pedir nombre
        nombre = input("\nIngrese el nombre del país a eliminar: ").strip()

        if nombre == "":
            print("Operación cancelada (nombre vacío).")
            return

        # Normalizar comparación
        mask = df["Nombre"].str.lower() != nombre.lower()

        # Verificar si existe
        if mask.all():
            print(f"⚠️ El país '{nombre}' no se encontró en la base de datos.")
            return

        # Mostrar confirmación
        print(f"\n¿Confirma eliminar el país '{nombre}'?")
        confirmar = input("Escriba S para confirmar, cualquier otra tecla para cancelar: ").strip().lower()

        if confirmar != "s":
            print("Operación cancelada.")
            return

        # Aplicar filtro y guardar
        df_filtrado = df[mask]
        df_filtrado.to_csv(ruta, index=False, encoding="utf-8-sig")

        print(f"✅ País '{nombre}' eliminado correctamente.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo Datos.csv en DB/")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

