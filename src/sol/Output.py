import pygraphviz as pgv
from deap import gp
import os

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import metrics
import matplotlib.pyplot as plt

def save_generated_tree(individual):
    nodes, edges, labels = gp.graph(individual)

    g = pgv.AGraph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    g.layout(prog="dot")

    for i in nodes:
        n = g.get_node(i)
        n.attr["label"] = labels[i]

    output_path = "../../output/tree.png"

    g.draw(os.path.join(os.getcwd(), output_path))
    
def plot_conf_matrix(targets, guesses):
    cm = metrics.confusion_matrix(targets, guesses)
    ConfusionMatrixDisplay(cm).plot()

    plt.savefig(os.path.join(os.getcwd(), "../../output/conf_mat.png"))

    plt.show()
    
def plot_pareto():
    pass