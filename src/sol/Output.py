import pygraphviz as pgv
from deap import gp
import os

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import metrics
import matplotlib.pyplot as plt

def save_generated_tree(individual, nexp = "", param = "", fitness = ""):
    nodes, edges, labels = gp.graph(individual)

    g = pgv.AGraph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    g.layout(prog="dot")

    for i in nodes:
        n = g.get_node(i)
        n.attr["label"] = labels[i]

    if param != "":
        param = "-" + str(param) + "-"
    if fitness != "":
        fitness = "_f" + str(fitness) + "-"

    output_path = "../../output/" + nexp + param + "tree" + fitness + ".png"

    g.draw(os.path.join(os.getcwd(), output_path))
    
def plot_conf_matrix(targets, guesses, nexp = "", param = "", fitness = ""):
    cm = metrics.confusion_matrix(targets, guesses)
    ConfusionMatrixDisplay(cm).plot()

    if param != "":
        param = "-" + str(param) + "-"
    if fitness != "":
        fitness = "_f" + str(fitness) + "-"
    plt.savefig(os.path.join(os.getcwd(), "../../output/" + nexp + param + "confmat" + fitness + ".png"))

    plt.show()

def show_or_save(plot, file_name, title):
    if not plot and file_name is not None:
        folder = f"../../output/{file_name}"

        exists = os.path.exists(folder)
        if not exists:
            os.mkdir(folder)

        plt.savefig(f"{folder}/{title}.png")
    else:
        plt.show()