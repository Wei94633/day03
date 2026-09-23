# 3.1
name = input("Please enter your name: ")
name = name.capitalize()

print("Hello " + name + "!")
print("-" * 60)

# 3.2
number = input("Please enter a number: ")
print(type(number))
print("-" * 60)
# Reason: input() always returns a string, even if the user enters a number.

# 3.3
number1 = input("Please enter the first number: ")
number2 = input("Please enter the second number: ")

number1 = int(number1)
number2 = int(number2)

print("The sum of the provided numbers is", number1 + number2)
print("-" * 60)

# 3.4
text = input("Please enter a string: ")
words = text.split()

result = ""

for word in words:
    result += word[0]

print(result)
print("-" * 60)

# 3.5
text = input("Please enter a text: ").lower()

language_frequencies = {
    "Esperanto": {
        "a": 12, "b": 1, "c": 1, "d": 3, "e": 9,
        "f": 1, "g": 1, "h": 0, "i": 10, "j": 4,
        "k": 4, "l": 6, "m": 3, "n": 8, "o": 9,
        "p": 3, "r": 6, "s": 6, "t": 5, "u": 3,
        "v": 2, "z": 1
    },

    "Spanish": {
        "a": 13, "b": 2, "c": 5, "d": 6, "e": 14,
        "f": 1, "g": 1, "h": 1, "i": 6, "j": 0,
        "k": 0, "l": 5, "m": 3, "n": 7, "o": 9,
        "p": 3, "q": 1, "r": 7, "s": 8, "t": 5,
        "u": 4, "v": 1, "y": 1, "z": 1
    },

    "Portuguese": {
        "a": 15, "b": 1, "c": 4, "d": 5, "e": 13,
        "f": 1, "g": 1, "h": 1, "i": 6, "j": 0,
        "l": 3, "m": 5, "n": 5, "o": 11, "p": 3,
        "q": 1, "r": 7, "s": 8, "t": 4, "u": 5,
        "v": 2, "x": 0, "z": 1
    },

    "Italian": {
        "a": 12, "b": 1, "c": 5, "d": 4, "e": 12,
        "f": 1, "g": 2, "h": 1, "i": 10, "l": 7,
        "m": 3, "n": 7, "o": 10, "p": 3, "q": 1,
        "r": 6, "s": 5, "t": 6, "u": 3, "v": 2,
        "z": 1
    },

    "French": {
        "a": 8, "b": 1, "c": 3, "d": 4, "e": 15,
        "f": 1, "g": 1, "h": 1, "i": 8, "j": 1,
        "k": 0, "l": 6, "m": 3, "n": 7, "o": 6,
        "p": 3, "q": 1, "r": 7, "s": 8, "t": 7,
        "u": 6, "v": 2, "x": 0, "y": 0, "z": 0
    },

    "English": {
        "a": 8, "b": 2, "c": 3, "d": 4, "e": 13,
        "f": 2, "g": 2, "h": 6, "i": 7, "j": 0,
        "k": 1, "l": 4, "m": 2, "n": 7, "o": 8,
        "p": 2, "q": 0, "r": 6, "s": 6, "t": 9,
        "u": 3, "v": 1, "w": 2, "x": 0, "y": 2,
        "z": 0
    },

    "German": {
        "a": 7, "b": 2, "c": 3, "d": 5, "e": 16,
        "f": 2, "g": 3, "h": 5, "i": 7, "j": 0,
        "k": 1, "l": 3, "m": 3, "n": 10, "o": 3,
        "p": 1, "q": 0, "r": 7, "s": 7, "t": 6,
        "u": 4, "v": 1, "w": 2, "x": 0, "y": 0,
        "z": 1
    },

    "Dutch": {
        "a": 8, "b": 2, "c": 1, "d": 6, "e": 19,
        "f": 1, "g": 3, "h": 2, "i": 7, "j": 2,
        "k": 2, "l": 4, "m": 2, "n": 10, "o": 6,
        "p": 2, "q": 0, "r": 6, "s": 4, "t": 7,
        "u": 2, "v": 3, "w": 2, "x": 0, "y": 0,
        "z": 1
    },

    "Swedish": {
        "a": 9, "b": 2, "c": 2, "d": 5, "e": 10,
        "f": 2, "g": 3, "h": 2, "i": 6, "j": 1,
        "k": 3, "l": 5, "m": 4, "n": 9, "o": 5,
        "p": 2, "r": 8, "s": 7, "t": 8, "u": 2,
        "v": 2, "y": 1
    },

    "Polish": {
        "a": 11, "b": 2, "c": 4, "d": 3, "e": 7,
        "f": 0, "g": 2, "h": 1, "i": 8, "j": 2,
        "k": 4, "l": 2, "m": 3, "n": 7, "o": 8,
        "p": 3, "r": 5, "s": 4, "t": 4, "u": 3,
        "w": 5, "y": 4, "z": 6
    },

    "Turkish": {
        "a": 12, "b": 3, "c": 1, "d": 5, "e": 9,
        "f": 1, "g": 1, "h": 1, "i": 9, "j": 0,
        "k": 5, "l": 6, "m": 4, "n": 8, "o": 3,
        "p": 1, "r": 7, "s": 3, "t": 3, "u": 3,
        "v": 1, "y": 3, "z": 2
    }
}

