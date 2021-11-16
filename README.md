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

En la imagen podemos observar dos gráficas, una con el fitness y otra con el penalty. El fitness se mide con el f-score (medida de precisión de la clasificación) y el penalty con el hamming loss (fracción de etiquetas mal clasificadas).

- El f_score es una métrica de clasificación que se calcula con la siguiente fórmula:

  $f\_score = \frac{2TP}{2TP+FP+FN}$

Cuando el f-score aumenta, las eiquetas son más precisas, por lo que el hamming loss es menor.
Hemos llegado a la conclusión de que todos los valores que usemos como penalización no aportan información para conseguir una mejor adaptación.

### MATRIZ DE CONFUSION

---

#### Variación de las etiquetas. Consideraciones y posible solución

Para solucionar la clasifiación fuera de los límites de la matriz, podemos usar una penalización por distancia. La distancia se calcula entre el valor predicho y el límite de clasifiación.

- Para ello necesitamos saber los límites inferiores y superiores de las etiquetas.
  Estos no son más que 0 y 1 en la clasificación binaria y 1 y 7 en la clasificación multiclase.

  $min = min(y\_test)$ siendo y_test el vector de etiquetas reales.
  $max = max(y\_test)$

- Tras tener los valores mínimos y máximos, podemos calcular la distancia entre el valor predicho y el intervalo [min, max].

  $distancia = abs(y\_pred - min) + abs(y\_pred - max)$

Si aplicamos una penalización por distancia, e intentamos disminuir la misma, el algoritmo eliminará etiquetas que se alejen de los valores válidos.

El problema que encontramos esque al hacer esto, es que convergemos mucho más rápido. Lo cual no es necesariamente malo, pero si previene encontrar soluciones mejores en el espacio de búsqueda. Aquellas en las que algunos de los valores se alejen de los límites pero se genere mayor adoptación con el resto de valores.

Esto es muy posible porque en la composición de los cristales, el papel que diferencia entre un tipo u otro es principalmente un material en concreto. En el caso de ventana o no ventana, el papel diferenciador lo tiene el Bario (Ba).

Podemos ver una matriz de confusión sin penalización a continuación:
![Sin usar penalización, observamos valores fuera del rango de las clases](https://github.com/irg1008/COMPU_Practica03/blob/ebec6080f3728ee63ecfdbdf76a829e4e70b0998/output/conf_mat.png?raw=true)

Y otra con penalización:
![Uso de penalización para evitar etiquetas "out of bounds"](https://github.com/irg1008/COMPU_Practica03/blob/6bdd291e88ce4e0425c4e9820789e5f9c480bdc1/output/conf_mat.png?raw=true)

### MEJOR FITNESS EN LAS CLASIFICACIONES

---

Configuración de ejecución:

- CXPB=0.5
- MUTPB=0.2
- NGEN=500
- NIND=200
- use_binary=True
- max_tree_height=10
- max_subtree_height=3,
- max_mutated_subtree_height=2

Por otro lado el máximo número de nodos generados en el árbol, es 50.

#### Clasificación binaria

El fitness por generación es el siguiente:

![Fitness en binary](https://i.imgur.com/myRhJcg.png)

El árbol generado de la mejor solución con fitness 0.9577 (95,77% de acierto) es:

![Árbol de clasificación binaria](https://i.imgur.com/1r7mfKO.png)

$protDiv(abs(sub(Mg, Fe)), add(add(protDiv(Mg, sub(Mg, Ba)), Mg), sub(sub(RI, Fe), protDiv(Fe, add(Fe, add(protDiv(protDiv(Al, sub(Ba, add(Al, Mg))), sub(abs(Al), sub(mul(Fe, K), mul(Al, Si)))), abs(protDiv(sub(Ba, add(Al, Mg)), mul(Al, Si)))))))))$

Por último la matriz de confusión es la siguiente:

![Matriz de confusión binaria](https://i.imgur.com/N3fRKKi.png)

#### Clasificación multiclase

Con los mismos parámetros de ejecución, el fitness por generación es el siguiente:
![Fitness en multiclase](https://i.imgur.com/LVzsWxQ.png)

- El mejor fitness es 0,5492 (54,92% de acierto)

Podemos observar que el fitness es mucho menor, esto es porque el algoritmo genético no es el mejor para clasificación de varias etiquetas, aun menos cuando solo tenemos 215 filas de datos en el dataset, siendo la mayoría de los datos para dos etiquetas (1 y 2) (podemos ver esto reflejado en la matriz de confusión más abajo).

Con el correspondiente árbol:

![Árbol de clasificación multiclase](https://i.imgur.com/q47PEKI.png)

La expresión de este árbol es:

$add(protDiv(Al, add(add(add(Na, Al), protDiv(Al, neg(add(mul(sub(add(Mg, Ba), protDiv(Na, Na)), add(Mg, add(Mg, Ba))), protDiv(abs(Al), abs(Na)))))), protDiv(Na, neg(add(mul(Si, protDiv(Fe, Fe)), add(mul(abs(Na), add(Mg, Fe)), Na)))))), abs(Al))$

Por último, la matriz de confusión nos otorga una vista de porque la clasificación no es buena en este caso:

![Matriz de multiclase](https://i.imgur.com/8BObo67.png)

Más concretamente la fracción de etiquetas es:
| Etiqueta   | Número de datos |
|------------|-----------------|
| Etiqueta 1 | 71              |
| Etiqueta 2 | 76              |
| Etiqueta 3 | 17              |
| Etiqueta 4 | 0               |
| Etiqueta 5 | 13              |
| Etiqueta 6 | 9               |
| Etiqueta 7 | 29              |
| __Total__  | __215__         |
          
### POSIBLES MEJORAS

---

- Crear operadores adicionales
- Cambiar la clasificación a distancia de binarios.
- Minimizar el árbol y eliminar ramas innecesarias usando Orthogonal least squares (OLS). No implementado , ya que aumenta el tiempo de ejecución y no merece la pena la mejora.

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
