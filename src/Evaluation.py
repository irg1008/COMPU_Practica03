
def eval_ind(inputs, targets, toolbox, individual):
    func = toolbox.compile(expr=individual)

    correct_guesses = 0
    total_guesses = len(individual)

    for input, target in zip(inputs, targets):
        print(inputs)
        guess = func(*input)
        if guess == target:
            correct_guesses += 1

    return correct_guesses/total_guesses,
