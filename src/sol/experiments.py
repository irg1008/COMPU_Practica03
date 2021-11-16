# Create experiments for main file in src/sol
# Experiment with number of individuals.
# Experiment with number of iterations.
from main import experimento

def experiments():
    TH = [6, 8, 10]
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
            
            experiment(
                max_tree_height=aux[0],
                max_subtree_height=aux[1],
                max_mutated_subtree_height=aux[2],
                CXPB=aux[3],
                MUTPB=aux[4],
                nexp=names[i],
                param=aux[i]
            )
