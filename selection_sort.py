def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Input from the user
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in user_input.split()]

selection_sort(numbers)

# Display the sorted list
print("Sorted list:", numbers)
