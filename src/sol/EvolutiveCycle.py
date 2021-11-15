from deap import tools, algorithms
from Configuration import config_population, config_algorithm
from Stats import config_stats, show_stats
from Output import show_tree


def make_evolution(inputs, targets, toolbox, plot_stats=False, plot_tree=False, debug=False, CXPB=0.5, MUTPB=0.2, NGEN=40, NIND=50):
    pset = config_population(toolbox)
    stats = config_stats()

    config_algorithm(inputs, targets, toolbox, pset)

    pop = toolbox.population(n=NIND)
    hof = tools.HallOfFame(1)

    pop, logbook = algorithms.eaSimple(
        pop, toolbox, verbose=False, stats=stats, halloffame=hof,
        cxpb=CXPB, mutpb=MUTPB, ngen=NGEN)

    best = tools.selBest(pop, 1)[0]

    if debug:
        # print(logbook)
        print(f"Best individual is {best} with fitness {best.fitness.values[0]}")

    if plot_stats:
        show_stats(logbook)

    if plot_tree:
        show_tree(best)

    return logbook, best
