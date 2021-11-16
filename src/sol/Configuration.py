from deap import creator, base, tools, gp
import math
import operator
import random
from Evaluation import eval_ind_simple


def protDiv(left, right):
    return 0 if right == 0 else left / right


def protSqrt(x):
    return math.sqrt(abs(x))


def config_individual():
    # Create primitive set
    pset = gp.PrimitiveSet("MAIN", 9)

    # Add all primitives to the primitive set
    pset.addPrimitive(operator.add, 2)
    pset.addPrimitive(operator.sub, 2)
    pset.addPrimitive(operator.mul, 2)
    pset.addPrimitive(protDiv, 2)
    pset.addPrimitive(operator.neg, 1)
    pset.addPrimitive(operator.abs, 1)
    # pset.addPrimitive(protSqrt, 1)
    # pset.addPrimitive(math.cos, 1)
    # pset.addPrimitive(math.sin, 1)

    pset.renameArguments(ARG0="RI", ARG1="Na", ARG2="Mg",
                         ARG3="Al", ARG4="Si", ARG5="K",
                         ARG6="Ca", ARG7="Ba", ARG8="Fe")

    # pset.addEphemeralConstant("rand101", lambda: random.uniform(0, 1))

    return pset


def config_population(toolbox, max_subtree_height):
    # Create fitness and individual.
    if not hasattr(creator, "FitnessMax"):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    if not hasattr(creator, "Individual"):
        creator.create("Individual", gp.PrimitiveTree,
                       fitness=creator.FitnessMax)

    pset = config_individual()

    # Register expr, individual, population and compile in toolbox
    toolbox.register("expr", gp.genHalfAndHalf, pset=pset,
                     min_=1, max_=max_subtree_height)
    toolbox.register("individual", tools.initIterate,
                     creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("compile", gp.compile, pset=pset)

    return pset


def config_algorithm(inputs, targets, toolbox, pset, max_tree_height, max_subtree_mut_height):
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0,
                     max_=max_subtree_mut_height)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

    limit_height = max_tree_height
    toolbox.decorate("mate", gp.staticLimit(
        key=operator.attrgetter("height"), max_value=limit_height))
    toolbox.decorate("mutate", gp.staticLimit(
        key=operator.attrgetter("height"), max_value=limit_height))

    n_elem = 200
    toolbox.decorate("mate", gp.staticLimit(key=len, max_value=n_elem))
    toolbox.decorate("mutate", gp.staticLimit(key=len, max_value=n_elem))

    def eval_func(toolbox, individual):
        return eval_ind_simple(inputs, targets, toolbox, individual)

    toolbox.register("evaluate", eval_func, toolbox)


def config(inputs, targets, toolbox,
           max_tree_height=5, max_subtree_height=3,  max_subtree_mut_height=2):
    pset = config_population(toolbox, max_subtree_height)
    config_algorithm(inputs, targets, toolbox, pset,
                     max_tree_height, max_subtree_mut_height)
