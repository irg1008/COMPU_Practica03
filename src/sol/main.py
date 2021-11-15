from EvolutiveCycle import make_evolution
from Input import load_data
from Test import test_data
from deap import base


def main(use_binary=False, CXPB=0.7, MUTPB=0.2, NGEN=100, NIND=100, plot_stats=True,
         plot_tree=True, debug=True, debug_iter=False, plot_matrix=True):
    toolbox = base.Toolbox()

    # To test binary or multi-class change targets for multiple_targets and the other way around.
    inputs, binary_targets, multiple_targets = load_data()
    targets = binary_targets if use_binary else multiple_targets

    _, best = make_evolution(inputs, targets,
                             toolbox, plot_stats, plot_tree, debug,
                             CXPB, MUTPB, NGEN, NIND)

    test_data(inputs, targets, best, toolbox, debug, debug_iter, plot_matrix)


if __name__ == "__main__":
    main()
