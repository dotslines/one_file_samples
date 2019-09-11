import random

my_list = [random.randint(0, 100) for i in range(40)]


def insertion_sort(sequence):
    length_seq = len(sequence)
    if length_seq < 2:
        return sequence
    else:
        for i in range(1, length_seq):
            before = sequence[:i]
            for j in range(len(before)):
                if sequence[i] < before[j]:
                    element = sequence[i]
                    for n in reversed(range(j, i)):
                        sequence[n+1] = sequence[n]
                        sequence[j] = element
    return sequence


print(insertion_sort(my_list))
