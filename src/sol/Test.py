from sklearn.metrics import ConfusionMatrixDisplay
from sklearn import metrics
import matplotlib.pyplot as plt
import os

def test_data(inputs, targets, best_sol, toolbox,
              debug=False, debug_iter=False, plot_matrix=True):
    func = toolbox.compile(expr=best_sol)
    guessed_equals_target = 0
    guesses = []

    for input, target in zip(inputs, targets):
        guessed_target = round(func(*input))
        guesses.append(guessed_target)

        if debug_iter:
            print(f"To guess: {type}. Guessed value is: {guessed_target}")

        if guessed_target == target:
            guessed_equals_target += 1

    if debug:
        print("Number correct: {} out of {}".format(
            guessed_equals_target, len(inputs)))
        print(
            f"The correctly guessed percentage is {guessed_equals_target/len(inputs)}")
        
    if plot_matrix:
        cm = metrics.confusion_matrix(targets, guesses)
        ConfusionMatrixDisplay(cm).plot()

        plt.savefig(os.path.join(os.getcwd(), "../../output/conf_mat.png"))

        plt.show()
