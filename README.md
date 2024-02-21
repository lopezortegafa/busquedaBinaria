# Búsqueda Binaria

Este proyecto implementa el algoritmo de búsqueda binaria en Python para buscar elementos en un arreglo ordenado.

## Uso

Para utilizar este programa, ejecuta el archivo `main.py`. El programa te pedirá que ingreses la cantidad de elementos del arreglo y luego ingreses cada elemento. Después, te pedirá que ingreses el elemento que deseas buscar en el arreglo. Luego, el programa buscará el elemento utilizando el algoritmo de búsqueda binaria y te informará si el elemento se encuentra en el arreglo y en qué posición.

## Nota: Restricción sobre el tipo de datos

Este programa está diseñado para trabajar con números enteros. Si se ingresan números flotantes u otros tipos de datos, el programa puede no funcionar como se espera. Se recomienda ingresar solo números enteros al utilizar este programa.

### Ejemplo de uso:

```python main.py
Ingrese la cantidad de elementos del arreglo: 5
Ingrese el elemento 1: 3
Ingrese el elemento 2: 5
Ingrese el elemento 3: 7
Ingrese el elemento 4: 9
Ingrese el elemento 5: 11
Ingrese el elemento a buscar: 7
El elemento 7 se encuentra en la posición 2.
```

## Estructura de archivos

El proyecto consta de los siguientes archivos:

- `main.py`: Contiene la función principal (`main`) para ejecutar el programa. Importa las funciones del módulo `busqueda_binaria`.
- `busqueda_binaria.py`: Implementa la función `busqueda_binaria` que busca un elemento en un arreglo utilizando el algoritmo de búsqueda binaria.
  - `busqueda_binaria(arr, elemento)`: Realiza la búsqueda binaria del `elemento` en el arreglo `arr`.
  - `obtener_arreglo()`: Solicita al usuario los elementos del arreglo.

## Contribución

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y commitea (`git commit -am 'Agrega una nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un pull request.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto con el autor:
- Nombre: Fabián Andrés López Ortega
- Correo electrónico: lopezortega.fa@gmail.com
