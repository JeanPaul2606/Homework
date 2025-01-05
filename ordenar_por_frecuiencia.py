def ordenar_por_frecuencias(lista: list[int]) -> list[int]:
    """
    Ordena una lista de números en función de la frecuencia de aparición de cada número.
    Los números con mayor frecuencia aparecen primero. Si dos números tienen la misma frecuencia,
    se ordenan de menor a mayor.

    :param lista: Lista de números enteros.
    :return: Lista ordenada por frecuencias.
    """
    from collections import Counter

    # Validar que la lista no esté vacía
    if not lista:
        raise ValueError("La lista está vacía.")

    # Validar que todos los elementos de la lista sean enteros
    if not all(isinstance(x, int) for x in lista):
        raise ValueError("Todos los elementos de la lista deben ser números enteros.")

    # Contar las frecuencias de los números
    frecuencias = Counter(lista)

    # Ordenar por frecuencia descendente y por valor ascendente
    return sorted(lista, key=lambda x: (-frecuencias[x], x))

# Ejemplo de uso
def main():
    try:
        lista = [4, 5, 6, 5, 4, hola, 1, 4, 5, 6, 6, 6, 7, 2]  # Modificar AQUI PARA COMPILAR EL CODIGO
        resultado = ordenar_por_frecuencias(lista)
        print("Lista ordenada por frecuencias:", resultado)
    except NameError as ne:
        print(f"Error: {ne}. Asegúrate de que todos los elementos de la lista estén definidos o entre comillas.")
    except ValueError as ve:
        print(f"Error en la lista: {ve}")
    except TypeError as te:
        print(f"Error de tipo: {te}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
