from sklearn import metrics


def eval_ind_simple(inputs, targets, toolbox, individual):
    func = toolbox.compile(expr=individual)
    guessed_equals_target = 0
    guesses = []

    for input, target in zip(inputs, targets):
        guessed_target = round(func(*input))
        guesses.append(guessed_target)

        if guessed_target != target:
            guessed_equals_target += 1

    # The Hamming loss is the fraction of labels that are incorrectly predicted.
    hamming_loss = metrics.hamming_loss(targets, guesses)
    f1_score = metrics.f1_score(targets, guesses, average="micro")

    return f1_score, guessed_equals_target
