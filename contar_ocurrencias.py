def contar_ocurrencias(archivo: str) -> dict:
    """
    Lee un archivo de texto de registro (log) y cuenta la cantidad de ocurrencias de cada palabra.
    Devuelve un diccionario con las palabras como claves y sus conteos como valores.

    :param archivo: Ruta del archivo de texto de registro.
    :return: Diccionario con las palabras y sus ocurrencias.
    """
    from collections import Counter

    conteo_palabras = Counter()

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = f.readlines()

            if not lineas:
                raise ValueError("El archivo está vacío.")

            for linea in lineas:
                palabras = linea.strip().split()
                if not palabras:
                    continue  # Ignorar líneas vacías
                conteo_palabras.update(palabras)

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró.")
        raise
    except PermissionError:
        print(f"Error: No tienes permisos para leer el archivo '{archivo}'.")
        raise
    except UnicodeDecodeError:
        print(f"Error: No se pudo leer el archivo '{archivo}' debido a un problema de codificación.")
        raise
    except ValueError as ve:
        print(f"Error en el archivo: {ve}")
        raise
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        raise

    return dict(conteo_palabras)

def main():
    archivo = "registro.log"  # Cambia esto por la ruta para tu archivo log

    try:
        ocurrencias = contar_ocurrencias(archivo)
        print("Conteo de palabras:", ocurrencias)
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    main()
