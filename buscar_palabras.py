def buscar_palabras(textos: list[str], palabras_clave: list[str]) -> dict:
    """
    Recibe una lista de textos largos y una lista de palabras clave. Devuelve un diccionario
    donde cada palabra clave es una clave, y el valor es una lista de índices de los textos
    donde aparece la palabra clave.

    :param textos: Lista de textos largos.
    :param palabras_clave: Lista de palabras clave a buscar.
    :return: Diccionario con palabras clave como claves y listas de índices como valores.
    """
    resultado = {}
    
    try:
        for palabra in palabras_clave:
            indices = []
            for i, texto in enumerate(textos):
                if palabra.lower() in texto.lower():  # Comparación insensible a mayúsculas
                    indices.append(i)
            resultado[palabra] = indices
    except Exception as e:
        print(f"Error al procesar los datos: {e}")
        raise

    return resultado

def main():
    try:
        textos = [
            "Este es un ejemplo de texto.",
            "Otro texto diferente con palabras clave.",
            "La búsqueda en Python es muy flexible.",
        ]
        palabras_clave = ["awd", "Python", "clave"]  # MODIFICAR EN PALABRAS_CLAVE Y TEXTOS PARA COMPILAR 

        if not all(isinstance(texto, str) for texto in textos):
            raise ValueError("Todos los elementos de la lista de textos deben ser cadenas de texto.")

        resultado = buscar_palabras(textos, palabras_clave)
        print("Resultados:", resultado)
    except NameError as ne:
        print(f"Ocurrió un error de nombre: {ne}. Asegúrate de escribir las palabras clave entre comillas.")
    except ValueError as ve:
        print(f"Ocurrió un error en los textos: {ve}")
    except Exception as e:
        print(f"Ocurrió un error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
