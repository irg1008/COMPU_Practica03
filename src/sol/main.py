from EvolutiveCycle import make_evolution
from Input import load_data
from Test import test_data
from deap import base


def main():
    toolbox = base.Toolbox()

    inputs, targets, multiple_targets = load_data()
    
    _, best = make_evolution(inputs, targets,
                             toolbox, plot_stats=True,
                             CXPB=0.5, MUTPB=0.8, NGEN=30, NIND=50)
    
    test_data(inputs, targets, best, toolbox)


if __name__ == "__main__":
    main()
