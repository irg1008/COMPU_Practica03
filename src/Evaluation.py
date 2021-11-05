import math
from Input import fCuarta


def eval_ind(toolbox, individual):
    # Se calcula el error cuadrático medio que comete la función
    # al evaluarse sobre los diferentes datos
    # El ECM se calcula como:

    func = toolbox.compile(expr=individual)

    entradas, salidas = fCuarta()

    sqerrors = []
    for x, y in zip(entradas, salidas):
        sqerrors.append((func(x) - y)**2)

    return (math.fsum(sqerrors) / len(entradas)),
