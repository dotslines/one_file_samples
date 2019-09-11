import random

my_list = [random.randint(0, 100) for i in range(40)]


def bubble_sort(sequence):
    list_length = len(sequence)
    if list_length < 2:
        return sequence
    else:
        flag = True
        while flag:
            for i in range(1, list_length):
                if sequence[i] < sequence[i-1]:
                    sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
                    flag = True
                else:
                    flag = False
                    for i in range(1, list_length):
                        if sequence[i] < sequence[i - 1]:
                            sequence[i], sequence[i - 1] = sequence[i - 1], sequence[i]
                            flag = True
    return sequence


print(bubble_sort(my_list))
