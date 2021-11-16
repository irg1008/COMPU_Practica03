from deap import tools, algorithms


def make_evolution(toolbox, stats, CXPB=0.5, MUTPB=0.2, NGEN=40, NIND=50):
    pop = toolbox.population(n=NIND)
    hof = tools.HallOfFame(1)
    
    pop, logbook = algorithms.eaSimple(
        pop, toolbox, verbose=False, stats=stats, halloffame=hof,
        cxpb=CXPB, mutpb=MUTPB, ngen=NGEN)
    
    best = tools.selBest(pop, 1)[0]

    return logbook, best
