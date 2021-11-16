### INSTALL

---

1. Install pygraphviz on linux machine, WSL, docker or similar: 

```bash
sudo apt-get install graphviz graphviz-dev
```

Access the website if encountered any problem: [Installation guide](https://pygraphviz.github.io/documentation/latest/install.html)

2. Install all python requirements (min. python version: 3.6):

```bash
pip install -r requirements.txt
```

Requirements:
- pandas (csv loading)
- sklearn (confussion matrix and other metrics)
- matplotlib (plotting)
- deap
- pygraphviz (generating tress)


3. Execute main or experiments:

```bash
python main.py
```

### ABSTRACT

---

Usar algoritmos genéticos no es lo óptimo en clasificación pero puede ser útil para dar unos pesos iniciales en un algorítmo neuronal. Podríamos intentarlo pero necesitaríamos muchos datos para entrenarlo.

Al tener solo dos clases, el algoritmo usa pocos datos de entrada.
Encuentra un dato que permite diferenciar entre ventana y no ventana y lo usa de forma exclusiva en la función.

En nuestro caso. El elemento Ba(bario) se encuentra mucho más en cristales de ventana que en cristales de no ventana.
El algoritmo detecta esto y usa este factor para calcular si es ventaan o no venatana, ignorando el resto de parámetros.

Para obtener una función que use todos los parámetros deberíamos tener más tipos a clasificar.
En nuestro caso los tipos pueden ser los siguientes:

Type of glass:

- 1 buildingwindowsfloatprocessed
- 2 buildingwindowsnonfloatprocessed
- 3 vehiclewindowsfloatprocessed
- 4 vehiclewindowsnonfloatprocessed (none in this database)
- 5 containers
- 6 tableware
- 7 headlamps

Tipos binarios:

- Ventana
- No ventana

### PORQUE NO HEMOS USADO MULTIOBJETIVO. LO HEMOS PROBADO CON NUMEROSOS ESCENARIOS

---

No usamos multiobjetivo porque los objetivos de clasifiación son claros: Consrguir acertar el máximo núimero de etiqyetas/clases.

Otros objetivos son minimizar el número de fallos, o similares.
Todos los objetivos dependen unos de otros por lo que los valores evolucionan de la misma manera, sin aportar información al algoritmo.

Por ejemplo:

![Fitness and penalty in multiclass](https://github.com/irg1008/COMPU_Practica03/blob/7c092416cc14659fc3813953fb0876cbe01459fc/output/stats.png?raw=true)

En la imagen podemos observar dos gráficas, una con el fitness y otra con el penalty. El fitness se mide con el f-score y el penalty con el hamming loss (fracción de etiquetas mal clasificadas).

Cuando el f-score aumenta, las eiquetas son más precisas, por lo que el hamming loss es menor.
Hemos llegado a la conclusión de que todos los valores que usemos como penalización no aportan información para conseguir una mejor adaptación.

### MATRIZ DE CONFUSION

---

#### Variación de las etiquetas. Consideraciones y posible solución

Para solucionar la clasifiación fuera de los límites de la matriz, podemos usar una penalización por distancia. La distancia se calcula entre el valor predicho y el límite de clasifiación.

- Para ello necesitamos saber los límites inferiores y superiores de las etiquetas.
Estos no son más que 0 y 1 en la clasificación binaria y 1 y 7 en la clasificación multiclase.

  $min = min(ytest)$ siendo y_test el vector de etiquetas reales.
  $max = max(ytest)$

- Tras tener los valores mínimos y máximos, podemos calcular la distancia entre el valor predicho y el intervalo [min, max].

  $distancia = abs(ypred - min) + abs(ypred - max)$

Si aplicamos una penalización por distancia, e intentamos disminuir la misma, el algoritmo eliminará etiquetas que se alejen de los valores válidos.

El problema que encontramos esque al hacer esto, es que convergemos mucho más rápido. Lo cual no es necesariamente malo, pero si previene encontrar soluciones mejores en el espacio de búsqueda. Aquellas en las que algunos de los valores se alejen de los límites pero se genere mayor adoptación con el resto de valores.

Esto es muy posible porque en la composición de los cristales, el papel que diferencia entre un tipo u otro es principalmente un material en concreto. En el caso de ventana o no ventana, el papel diferenciador lo tiene el Bario (Ba).

Podemos ver una matriz de confusión sin penalización a continuación:
![Sin usar penalización, observamos valores fuera del rango de las clases](https://github.com/irg1008/COMPU_Practica03/blob/ebec6080f3728ee63ecfdbdf76a829e4e70b0998/output/conf_mat.png?raw=true)

Y otra con penalización:
![Uso de penalización para evitar etiquetas "out of bounds"](https://github.com/irg1008/COMPU_Practica03/blob/6bdd291e88ce4e0425c4e9820789e5f9c480bdc1/output/conf_mat.png?raw=true)

### POSIBLES MEJORAS

---

- Crear operadores adicionales
- Cambiar la clasificación a distancia de binarios o algo así. Por eso venía en binarios.
- Minimizar el árbol y eliminar ramas innecesarias usando Orthogonal least squares (OSL)

  No hemos implementado Orthogonal least squares (OLS), ya que aumenta el tiempo de ejecución y no merece la pena la mejora.

### LIBRERÍAS USADAS

---

Used sklearn for the f_1 score. This allows us to create multi-class confussion matrix and extract the average f-score

## BIBLIOGRAFÍA

---

[Multiclass confussion matrix](https://towardsdatascience.com/confusion-matrix-for-your-multi-class-machine-learning-model-ff9aa3bf7826)

[Paper](https://link.springer.com/chapter/10.1007/978-3-662-44303-3_5)
[Classification techniques](https://www.sciencedirect.com/topics/computer-science/classification-technique)
[Glass Composition](https://www.britannica.com/technology/glass)
[Binary method](https://ieeexplore.ieee.org/document/6597232)