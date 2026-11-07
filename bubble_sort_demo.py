# Create an unsorted list
numbers = [64, 25, 12, 22, 11]

print("Original list:", numbers)

# Repeat the sorting process
for i in range(len(numbers) - 1):

    # Compare numbers next to each other
    for j in range(len(numbers) - 1 - i):

        # Swap numbers if they are in the wrong order
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # Show the list after each pass
    print("Pass", i + 1, ":", numbers)

print("Sorted list:", numbers)