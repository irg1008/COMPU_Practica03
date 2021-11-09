import matplotlib.pyplot as plt
from deap import tools
import numpy as np
import os


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
    mins = log.select("min")
    maxs = log.select("max")

    _, ax1 = plt.subplots()

    _ = ax1.plot(gen, avgs, "b-", label="Average Fitness")
    _ = ax1.plot(gen, maxs, "g-", label="Max Fitness")
    _ = ax1.plot(gen, mins, "r-", label="Min Fitness")
    ax1.set_xlabel("Generation")
    ax1.set_ylabel("Fitness", color="b")

    plt.savefig(os.path.join(os.getcwd(), "../../output/stats.png"))

    plt.show()
