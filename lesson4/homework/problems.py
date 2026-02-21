# Problem 1
# Ask the user for a sentence.
# Use a dictionary to count how many times each word appears.
# Print the dictionary.
# (Hint: split the sentence)
user_input =  input("Enter a sentence: ")
word_counts = {}
words = user_input.split()
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts)



# Problem 2
# Create a dictionary called capitals with states and their capitals.
# Ask the user for a state and print the capital.
# If not found, print "No data".
capitals = {"Canada": "Ottawa", "USA": "Washington D.C.", "Mexico": "Mexico City"}
state = input("Enter any state:")
if state.title() in capitals:
    print("The capital of", state, "is", capitals[state.title()])
else:
    print("No data")


# Problem 3
# Ask the user for a word.
# Print the letter that appears the most times.
# If there is a tie, print any one of them.
user_input = input("Enter a word: ")
letter_counts = {}
for letter in user_input:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

if letter_counts:
    max_letter = max(letter_counts, key=letter_counts.get)
    print(max_letter)


# Problem 4
# Create a dictionary called inventory with items and their quantity.
# Ask the user what item they want to buy and how many.
# If there are enough, subtract from the inventory and print the new inventory.
# Otherwise print "Not enough".
inventory = {"apple": 10, "banana": 5, "orange": 8}
item = input("What item do you want to buy: ")
quantity = int(input("How many do you want to buy: "))

if item in inventory and inventory[item] >= quantity:
    inventory[item] -= quantity
    print("New inventory:", inventory)
else:
    print("Not enough")


# Problem 5
# Ask the user for two words.
# Use dictionaries to check if they are anagrams (same letters, different order).
# Print "Anagram" or "Not anagram".
word = input("Enter the first word: ")
word2 = input("Enter the second word: ")
def count_letters(word):
    word = word.lower()
    letter_count =  {}
    for letter in word:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    return letter_count
if count_letters(word) == count_letters(word2):
    print("Anagram")
else:
    print("Not anagram")