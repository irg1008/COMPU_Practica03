def test_data(inputs, targets, best_sol, toolbox):
    func = toolbox.compile(expr=best_sol)
    guessed_equals_target = 0

    for input, target in zip(inputs, targets):
        guessed_target = func(*input)
        is_not_window, _ = target
        
        print(f"To guess: {is_not_window}. Guessed value is: {guessed_target}")
        
        if guessed_target == is_not_window:
            guessed_equals_target += 1

    # print("Number correct: {} out of {}".format(
    #     guessed_equals_target, len(inputs)))
    print(
        f"The correctly guessed percentage is {guessed_equals_target/len(inputs)}")
