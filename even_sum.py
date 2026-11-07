# Add even numbers using a for loop
total = 0

for num in range(1, 51):
    if num % 2 == 0:
        total += num

print("For loop total:", total)

# Add even numbers using a while loop
total = 0
num = 1

while num <= 50:
    if num % 2 == 0:
        total += num
    num += 1

print("While loop total:", total)

# Both loops give the same result.
# I find the for loop easier to understand.