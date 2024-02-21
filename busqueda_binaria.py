def busqueda_binaria(arr, elemento):
    izquierda = 0
    derecha = len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == elemento:
            return medio
        elif arr[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

def obtener_arreglo():
    arreglo = []
    n = int(input("Ingrese la cantidad de elementos del arreglo: "))
    for i in range(n):
        elemento = float(input(f"Ingrese el elemento {i + 1}: "))
        arreglo.append(elemento)
    return arreglo