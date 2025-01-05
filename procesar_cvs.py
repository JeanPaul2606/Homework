import pandas as pd

def procesar_csv(archivo_csv: str) -> dict:
    """
    Procesa un archivo CSV para calcular estadísticas por columna:
    - Media
    - Mediana
    - Desviación estándar

    Maneja excepciones para datos faltantes o valores inválidos.

    :param archivo_csv: Ruta del archivo CSV a procesar.
    :return: Diccionario con estadísticas por columna.
    """
    try:
        # Cargar el archivo CSV
        df = pd.read_csv(archivo_csv)

        # Validar si el archivo está vacío
        if df.empty:
            raise ValueError("El archivo CSV está vacío.")

        # Calcular estadísticas
        estadisticas = {}
        for columna in df.select_dtypes(include=["number"]):  # Solo columnas numéricas
            col_data = df[columna].dropna()  # Ignorar valores faltantes
            if col_data.empty:
                estadisticas[columna] = {
                    "Media": None,
                    "Mediana": None,
                    "Desviación estándar": None,
                }
            else:
                estadisticas[columna] = {
                    "Media": col_data.mean(),
                    "Mediana": col_data.median(),
                    "Desviación estándar": col_data.std(),
                }

        return estadisticas

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_csv}' no se encontró.")
        raise
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo '{archivo_csv}' no contiene datos válidos.")
        raise
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        raise

# Ejemplo de uso
def main():
    archivo = "estructura_con_pk.csv"  # Cambiar por la ruta del archivo descargado

    try:
        resultado = procesar_csv(archivo)
        print("Estadísticas por columna:")
        for columna, stats in resultado.items():
            print(f"{columna}: {stats}")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    main()
