import numpy as np
from sklearn import metrics


def eval_ind(inputs, targets, toolbox, individual):
    func = toolbox.compile(expr=individual)

    correct_guesses = 0
    total_guesses = len(inputs)

    for input, target in zip(inputs, targets):
        guess = func(*input)

        is_window = target[0]

        if guess == is_window:
            correct_guesses += 1

    return correct_guesses/total_guesses,


def eval_ind_confussion(inputs, targets, toolbox, individual):
    func = toolbox.compile(expr=individual)

    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for input, target in zip(inputs, targets):
        guess = func(*input)

        is_window = target[0]

        if guess == is_window:
            if is_window:
                TP += 1
            else:
                TN += 1
        else:
            if is_window:
                FN += 1
            else:
                FP += 1

    f_score = 2*TP/(2*TP + FP + FN)

    return f_score,


def eval_ind_multiple_confussion(inputs, targets, toolbox, individual):
    func = toolbox.compile(expr=individual)

    test = []
    guesses = []

    # Make the confusion matrix.
    for input, target in zip(inputs, targets):
        guess = func(*input)
        type = target[0]

        guesses.append(guess)
        test.append(type)

    conf_matrix = metrics.confusion_matrix(test, guesses)
    print(conf_matrix)
    print(metrics.classification_report(test, guesses, digits=3))

    f_score = metrics.f1_score(test, guesses, average="weighted")

    return f_score,
