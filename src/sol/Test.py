def test_data(inputs, targets, best_sol, toolbox, plot_matrix=True):
    func = toolbox.compile(expr=best_sol)
    guessed_equals_target = 0
    guesses = []

    for input, target in zip(inputs, targets):
        guessed_target = round(func(*input))
        guesses.append(guessed_target)

        if guessed_target == target:
            guessed_equals_target += 1

    return guessed_equals_target, guesses

