from sklearn import metrics


def eval_ind_confussion(inputs, targets, toolbox, individual):
    func = toolbox.compile(expr=individual)

    test = []
    guesses = []

    # Make the confusion matrix.
    for input, target in zip(inputs, targets):
        guess = func(*input)
        type = target[0]

        guesses.append(int(guess))
        test.append(type)

    f_score = metrics.f1_score(test, guesses, average="weighted")

    return f_score,
