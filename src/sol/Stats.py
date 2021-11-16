import matplotlib.pyplot as plt
from deap import tools
import numpy as np
import os


def col(a, *n_cols):
    cols = []
    for n in n_cols:
        col = np.array(a)[:, n]
        cols.append(col)
    return cols


def config_stats():
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", np.min)
    stats.register("max", np.max)
    stats.register("std", np.std)
    stats.register("avg", np.average)
    return stats

def get_nice_legend(ax):
    legend = ax.legend(loc="best", shadow=True, edgecolor="black",
                       borderpad=1, labelspacing=0.8, facecolor="whitesmoke")
    plt.setp(legend.get_texts(), color="black")


def plot_ax(ax, x_label, y_label, _x, y, labels, colors):
    linewidth = 2
    line_alpha = 0.6
    grid_alpha = 0.1

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.tick_params(axis="y")
    ax.grid(alpha=grid_alpha)

    for _y, _l, _c in zip(y, labels, colors):
        ax.plot(_x, _y, color=_c,
                linewidth=linewidth, alpha=line_alpha, label=_l)

    get_nice_legend(ax)


def plot_fitness_penalty(log, title="Fitness over generations"):
    fit_label = "Fitness"
    x_label = "Generations"

    avg_label = "Average"
    max_label = "Maxs"
    min_label = "Mins"

    colors = ["r", "g", "b"]
    size = (12, 6)

    gen = log.select("gen")
    avgs = log.select("avg")
    mins = log.select("min")
    maxs = log.select("max")

    fig, ax = plt.subplots(1, figsize=size)

    fig.suptitle(title)

    plot_ax(ax, x_label, fit_label, gen,
            [avgs, maxs, mins],
            [avg_label, max_label, min_label],
            colors)

    plt.savefig(os.path.join(os.getcwd(), "../../output/stats.png"))
    plt.show()
