def test_data(inputs, targets, best_sol, toolbox):
    func = toolbox.compile(expr=best_sol)
    guessed_equals_target = 0

    for input, target in zip(inputs, targets):
        guessed_target = round(func(*input))

        is_window = target[0]

        print(f"To guess: {is_window}. Guessed value is: {guessed_target}")

        if guessed_target == is_window:
            guessed_equals_target += 1

    print("Number correct: {} out of {}".format(
        guessed_equals_target, len(inputs)))
    print(
        f"The correctly guessed percentage is {guessed_equals_target/len(inputs)}")
