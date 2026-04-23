import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values):
    val = values.copy()
    x = len(val)
    for i in range(x):
        min = i
        for j in range(i+1, x):
            if val[j] < val[min]:
                min = j
        val[i], val[min] = val[min], val[i]
    return val

def bubble_sort(values):
    val2 = values.copy()
    x = len(val2)
    plt.ion()
    plt.show()
    for i in range(x):
        for j in range(0, x-1-i):
            if val2[j] > val2[j+1]:
                val2[j], val2[j+1] = val2[j+1], val2[j]
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
    plt.ioff()
    plt.show()
    return val2


if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print("Data:")
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    selection = selection_sort(values)
    print("Selection:")
    print(selection)
    bubble = bubble_sort(values)
    print("Bubble:")
    print(bubble)
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
