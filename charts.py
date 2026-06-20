import matplotlib.pyplot as plt
import database


def weight_progress_chart():
    weights = database.get_bodyweights()

    y = [i[0] for i in weights]
    x = list(range(1, len(y) + 1))

    plt.plot(x, y, marker="o")

    plt.xlabel("Record Number")
    plt.ylabel("Body Weight (kg)")
    plt.title("Weight Progress")

    plt.show()
