from deap import tools, algorithms
from Configuration import config_population, config_algorithm
from Stats import config_stats, show_stats


def make_evolution(inputs, targets, toolbox, plot_stats=False, CXPB=0.5, MUTPB=0.2, NGEN=40, NIND=50):
    pset = config_population(toolbox)
    stats = config_stats()

    config_algorithm(inputs, targets, toolbox, pset)

    pop = toolbox.population(n=NIND)

    pop, logbook = algorithms.eaSimple(
        pop, toolbox, verbose=False, stats=stats,
        cxpb=CXPB, mutpb=MUTPB, ngen=NGEN)

    best = tools.selBest(pop, 1)[0]

    print(
        f"Best individual is {best} with fitness {best.fitness.values[0]}")

    if plot_stats:
        show_stats(logbook)

    return logbook, best
