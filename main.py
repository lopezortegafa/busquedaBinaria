from busqueda_binaria import busqueda_binaria, obtener_arreglo

def main():
    arreglo = obtener_arreglo()
    elemento = float(input("Ingrese el elemento a buscar: "))
    resultado = busqueda_binaria(arreglo, elemento)
    if resultado != -1:
        print(f"El elemento {elemento} se encuentra en la posición {resultado}.")
    else:
        print(f"El elemento {elemento} no se encuentra en el arreglo.")

if __name__ == "__main__":
    main()
