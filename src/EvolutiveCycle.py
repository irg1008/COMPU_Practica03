from deap import tools, algorithms, base
from Configuration import config_population, config_algorithm
from Stats import config_stats, show_stats


def make_evolution(inputs, targets, CXPB = 0.5, MUTPB = 0.2, NGEN = 30, NPOP = 50, plot_stats=False):
    toolbox = base.Toolbox()

    pset = config_population(toolbox)
    stats = config_stats()

    config_algorithm(inputs, targets, toolbox, pset)

    pop = toolbox.population(n = NPOP)

    pop, logbook = algorithms.eaSimple(
        pop, toolbox, verbose=False, stats=stats,
        cxpb=CXPB, mutpb=MUTPB, ngen=NGEN)

    best = tools.selBest(pop, 1)[0]

    if plot_stats:
        print(
            f"Best individual is {best} with fitness {best.fitness.values[0]}")
        show_stats(logbook)

    return logbook, best
