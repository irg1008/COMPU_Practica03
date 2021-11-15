from sklearn import metrics
import random


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

    f1_score = metrics.f1_score(test, guesses, average="weighted")

    return f1_score,


def eval_ind_simple(inputs, targets, toolbox, individual):
    func = toolbox.compile(expr=individual)
    guessed_equals_target = 0
    
    min_limit, max_limit = min(targets), max(targets)
    penalty = 0

    for input, target in zip(inputs, targets):
        guessed_target = round(func(*input))

        if guessed_target == target:
            guessed_equals_target += 1
                        
        if not min_limit <= guessed_target <= max_limit:
            # Get distance outside interval between min and max.
            distance = abs(guessed_target - min_limit) + abs(guessed_target - max_limit)
            # Makes the convergence easier, but mutation takes toll.
            # Thats why we use a random value.
            if random.random() < 0.2:
                penalty += distance

    return guessed_equals_target/len(inputs), penalty

# def eval_ind_advanced(inputs, targets, toolbox, individual):
#     # Sensitivity and specificity.
#     a, b = 1, 1
#     n = len(inputs)

#     func = toolbox.compile(expr=individual)

#     # Correct and wrong classifications.
#     wrong_guesses = 0

#     for input, target in zip(inputs, targets):
#         guess = func(*input)
#         type = target[0]

#         if int(guess) != type:
#             wrong_guesses += 1

#     acc = (n - wrong_guesses) / n

#     return acc,
