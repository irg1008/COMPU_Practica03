from EvolutiveCycle import make_evolution
from Input import load_data
from Test import test_data
from deap import base


def main():
    toolbox = base.Toolbox()

    # To test binary or multi-class change targets for multiple_targets and the other way around.
    inputs, targets, multiple_targets = load_data()

    logbook, best = make_evolution(inputs, targets,
                                   toolbox, plot_stats=True,
                                   CXPB=0.5, MUTPB=0.2, NGEN=40, NIND=50)

    print(logbook)
    print(
        f"Best individual is {best} with fitness {best.fitness.values[0]}")

    test_data(inputs, targets, best, toolbox)


if __name__ == "__main__":
    main()
