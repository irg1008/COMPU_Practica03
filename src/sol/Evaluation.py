from sklearn import metrics


def eval_ind_simple(inputs, targets, toolbox, individual):
    func = toolbox.compile(expr=individual)
    guesses = [round(func(*input)) for input in inputs]

    f1_score = metrics.f1_score(targets, guesses, average="micro")

    return f1_score,