letters = "abcdefghijklmnopqrstuvwxyz"
total = 0

for letter in letters:
    total += text.count(letter)

if total == 0:
    print("No valid letters found.")

else:
    text_frequencies = {}

    for letter in letters:
        count = text.count(letter)
        frequency = count / total * 100
        text_frequencies[letter] = frequency

        print(f"{letter}: {frequency:.2f}%")

    best_language = ""
    smallest_difference = float("inf")

    for language in language_frequencies:
        difference = 0

        for letter in letters:
            text_frequency = text_frequencies[letter]

            language_frequency = (
                language_frequencies[language].get(letter, 0)
            )

            difference += abs(
                text_frequency - language_frequency
            )

        print(f"{language} difference: {difference:.2f}")

        if difference < smallest_difference:
            smallest_difference = difference
            best_language = language


    print(f"Detected language: {best_language}")
print("-" * 60)

# 3.6
text = input("Please enter a text: ").lower()

language_frequencies = {
    "Esperanto": {
        "a": 12, "b": 1, "c": 1, "d": 3, "e": 9,
        "f": 1, "g": 1, "h": 0, "i": 10, "j": 4,
        "k": 4, "l": 6, "m": 3, "n": 8, "o": 9,
        "p": 3, "r": 6, "s": 6, "t": 5, "u": 3,
        "v": 2, "z": 1
    },

    "Spanish": {
        "a": 13, "b": 2, "c": 5, "d": 6, "e": 14,
        "f": 1, "g": 1, "h": 1, "i": 6, "j": 0,
        "k": 0, "l": 5, "m": 3, "n": 7, "o": 9,
        "p": 3, "q": 1, "r": 7, "s": 8, "t": 5,
        "u": 4, "v": 1, "y": 1, "z": 1
    },

    "Portuguese": {
        "a": 15, "b": 1, "c": 4, "d": 5, "e": 13,
        "f": 1, "g": 1, "h": 1, "i": 6, "j": 0,
        "l": 3, "m": 5, "n": 5, "o": 11, "p": 3,
        "q": 1, "r": 7, "s": 8, "t": 4, "u": 5,
        "v": 2, "x": 0, "z": 1
    },

    "Italian": {
        "a": 12, "b": 1, "c": 5, "d": 4, "e": 12,
        "f": 1, "g": 2, "h": 1, "i": 10, "l": 7,
        "m": 3, "n": 7, "o": 10, "p": 3, "q": 1,
        "r": 6, "s": 5, "t": 6, "u": 3, "v": 2,
        "z": 1
    },

    "French": {
        "a": 8, "b": 1, "c": 3, "d": 4, "e": 15,
        "f": 1, "g": 1, "h": 1, "i": 8, "j": 1,
        "k": 0, "l": 6, "m": 3, "n": 7, "o": 6,
        "p": 3, "q": 1, "r": 7, "s": 8, "t": 7,
        "u": 6, "v": 2, "x": 0, "y": 0, "z": 0
    },

    "English": {
        "a": 8, "b": 2, "c": 3, "d": 4, "e": 13,
        "f": 2, "g": 2, "h": 6, "i": 7, "j": 0,
        "k": 1, "l": 4, "m": 2, "n": 7, "o": 8,
        "p": 2, "q": 0, "r": 6, "s": 6, "t": 9,
        "u": 3, "v": 1, "w": 2, "x": 0, "y": 2,
        "z": 0
    },

    "German": {
        "a": 7, "b": 2, "c": 3, "d": 5, "e": 16,
        "f": 2, "g": 3, "h": 5, "i": 7, "j": 0,
        "k": 1, "l": 3, "m": 3, "n": 10, "o": 3,
        "p": 1, "q": 0, "r": 7, "s": 7, "t": 6,
        "u": 4, "v": 1, "w": 2, "x": 0, "y": 0,
        "z": 1
    },

    "Dutch": {
        "a": 8, "b": 2, "c": 1, "d": 6, "e": 19,
        "f": 1, "g": 3, "h": 2, "i": 7, "j": 2,
        "k": 2, "l": 4, "m": 2, "n": 10, "o": 6,
        "p": 2, "q": 0, "r": 6, "s": 4, "t": 7,
        "u": 2, "v": 3, "w": 2, "x": 0, "y": 0,
        "z": 1
    },

    "Swedish": {
        "a": 9, "b": 2, "c": 2, "d": 5, "e": 10,
        "f": 2, "g": 3, "h": 2, "i": 6, "j": 1,
        "k": 3, "l": 5, "m": 4, "n": 9, "o": 5,
        "p": 2, "r": 8, "s": 7, "t": 8, "u": 2,
        "v": 2, "y": 1
    },

    "Polish": {
        "a": 11, "b": 2, "c": 4, "d": 3, "e": 7,
        "f": 0, "g": 2, "h": 1, "i": 8, "j": 2,
        "k": 4, "l": 2, "m": 3, "n": 7, "o": 8,
        "p": 3, "r": 5, "s": 4, "t": 4, "u": 3,
        "w": 5, "y": 4, "z": 6
    },

    "Turkish": {
        "a": 12, "b": 3, "c": 1, "d": 5, "e": 9,
        "f": 1, "g": 1, "h": 1, "i": 9, "j": 0,
        "k": 5, "l": 6, "m": 4, "n": 8, "o": 3,
        "p": 1, "r": 7, "s": 3, "t": 3, "u": 3,
        "v": 1, "y": 3, "z": 2
    }
}


letters = "abcdefghijklmnopqrstuvwxyz"

total = 0
special = 0

for letter in text:
    if letter in letters:
        total += 1

    elif letter.isalpha():
        total += 1
        special += 1


if total == 0:
    print("No valid letters found.")

else:
    text_frequencies = {}

    for letter in letters:
        count = text.count(letter)
        frequency = count / total * 100
        text_frequencies[letter] = frequency

        print(f"{letter}: {frequency:.2f}%")

    special_frequency = special / total * 100
    text_frequencies["special"] = special_frequency

    best_language = ""
    smallest_difference = float("inf")

    for language in language_frequencies:
        difference = 0

        for letter in letters:
            text_frequency = text_frequencies[letter]

            language_frequency = (
                language_frequencies[language].get(letter, 0)
            )

            difference += abs(
                text_frequency - language_frequency
            )

        print(f"{language} difference: {difference:.2f}")

        if difference < smallest_difference:
            smallest_difference = difference
            best_language = language


    print(f"Detected language: {best_language}")

print("-" * 60)



