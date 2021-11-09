import pygraphviz as pgv
from deap import gp
import os

def show_tree(individual):
    nodes, edges, labels = gp.graph(individual)

    g = pgv.AGraph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)
    g.layout(prog="dot")

    for i in nodes:
        n = g.get_node(i)
        n.attr["label"] = labels[i]

    output_path = "../../output/tree.pdf"

    g.draw(os.path.join(os.getcwd(), output_path))