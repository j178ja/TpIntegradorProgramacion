
import pandas as pd       # Libreria para manejo de datos
from tabulate import tabulate # Libreria para mostrar tablas

def mostrar_datos():
    try:
        # Lee el archivo CSV
        df = pd.read_csv("DB/Datos.csv",  encoding="utf-8") #ruta absoluta del archivo CSV
        # Muestra todo el contenido como tabla
      #  print(df.to_string(index=False))    #muestra la tabla sin la estructura de lineas separadoras
        print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))  #muestra la tabla con lineas separadoras
    except FileNotFoundError:
        print("Error: No se encontro el archivo 'Datos.csv'")
    except Exception as e:
        print(f"Ocurrio un error: {e}")

# Llamada a la función
if __name__ == "__main__":  #sin esta linea se llama solo con la importacion por lo que se muestra aunque no se seleccione la opcion
    mostrar_datos()
