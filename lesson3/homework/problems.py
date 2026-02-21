# Problem 1
# Ask the user for a number n.
# Print all multiples of 3 from 0 to n (including n if it is a multiple of 3).
user_input = int(input("Type a number:"))  
for i in range(0, user_input + 1, 3):
    print(i)



# Problem 2
# Ask the user for a number n.
# Print the square of every number from 1 to n (1*1, 2*2, ...).
user_input = int(input("Type a number:"))  
for i in range(1, user_input + 1):
    print(i * i)


# Problem 3
# Ask the user for a number n.
# Print the numbers from n down to 0 (counting down).
user_input = int(input("Type a number:"))
for i in range(user_input, -1, -1):
    print(i)


# Problem 4
# Ask the user for a word.
# Build a new string that repeats the word 5 times with spaces in between.
# Example: "hi hi hi hi hi"
user_input = input("Type a word:")
result = (user_input + " ") * 5
print(result.strip())  # Remove the trailing space  



# Problem 5
# Ask the user for a number n.
# Print how many numbers from 1 to n are even.
user_input = int(input("Type a number:"))
even_count = 0
for i in range(1, user_input + 1):
    if i % 2 == 0:
        even_count += 1
print("There are", even_count, "even numbers from 1 to", user_input)