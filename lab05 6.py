def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def sequential_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search_iterative(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(arr, key, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        return binary_search_recursive(arr, key, mid + 1, high)
    else:
        return binary_search_recursive(arr, key, low, mid - 1)

def main():
    numbers = []
    n = int(input("Enter the number of integers: "))
    print("Enter the integers in the range 1 to 100:")
    for _ in range(n):
        num = int(input())
        if 1 <= num <= 100:
            numbers.append(num)
        else:
            print("Please enter integers in the range 1 to 100.")
            return

    selection_sort(numbers)
    print("Sorted list:", numbers)

    key = int(input("Enter a key to search: "))

    # Sequential Search
    seq_result = sequential_search(numbers, key)
    if seq_result != -1:
        print(f"Sequential Search: Found key at position {seq_result}")
    else:
        print("Sequential Search: Not Found!")

    # Binary Search (Iterative)
    binary_iter_result = binary_search_iterative(numbers, key)
    if binary_iter_result != -1:
        print(f"Binary Search (Iterative): Found key at position {binary_iter_result}")
    else:
        print("Binary Search (Iterative): Not Found!")

    # Binary Search (Recursive)
    binary_recursive_result = binary_search_recursive(numbers, key, 0, len(numbers) - 1)
    if binary_recursive_result != -1:
        print(f"Binary Search (Recursive): Found key at position {binary_recursive_result}")
    else:
        print("Binary Search (Recursive): Not Found!")

if __name__ == "__main__":
    main()
