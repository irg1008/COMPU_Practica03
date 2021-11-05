def test_data(inputs, targets, best_sol, toolbox, debug=False):
    func = toolbox.compile(expr=best_sol)
    guessed_equals_target = 0

    for input, target in zip(inputs, targets):
        guessed_target = round(func(*input))

        type = target[0]

        if debug:
            print(f"To guess: {type}. Guessed value is: {guessed_target}")

        if guessed_target == type:
            guessed_equals_target += 1

    if debug:
        print("Number correct: {} out of {}".format(
            guessed_equals_target, len(inputs)))
        print(
            f"The correctly guessed percentage is {guessed_equals_target/len(inputs)}")
