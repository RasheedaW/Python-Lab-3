# Create a list of numbers
numbers = [10, 5, 8, 2, 7]

print("Original list:", numbers)

# Sort without changing the original list
print("Sorted with sorted():", sorted(numbers))
print("Original list unchanged:", numbers)

# Sort the original list
numbers.sort()
print("Sorted with sort():", numbers)

# Add a number
numbers.append(12)
print("After adding 12:", numbers)

# Remove a number
numbers.remove(5)
print("After removing 5:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)