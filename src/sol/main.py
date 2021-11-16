from deap import base

from EvolutiveCycle import make_evolution
from Input import load_data
from Test import test_data
from Configuration import config
from Stats import config_stats, plot_fitness_penalty
from Output import save_generated_tree, plot_conf_matrix, print_metrics_report


def main(CXPB=0.5, MUTPB=0.2, NGEN=50, NIND=500, use_binary=True,
         save_tree=True, plot_stats=True, plot_matrix=True, debug=True,
         max_tree_height=5, max_subtree_height=3, max_mutated_subtree_height=2):

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

    if debug:
        fitness = round(best.fitness.values[0], 4)
        print(
            f"Best individual is {best} with fitness {fitness}")
        
    if plot_stats:
        plot_fitness_penalty(logbook)

    if save_tree:
        save_generated_tree(best)

    # Test the input data.
    # -----------------------------
    n_correct, guesses = test_data(inputs, targets, best, toolbox, plot_matrix)

    if debug:
        print(f"Number correct: {n_correct} out of {len(inputs)}")
        print(f"The correctly guessed percentage is {n_correct/len(inputs)}")

    if plot_matrix:
        plot_conf_matrix(targets, guesses)

    print_metrics_report(targets, guesses)

    return best


if __name__ == "__main__":
    main()
