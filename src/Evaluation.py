
def eval_ind(inputs, targets, toolbox, individual):
    func = toolbox.compile(expr=individual)

    correct_guesses = 0
    total_guesses = len(inputs)

    for input, target in zip(inputs, targets):
        is_window = target[1]
        guess = func(*input)

        if guess == is_window:
            correct_guesses += 1

    return correct_guesses/total_guesses,
