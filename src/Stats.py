import matplotlib.pyplot as plt
from deap import tools
import numpy as np

def config_stats():
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("std", np.std)
    stats.register("min", np.min)
    stats.register("max", np.max)
    return stats


def show_stats(log):
    gen = log.select("gen")
    avgs = log.select("avg")

    _, ax1 = plt.subplots()

    _ = ax1.plot(gen, avgs, "r-", label="Average Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness", color="b")

    plt.show()
