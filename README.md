Al tener solo dos clases, el algoritmo usa pocos datos de entrada.
Encuentra un dato que permite diferenciar entre ventana y no ventana y lo usa de forma exclusiva en la función.

En nuestro caso. El elemento Ba(bario) se encuentra mucho más en cristales de ventana que en cristales de no ventana.
El algoritmo detecta esto y usa este factor para calcular si es ventaan o no venatana, ignorando el resto de parámetros.

Para obtener una función que use todos los parámetros deberíamos tener más tipos a clasificar.
En nuestro caso los tipos pueden ser los siguientes:

Type of glass: (class attribute)

- 1 buildingwindowsfloatprocessed
- 2 buildingwindowsnonfloatprocessed
- 3 vehiclewindowsfloatprocessed
- 4 vehiclewindowsnonfloatprocessed (none in this database)
- 5 containers
- 6 tableware
- 7 headlamps

// TODO:

- Guardar resultados
- Hacer árbol

Usar algoritmos genéticos no es lo óptimo en clasificación pero puede ser útil para dar unos pesos iniciales en un algorítmo neuronal.

### LIBRERÍAS USADAS
Used sklearn for the f_1 score. This allows us to create multi-class confussion matrix and extract the average f-score

## BIBLIOGRAFÍA:
[Multiclass confussion matrix](https://towardsdatascience.com/confusion-matrix-for-your-multi-class-machine-learning-model-ff9aa3bf7826)

[Paper](https://link.springer.com/chapter/10.1007/978-3-662-44303-3_5)
[Classification techniques](https://www.sciencedirect.com/topics/computer-science/classification-technique)

Requirements:
- pandas
- sklearn
- matplotlib
- deap
- pygraphviz