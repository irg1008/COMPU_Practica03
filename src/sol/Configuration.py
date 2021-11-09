from deap import creator, base, tools, gp
import math
import operator
import random
from Evaluation import eval_ind_confussion


def protDiv(left, right):
    return 1 if right == 0 else left / right


def config_individual():
    # Create primitive set
    pset = gp.PrimitiveSet("MAIN", 9)

    # Add all primitives to the primitive set
    pset.addPrimitive(operator.add, 2)
    pset.addPrimitive(operator.sub, 2)
    pset.addPrimitive(operator.mul, 2)
    pset.addPrimitive(protDiv, 2)
    pset.addPrimitive(operator.neg, 1)
    pset.addPrimitive(math.cos, 1)
    pset.addPrimitive(math.sin, 1)

    pset.renameArguments(ARG0="RI", ARG1="Na", ARG2="Mg",
                         ARG3="Al", ARG4="Si", ARG5="K",
                         ARG6="Ca", ARG7="Ba", ARG8="Fe")

    # pset.addEphemeralConstant("rand101", lambda: random.uniform(-1, 1))

    return pset


def config_population(toolbox):
    # Create fitness and individual.
    if not hasattr(creator, "FitnessMax"):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    if not hasattr(creator, "Individual"):
        creator.create("Individual", gp.PrimitiveTree,
                       fitness=creator.FitnessMax)

    pset = config_individual()

    # Register expr, individual, population and compile in toolbox
    toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=3)
    toolbox.register("individual", tools.initIterate,
                     creator.Individual, toolbox.expr)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("compile", gp.compile, pset=pset)

    return pset


def config_algorithm(inputs, targets, toolbox, pset):
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

    toolbox.decorate("mate", gp.staticLimit(
        key=operator.attrgetter("height"), max_value=17))
    toolbox.decorate("mutate", gp.staticLimit(
        key=operator.attrgetter("height"), max_value=17))

    def eval_func(toolbox, individual):
        return eval_ind_confussion(inputs, targets, toolbox, individual)

    toolbox.register("evaluate", eval_func, toolbox)
