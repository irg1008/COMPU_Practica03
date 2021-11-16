from deap import base
from time import time
from EvolutiveCycle import make_evolution
from Input import load_data
from Test import test_data
from Configuration import config
from Stats import config_stats, plot_fitness_penalty
from Output import save_generated_tree, plot_conf_matrix, get_metrics_report, log


def execute(CXPB=0.5, MUTPB=0.2, NGEN=30, NIND=200, use_binary=True,
         save_tree=True, plot_stats=True, plot_matrix=True, debug=True, exp_name="Base",
         max_tree_height=10, max_subtree_height=3, max_mutated_subtree_height=2):
    
    print(f"Executing experiment: {exp_name}:")

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
    start = time() # Start evolution time.
    logbook, best = make_evolution(toolbox, stats, CXPB, MUTPB, NGEN, NIND)
    end = time() # End evolution time.

    # Show stats, debug and tree.
    # -----------------------------
    if debug:
        fitness = round(best.fitness.values[0], 4)
        log(
            f"Best individual is {best} with fitness {fitness}")
        
    if plot_stats:
        plot_fitness_penalty(logbook, exp_name)

    if save_tree:
        save_generated_tree(best, exp_name)

    # Test the input data.
    # -----------------------------
    n_correct, guesses = test_data(inputs, targets, best, toolbox, plot_matrix)

    if debug:
        log(f"Number correct: {n_correct} out of {len(inputs)}")
        log(f"The correctly guessed percentage is {n_correct/len(inputs)}")

    if plot_matrix:
        plot_conf_matrix(targets, guesses, exp_name)
        metrics = get_metrics_report(targets, guesses)
        log("Metrics for f_score and accuracy on all guessed labels:")
        print(metrics)


    log(f"Executing time: {round(end-start, 2)} seconds.")
    print("-----------------------------------------")

def main():
    execute()

if __name__ == "__main__":
    main()
