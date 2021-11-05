from EvolutiveCycle import make_evolution
from Input import load_data


def main():
    inputs, targets = load_data()
    make_evolution(inputs, targets, plot_stats=True)


if __name__ == "__main__":
    main()
