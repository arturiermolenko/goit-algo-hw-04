import random
import timeit


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sort_func(data)
    return timeit.default_timer() - start_time


def generate_data(dimension):
    return random.sample(range(dimension * 10), dimension)


def python_sort(data):
    return sorted(data)


if __name__ == "__main__":
    sizes = [100, 10000, 50000]
    for size in sizes:
        random_data = generate_data(size)

        print(f"Size: {size}")

        print(
            f"Insertion sort: {measure_time(insertion_sort, random_data.copy())} seconds"
        )
        print(f"Merge sort: {measure_time(merge_sort, random_data.copy())} seconds")
        print(
            f"Timsort (Python sorted): {measure_time(python_sort, random_data.copy())} seconds"
        )
