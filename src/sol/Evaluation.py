from sklearn import metrics


def eval_ind_simple(inputs, targets, toolbox, individual):
    """Funciton that uses f_score to calculate fitness.

    Args:
        inputs ([type]): [description]
        targets ([type]): [description]
        toolbox ([type]): [description]
        individual ([type]): [description]

    Returns:
        [type]: [description]
    """
    func = toolbox.compile(expr=individual)
    guesses = [round(func(*input)) for input in inputs]

    f1_score = metrics.f1_score(targets, guesses, average="micro")

    return f1_score,

def eval_ind_paper(inputs, targets, toolbox, individual):
    """Function that calculates accuracy of the individual based on reasearch on next paper:
    https://www.researchgate.net/publication/338868261_Data_Mining_and_Image_Analysis_Using_Genetic_Programming

    Args:
        inputs ([type]): [description]
        targets ([type]): [description]
        toolbox ([type]): [description]
        individual ([type]): [description]

    Returns:
        [type]: [description]
    """
    
    func = toolbox.compile(expr=individual)
    guesses = [round(func(*input)) for input in inputs]
    
    a, b = 0.5, 1
    TCN = 0

    for target, guess in zip(targets, guesses):
        if target == guess:
            TCN += 1
            
    N = len(inputs)
    FCN = N - TCN  

    fitness = (a*TCN) / (N + b*FCN)

    return fitness,