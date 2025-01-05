def buscar_pares(lista: list[int], objetivo: int) -> list[tuple[int, int]]:
    """
    Dada una lista de enteros y un número objetivo, encuentra todos los pares únicos
    de números en la lista que sumen el objetivo.

    :param lista: Lista de números enteros.
    :param objetivo: Número objetivo para la suma.
    :return: Lista de pares únicos que sumen el objetivo.
    """
    pares = set()
    vistos = set()

    try:
        for num in lista:
            if not isinstance(num, int):
                raise ValueError(f"El elemento '{num}' no es un número entero.")
            complemento = objetivo - num
            if complemento in vistos:
                pares.add(tuple(sorted((num, complemento))))
            vistos.add(num)
    except NameError as ne:
        print(f"Error: {ne}. Asegúrate de que todos los elementos de la lista estén definidos o entre comillas.")
        raise
    except TypeError as e:
        print(f"Error: {e}. Asegúrate de que la lista contenga solo números enteros.")
        raise
    except ValueError as ve:
        print(f"Error en la lista: {ve}")
        raise

    return list(pares)

def main():
    try:
        lista = [2, 4, 3, 7, 5, -1, hola, 8, 6]  # MODIFICAR AQUI PARA COMPILAR
        objetivo = 9
        pares = buscar_pares(lista, objetivo)
        print("Pares que suman el objetivo:", pares)
    except Exception as e:
        print(f"Ocurrió un error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
