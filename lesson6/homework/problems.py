# Problem 1
# Create a tuple called scores with 4 numbers.
# Print the average score.
scores = (85, 90, 78, 92)
average = sum(scores) / len(scores)
print("Average:", average)


# Problem 2
# Create a list of tuples representing students:
# ("Ava", 95), ("Ben", 88), ("Kai", 73)
# Print the name of the student with the highest score.
students = [("Ava", 95), ("Ben", 88), ("Kai", 73)]
highest_score = 0
top_student = ""
for name, score in students:
    if score > highest_score:
        highest_score = score
        top_student = name
print("Highest score was:", top_student)


# Problem 3
# Ask the user for a sentence.
# Split it into words.
# Create a list of tuples where each tuple is (word, length_of_word).
# Print the list.
user_input = input("Enter a sentence: ")
words = user_input.split()
word_lengths = []
for word in words:
    word_lengths.append((word, len(word)))
print(word_lengths) 




# Problem 4
# Create a function called first_and_last(word).
# It should return a tuple containing the first and last letter of the word.
# Test it.
def first_and_last(word):
    return word[0], word[-1]
answer = first_and_last("What")
print(answer)


# Problem 5
# Tuples can be dictionary keys.
# Create a dictionary where the keys are points like (x, y) and the values are colors.
# Add at least 3 points and print the dictionary.
point_colors = {(0, 0): "Red",(1, 2): "Blue",(3, 4): "Green"}
print(point_colors)