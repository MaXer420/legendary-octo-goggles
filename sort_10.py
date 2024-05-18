import random

a = []
orig = []
prompt = input("Ввести 10 чисел у масив?(y/n): ")
if prompt == "y":
    while len(a) < 10:
        try:
            a.append(int(input(f"Додайте значення(#{len(a)+1}): ")))
            orig.append(int(input(f"Додайте значення(#{len(a)+1}): ")))
        except ValueError:
            print("Будь ласка введіть, числове значення.")
elif prompt == "n":
    for r in range(10):
        rand = random.randint(-10, 100)
        a.append(rand)
        orig.append(rand)

print(f"Вот ваш масив: {a}")


def bubble_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        swapped = False
        for j in range(i+1, len_arr):
            if arr[i] >= arr[j]:
                swapped = True
                # swap the pair of items if out of order
                arr[i], arr[j] = arr[j], arr[i]
                print(arr)
        if not swapped:
            # if no swap was made the list is sorted
            return arr


def merge_sort(arr):
    list_length = len(arr)

    if list_length == 1:
        return arr

    center = list_length // 2
    left = merge_sort(arr[:center])  # divide the list into two sublists
    right = merge_sort(arr[center:])
    print(left, right)
    return merge(left, right)


def merge(larr, rarr):  # sort the sublists and merge them
    q = []
    while larr and rarr:
        q.append((larr if larr[0] <= rarr[0] else rarr).pop(0))  # sort sublist
    return q + larr + rarr


prompt = input("Посортувати за допомогою bubble sort чи merge sort алгоритму?(b/m): ")


if prompt == "b":
    print(f"\nOригінальний масив: {orig}\nВідсортований масив: {bubble_sort(a)}")
if prompt == "m":
    print(f"\nOригінальний масив: {orig}\nВідсортований масив: {merge_sort(a)}")

