# Problem 1
 #Ask the user for a sentence.
 #Print how many words it has.
 #(Hint: split the sentence by spaces)
user_input = input("Type a sentences with multiple words: ")
x = user_input.split(" ")
print(len(x))


# Problem 2
# Ask the user for a word.
# Build a new string that turns every vowel into "*".
# Example: "hello" -> "h*ll*"
user_input = input("Say a word: ")
new_word = " "
for i in range(len(user_input)): 
    print(user_input[i])
    if user_input[i] in "aeiou":
        new_word = new_word + "*"
    else: 
        new_word = new_word + user_input[i]
print(new_word)



# Problem 3
# Ask the user for a word.
# Print the first index where the letter "a" appears.
# If there is no "a", print -1.
user_input = input("Say a word: ")
index = -1
for i in range(len(user_input)):
    if user_input[i] == "a": 
        index = i
        break
print(index)



# Problem 4
 #Ask the user for two words.
 #print the longer word. If they are the same length, print "Tie".
user_input = input ("Say one word: ")
user_input2 = input ("Say another word: ")
if len (user_input) > len (user_input2):
    print (user_input)
elif len (user_input2) > len (user_input):
    print (user_input2)
else:
   print ("Tie")

# Problem 5
# Ask the user for a phrase.
# Build a new string that keeps only letters (remove spaces and punctuation).
# For this problem, remove commas and periods too.
user_input = input("Say a phrase:")
new_string = " "
for character in user_input:
    if character.isalpha():
        new_string = new_string + character
print(new_string)