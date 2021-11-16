from deap import base

from EvolutiveCycle import make_evolution
from Input import load_data
from Test import test_data
from Configuration import config
from Stats import config_stats, plot_fitness_penalty
from Output import save_generated_tree, plot_conf_matrix

import time

def experiment(NGEN=200, NIND=200,
         max_tree_height=10, max_subtree_height=3, max_mutated_subtree_height=2, CXPB=0.5, MUTPB=0.2,
         nexp = "", param = "",
         use_binary=True, save_tree=True, plot_stats=True, plot_matrix=True, debug=True,
         ):

    # Create toolbox.
    # -----------------------------
    toolbox = base.Toolbox()

    # Import data.
    # -----------------------------
    inputs, binary_targets, multiple_targets = load_data()
    targets = binary_targets if use_binary else multiple_targets

    # Config algorithm.
    # -----------------------------
    config(inputs, targets, toolbox,
           max_tree_height, max_subtree_height, max_mutated_subtree_height)

    # Config stats.
    # -----------------------------
    stats = config_stats()

    # Make evolution.
    # -----------------------------
    logbook, best = make_evolution(toolbox, stats, CXPB, MUTPB, NGEN, NIND)

    # Show stats, debug and tree.
    # -----------------------------
    fitness = round(best.fitness.values[0], 4)
    
    if debug:
        print(
            f"Best individual is {best} with fitness {fitness}")

    if plot_stats:
        plot_fitness_penalty(logbook, nexp=nexp, param=param, fitness=fitness)

    if save_tree:
        save_generated_tree(best, nexp=nexp, param=param, fitness=fitness)

    # Test the input data (only needed in f_score fitness function).
    # -----------------------------
    n_correct, guesses = test_data(inputs, targets, best, toolbox, plot_matrix)

    if debug:
        print(f"Number correct: {n_correct} out of {len(inputs)}")
        print(f"The correctly guessed percentage is {n_correct/len(inputs)}")

    if plot_matrix:
        plot_conf_matrix(targets, guesses, nexp=nexp, param=param, fitness=fitness)
        
    return fitness, best

def main():
    total_start = time.time()
    for k in range(10):
        start = time.time()
        TH = [6, 8, 10, 12]
        MITH = [1, 2, 4, 5]
        MUTSH = [1, 2, 4, 5]
        CXPB = [0.4, 0.5, 0.6, 0.8]
        MUTPB = [0.1, 0.15, 0.25, 0.3]

        base = (5, 3, 3, 0.7, 0.2)
        comb = (TH, MITH, MUTSH, CXPB, MUTPB)
        names = (
            "TreeHeight",
            "MaxInitialTreeHeight",
            "MaxMutationSubtreeHeight",
            "CroisProbability",
            "MutationProbability"
        )

        for i in range(1):#len(base)):
            experimento = list(base)
            experimento[i] = comb[i]

            for j in experimento[i]:
                aux = list(experimento)
                aux[i] = j
                
                es = time.time()
                fitness, best = experiment(
                    max_tree_height=aux[0],
                    max_subtree_height=aux[1],
                    max_mutated_subtree_height=aux[2],
                    CXPB=aux[3],
                    MUTPB=aux[4],
                    nexp=names[i],
                    param=aux[i]
                )
                ee = time.time()
                with open('comas.csv','a') as fd:
                    fd.write(f"{names[i]},{aux[i]},{fitness},{ee-es}\n")
                with open('espacios.csv','a') as fd:
                    fd.write(f"{names[i]} {aux[i]} {fitness} {ee-es}\n")
                
        
        end = time.time()
        print(f">> Tiempo {k}: {end - start}")
    
    total_end = time.time()
    print(f"> Tiempo 10 iteraciones: {total_end-total_start}")

if __name__ == "__main__":
    main()
