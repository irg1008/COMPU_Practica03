from EvolutiveCycle import make_evolution
from Input import load_data
from Test import test_data
from deap import base


def main():
    toolbox = base.Toolbox()

    # To test binary or multi-class change targets for multiple_targets and the other way around.
    inputs, binary_targets, multiple_targets = load_data()
    
    targets = multiple_targets
    targets = binary_targets

    _, best = make_evolution(inputs, targets,
                                   toolbox, plot_stats=True, plot_tree=True, debug=True,
                                   CXPB=0.6, MUTPB=0.2, NGEN=50, NIND=50)

    test_data(inputs, targets, best, toolbox, debug=False)


if __name__ == "__main__":
    main()
