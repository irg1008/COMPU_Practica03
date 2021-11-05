
def eval_ind(inputs, targets, toolbox, individual):
    func = toolbox.compile(expr=individual)

    correct_guesses = 0
    total_guesses = len(inputs)

    for input, target in zip(inputs, targets):
        _, is_window = target
        guess = func(*input)

        if guess == is_window:
            correct_guesses += 1

    # TODO: Change this for a confussion matrix and a f_score

    return correct_guesses/total_guesses,


def eval_ind_confussion(inputs, targets, toolbox, individual):
    func = toolbox.compile(expr=individual)

    true_positives = 0
    true_negatives = 0
    false_positives = 0
    false_negatives = 0

    for input, target in zip(inputs, targets):
        guess = func(*input)
        
        is_not_window, _ = target

        if guess == is_not_window:
            if is_not_window:
                true_negatives += 1
            else:
                true_positives += 1
        else:
            if is_not_window:
                false_positives += 1
            else:
                false_negatives += 1

    f_score = true_positives/(true_positives + 1/2 *
                              (false_negatives + false_positives))

    return f_score,
