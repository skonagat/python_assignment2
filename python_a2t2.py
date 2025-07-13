# Task 2: Sum of integers from 1 to 50 using a Loop

# Method 1 - Using for loop
sum = 0
for num in range(0, 51):
    sum += num
print ("Method 1 : Sum of all integers from 1 to 50 is", sum)

# Method 2 - Using formula n(n+1)/2
n=50
print("Method 2 : Sum of all integers from 1 to 50 is", int(n*(n+1)/2))