#!/usr/bin/env python3
"""Sorting algorithms demo."""

import random
import time


def bubble_sort(arr):
    """Bubble sort implementation."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    """Quick sort implementation."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """Merge sort implementation."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    """Merge two sorted lists."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def test_sort(sort_func, arr, name):
    """Test a sorting function."""
    arr_copy = arr.copy()
    start = time.time()
    sorted_arr = sort_func(arr_copy)
    elapsed = time.time() - start
    print(f"{name}: {len(arr)} elements sorted in {elapsed:.4f}s")
    return sorted_arr


def main():
    """Main function."""
    print("=" * 50)
    print("Sorting Algorithms Demo")
    print("=" * 50)
    
    # Generate random array
    sizes = [100, 1000, 5000]
    
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        print(f"\nArray size: {size}")
        print("-" * 30)
        
        test_sort(bubble_sort, arr, "Bubble Sort")
        test_sort(quick_sort, arr, "Quick Sort")
        test_sort(merge_sort, arr, "Merge Sort")
    
    print("\n" + "=" * 50)
    print("Done!")


if __name__ == "__main__":
    main()
