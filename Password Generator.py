# user input
word = input("Choose a website: ").lower()

# list tracks repeats in string
repeats = []

# length variable makes working with 2 different lengths of the "word" string easier
length = len(word)

# tracks even/odd position in string index with 2 being even and 1 odd
odd = 2

# dictionaries used to capitalize numbers and symbols because python doesn't let me do it by default
sym = {
    "1": "!",
    "2": "@",
    "3": "#",
    "4": "$",
    "5": "%",
    "6": "^",
    "7": "&",
    "8": "*",
    "9": "(",
    "0": ")"
}
numb = {
    "!": "1",
    "@": "2",
    "#": "3",
    "$": "4",
    "%": "5",
    "^": "6",
    "&": "7",
    "*": "8",
    "(": "9",
    ")": "0"
}

# finds repeat letters, adds them to the end of string, slices the string, and
# adds repeat letter to repeats list to avoid running for the same letter twice and to be used later on
for letter in word:
    if word.count(letter) > 1 and letter not in repeats:
        word += letter
        word = word[:word.index(letter)] + word[(word.index(letter) + 1):]
        repeats.append(letter)

# reverses word, adds letters to the end of string, and slices the original letters off
for letter in reversed(word):
    word += letter
word = word[length:]

# adds number equivalent to the length of the word times the number of repeats to the string
word += str(len(repeats) * len(word))

# defines new word variable, still unsure if entirely needed
new_word = word

# finds length of word, changes it to a string. This leaves us with a number that we can iterate and
# compare with the sym dictionary to concatenate the string with the symbols equivalent to it's length
for num in str(len(word)):
    new_word += sym[num]

# resets word
word = ""

# checks if index of string is even or odd using odd variable, if index is odd, capitalizes letter, if letter is number or symbol, uses sym and numb dictionaries
for letter in new_word:
    if odd == 1:
        if letter in sym:
            word += sym[letter]
        elif letter in numb:
            word += numb[letter]
        else:
            word += letter.upper()
        odd = 2
    else:
        word += letter
        odd = 1

# prints output with spaces to make it easier to see and copy in the terminal, especially during debugging
print("")
print(word)
print("")
