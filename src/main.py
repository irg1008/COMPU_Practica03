from EvolutiveCycle import make_evolution
from Input import load_data
from Test import test_data
from deap import base


def main():
    toolbox = base.Toolbox()

    inputs, targets = load_data()
    _, best = make_evolution(inputs, targets,
                             toolbox, plot_stats=True,
                             CXPB=0.5, MUTPB=0.1, NGEN=300, NIND=400)
    test_data(inputs, targets, best, toolbox)


if __name__ == "__main__":
    main()
