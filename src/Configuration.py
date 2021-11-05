from deap import creator, base, tools, gp
import math
import random
import operator
from Evaluation import eval_ind


def protectedDiv(left, right):
    return 1 if right == 0 else left / right


def config_individual():
    # Create primitive set
    pset = gp.PrimitiveSet("MAIN", 1)

    # Add all primitives to the primitive set
    pset.addPrimitive(operator.add, 2)
    pset.addPrimitive(operator.sub, 2)
    pset.addPrimitive(operator.mul, 2)
    pset.addPrimitive(protectedDiv, 2)
    pset.addPrimitive(operator.neg, 1)
    pset.addPrimitive(math.cos, 1)
    pset.addPrimitive(math.sin, 1)

    """
    A constant (random) value to include in the tree is added: it allows to include in the functions other operands.
    """
    pset.addEphemeralConstant("rand101", lambda: random.randint(-1, 1))

    """
    An argument is added for the function to be evaluated (in our problem there is only one: the 'x' of the function). 
    That is, given an x, you are asked to calculate the corresponding y.
    If the function needs more input parameters, they are added here
    """
    pset.renameArguments(ARG0="x")

    return pset


def config_population(toolbox):
    # Create fitness and individual.
    if not hasattr(creator, "FitnessMin"):
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    if not hasattr(creator, "Individual"):
        creator.create("Individual", gp.PrimitiveTree,
                       fitness=creator.FitnessMin)

    pset = config_individual()

    # Register expr, individual, population and compile in toolbox
    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
    toolbox.register("individual", tools.initIterate,
                     creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("compile", gp.compile, pset=pset)

    return pset


def config_algorithm(toolbox, pset):
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

    toolbox.decorate("mate", gp.staticLimit(
        key=operator.attrgetter("height"), max_value=17))
    toolbox.decorate("mutate", gp.staticLimit(
        key=operator.attrgetter("height"), max_value=17))

    toolbox.register("evaluate", eval_ind, toolbox)
