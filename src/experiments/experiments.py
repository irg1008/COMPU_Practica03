# Create experiments for main file in src/sol
# Experiment with number of individuals.
# Experiment with number of iterations.

def experiments():
    TH = [2, 6, 8, 10]
    MITH = [1, 2, 4, 5]
    MUTSH = [1, 2, 4, 5]
    CXPB = [0.5, 0.6, 0.8, 0.9]
    MUTPB = [0.1, 0.15, 0.25, 0.3]

    base = (5, 3, 3, 0.7, 0.2)
    comb = (TH, MITH, MUTSH, CXPB, MUTPB)
    names = (
        "Tree height",
        "Max Initial Tree Height",
        "Max Mutation Subtree Height",
        "Crois Probability",
        "Mutation Probability"
    )

    for i in range(len(base)):
        experimento = list(base)
        experimento[i] = comb[i]

        for j in experimento[i]:
            aux = list(experimento)
            aux[i] = j
            
            # Aqui ejecutamos la funcion con los experimentos de aux
            
            # Aqui guardamos las imágenes en ficheros
            ngraph = "{names[i]} - {aux[i]} - graph"  # Nombre del grafico
            ntree = "{names[i]} - {aux[i]} - tree"  # Nombre del arbol
