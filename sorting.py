import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(values):
    x = len(values)
    for i in range(x):
        min = i
        for j in range(i+1, x):
            if values[j] < values[min]:
                min = j
        values[i], values[min] = values[min], values[i]
    return values



if __name__ == "__main__":
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    print(values)  # např. [42, 7, 91, 15, 63, 8, 57, 73, 2, 100]
    selection = selection_sort(values)
    print(selection)
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20
