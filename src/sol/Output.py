import pygraphviz as pgv
from deap import gp
import os

from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import metrics
import matplotlib.pyplot as plt

def get_parsed_label(label):
    label_dict = {
        "protDiv": "/",
        "protSqrt": "√",
        "mul": "*",
        "sub": "-",
        "add": "+",
    }
    
    has_parsed = label in label_dict
    label = label_dict[label] if has_parsed else label
    
    return label

def save_generated_tree(individual, exp_name):
    nodes, edges, labels = gp.graph(individual)

    g = pgv.AGraph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    g.layout(prog="dot")
    
    g.node_attr.update(color="lightblue2", style="filled")
    
    for i in nodes:
        n = g.get_node(i)
        l = get_parsed_label(labels[i])
        n.attr["label"] = l

    output_path = f"../../output/{exp_name}/tree.png"

    g.draw(os.path.join(os.getcwd(), output_path))
    
def plot_conf_matrix(targets, guesses, exp_name):
    cm = metrics.confusion_matrix(targets, guesses)
    ConfusionMatrixDisplay(cm).plot()

    save_plot(exp_name, "conf_matrix")

def save_plot(file_name, title):
    folder = f"../../Output/{file_name}"

    exists = os.path.exists(folder)
    if not exists:
        os.mkdir(folder)

    plt.savefig(f"{folder}/{title}.png")
        
def print_metrics_report(targets, guesses):
    report = metrics.classification_report(targets, guesses, zero_division=1)
    print(report)
    