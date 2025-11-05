
import os
import pandas as pd
from tabulate import tabulate

def actualizar_pais():
    """Actualiza la población y superficie de un país existente en Datos.csv"""
    ruta = os.path.join(os.path.dirname(__file__), "..", "DB", "Datos.csv")
    ruta = os.path.abspath(ruta)

    try:
        # Leer CSV con manejo de codificación
        try:
            df = pd.read_csv(ruta, encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(ruta, encoding="latin-1")

        # Mostrar listado actual
        print("\n=== LISTADO DE PAÍSES ===")
        print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))

        # Pedir nombre del país a modificar
        nombre = input("\nIngrese el nombre del país a actualizar: ").strip()

        # Verificar existencia
        mask = df["Nombre"].str.lower() == nombre.lower()
        if not mask.any():
            print(f"⚠️ El país '{nombre}' no se encontró en la base de datos.")
            return

        # Mostrar datos actuales
        pais_actual = df[mask].iloc[0]
        print(f"\nDatos actuales de {pais_actual['Nombre']}:")
        print(f"Población: {pais_actual['Poblacion']}")
        print(f"Superficie: {pais_actual['Superficie']}")

        # Pedir nuevos valores (permite dejar en blanco para no cambiar)
        nueva_poblacion = input("Nueva población (deje vacío para mantener actual): ").strip()
        nueva_superficie = input("Nueva superficie (deje vacío para mantener actual): ").strip()

        # Actualizar solo si se ingresó algo
        if nueva_poblacion:
            try:
                df.loc[mask, "Poblacion"] = int(nueva_poblacion)
            except ValueError:
                print("❌ Valor inválido para población. Debe ser numérico.")
                return

        if nueva_superficie:
            try:
                df.loc[mask, "Superficie"] = float(nueva_superficie)
            except ValueError:
                print("❌ Valor inválido para superficie. Debe ser numérico.")
                return

        # Guardar cambios
        df.to_csv(ruta, index=False, encoding="utf-8-sig")
        print(f"\n✅ Datos de '{nombre}' actualizados correctamente.")

        # Mostrar resultado final
        print("\n=== BASE DE DATOS ACTUALIZADA ===")
        print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))

    except FileNotFoundError:
        print("Error: no se encontró el archivo Datos.csv en la carpeta DB/")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
