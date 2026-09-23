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
        "a": 12.117, "b": 0.980, "c": 0.776, "d": 3.044,
        "e": 8.995, "f": 1.037, "g": 1.171, "h": 0.384,
        "i": 10.012, "j": 3.501, "k": 4.163, "l": 6.104,
        "m": 2.994, "n": 7.955, "o": 8.779, "p": 2.755,
        "r": 5.914, "s": 6.092, "t": 5.276, "u": 3.183,
        "v": 1.904, "z": 0.494,
        "ĉ": 0.657, "ĝ": 0.691, "ĥ": 0.022,
        "ĵ": 0.055, "ŝ": 0.385, "ŭ": 0.520
    },

    "Spanish": {
        "a": 11.525, "b": 2.215, "c": 4.019, "d": 5.010,
        "e": 13.702, "f": 0.692, "g": 1.768, "h": 1.973,
        "i": 6.247, "j": 0.493, "k": 0.026, "l": 4.967,
        "m": 3.157, "n": 6.712, "o": 8.683, "p": 2.510,
        "q": 0.877, "r": 6.871, "s": 7.977, "t": 4.632,
        "u": 3.927, "v": 1.138, "w": 0.027, "x": 0.515,
        "y": 1.433, "z": 0.467,
        "á": 0.502, "é": 0.433, "í": 0.725,
        "ñ": 0.311, "ó": 0.827, "ú": 0.168,
        "ü": 0.012
    },

    "Portuguese": {
        "a": 14.634, "b": 1.043, "c": 3.882, "d": 4.992,
        "e": 13.101, "f": 1.023, "g": 1.303, "h": 1.281,
        "i": 6.186, "j": 0.379, "k": 0.015, "l": 2.779,
        "m": 4.738, "n": 4.446, "o": 9.735, "p": 2.523,
        "q": 1.204, "r": 6.530, "s": 6.805, "t": 4.336,
        "u": 3.639, "v": 1.575, "w": 0.037, "x": 0.453,
        "y": 0.006, "z": 0.470,
        "à": 0.072, "â": 0.562, "á": 0.118,
        "ã": 0.733, "ç": 0.530, "é": 0.337,
        "ê": 0.450, "í": 0.132, "ó": 0.296,
        "ô": 0.635, "õ": 0.040, "ú": 0.207,
        "ü": 0.026
    },

    "Italian": {
        "a": 11.745, "b": 0.927, "c": 4.501, "d": 3.736,
        "e": 11.792, "f": 1.153, "g": 1.644, "h": 0.136,
        "i": 10.143, "j": 0.011, "k": 0.009, "l": 6.510,
        "m": 2.512, "n": 6.883, "o": 9.832, "p": 3.056,
        "q": 0.505, "r": 6.367, "s": 4.981, "t": 5.623,
        "u": 2.813, "v": 2.097, "w": 0.033, "x": 0.008,
        "y": 0.020, "z": 1.181,
        "à": 0.635, "è": 0.263, "ì": 0.030,
        "í": 0.030, "ò": 0.002, "ù": 0.166,
        "ú": 0.166
    },

    "French": {
        "a": 7.636, "b": 0.901, "c": 3.260, "d": 3.669,
        "e": 14.715, "f": 1.066, "g": 0.866, "h": 0.937,
        "i": 7.529, "j": 0.813, "k": 0.074, "l": 5.456,
        "m": 2.968, "n": 7.095, "o": 5.796, "p": 2.521,
        "q": 1.362, "r": 6.693, "s": 7.948, "t": 7.244,
        "u": 6.311, "v": 1.838, "w": 0.049, "x": 0.427,
        "y": 0.708, "z": 0.326,
        "à": 0.486, "â": 0.051, "ç": 0.085,
        "è": 0.271, "é": 1.504, "ê": 0.218,
        "ë": 0.008, "î": 0.045, "ï": 0.005,
        "ô": 0.023, "ù": 0.058, "û": 0.060
    },

    "English": {
        "a": 8.167, "b": 1.492, "c": 2.782, "d": 4.253,
        "e": 12.702, "f": 2.228, "g": 2.015, "h": 6.094,
        "i": 6.966, "j": 0.153, "k": 0.772, "l": 4.025,
        "m": 2.406, "n": 6.749, "o": 7.507, "p": 1.929,
        "q": 0.095, "r": 5.987, "s": 6.327, "t": 9.056,
        "u": 2.758, "v": 0.978, "w": 2.360, "x": 0.150,
        "y": 1.974, "z": 0.074
    },

    "German": {
        "a": 6.516, "b": 1.886, "c": 2.732, "d": 5.076,
        "e": 16.396, "f": 1.656, "g": 3.009, "h": 4.577,
        "i": 6.550, "j": 0.268, "k": 1.417, "l": 3.437,
        "m": 2.534, "n": 9.776, "o": 2.594, "p": 0.670,
        "q": 0.018, "r": 7.003, "s": 7.270, "t": 6.154,
        "u": 4.166, "v": 0.846, "w": 1.921, "x": 0.034,
        "y": 0.039, "z": 1.134,
        "ä": 0.578, "ö": 0.443, "ü": 0.995,
        "ß": 0.307
    },

    "Dutch": {
        "a": 7.490, "b": 1.580, "c": 1.240, "d": 5.930,
        "e": 18.910, "f": 0.810, "g": 3.400, "h": 2.380,
        "i": 6.500, "j": 1.460, "k": 2.250, "l": 3.570,
        "m": 2.210, "n": 10.030, "o": 6.060, "p": 1.570,
        "q": 0.009, "r": 6.410, "s": 3.730, "t": 6.790,
        "u": 1.990, "v": 2.850, "w": 1.520, "x": 0.036,
        "y": 0.035, "z": 1.390
    },

    "Swedish": {
        "a": 9.383, "b": 1.535, "c": 1.486, "d": 4.702,
        "e": 10.149, "f": 2.027, "g": 2.862, "h": 2.090,
        "i": 5.817, "j": 0.614, "k": 3.140, "l": 5.275,
        "m": 3.471, "n": 8.542, "o": 4.482, "p": 1.839,
        "q": 0.020, "r": 8.431, "s": 6.590, "t": 7.691,
        "u": 1.919, "v": 2.415, "w": 0.142, "x": 0.159,
        "y": 0.708, "z": 0.070,
        "å": 1.340, "ä": 1.800, "ö": 1.310
    },

    "Polish": {
        "a": 8.965, "b": 1.482, "c": 3.988, "d": 3.293,
        "e": 7.921, "f": 0.312, "g": 1.377, "h": 1.072,
        "i": 8.286, "j": 2.343, "k": 3.411, "l": 2.136,
        "m": 2.911, "n": 5.600, "o": 7.590, "p": 3.101,
        "q": 0.003, "r": 4.571, "s": 4.263, "t": 3.966,
        "u": 2.347, "v": 0.034, "w": 4.549, "x": 0.019,
        "y": 3.857, "z": 5.620,
        "ą": 1.021, "ć": 0.448, "ę": 1.131,
        "ł": 1.746, "ń": 0.185, "ó": 0.823,
        "ś": 0.683, "ź": 0.061, "ż": 0.885
    },

    "Turkish": {
        "a": 11.920, "b": 2.844, "c": 0.963, "d": 4.706,
        "e": 8.912, "f": 0.461, "g": 1.253, "h": 1.212,
        "i": 8.600, "j": 0.034, "k": 4.683, "l": 5.922,
        "m": 3.752, "n": 7.487, "o": 2.476, "p": 0.886,
        "q": 0.000, "r": 6.722, "s": 3.014, "t": 3.314,
        "u": 3.235, "v": 0.959, "w": 0.000, "x": 0.000,
        "y": 3.336, "z": 1.500,
        "ç": 1.156, "ğ": 1.125, "ı": 5.114,
        "ö": 0.777, "ş": 1.780, "ü": 1.854
    }
}


# Normal letters
letters = "abcdefghijklmnopqrstuvwxyz"

# Store special characters
special = ""

total = 0


# Count normal and special letters
for letter in text:

    if letter in letters:
        total += 1

    elif letter.isalpha():
        total += 1

        if letter not in special:
            special += letter


if total == 0:
    print("No valid letters found.")

else:

    text_frequencies = {}


    # Calculate normal letter frequencies
    for letter in letters:

        count = text.count(letter)

        frequency = count / total * 100

        text_frequencies[letter] = frequency

        print(f"{letter}: {frequency:.2f}%")


    # Calculate special character frequencies
    # They are stored, but NOT printed
    for letter in special:

        count = text.count(letter)

        frequency = count / total * 100

        text_frequencies[letter] = frequency


    best_language = ""

    smallest_difference = float("inf")


    # Compare each language
    for language in language_frequencies:

        difference = 0


        # Compare normal letters
        for letter in letters:

            text_frequency = text_frequencies[letter]

            language_frequency = (
                language_frequencies[language].get(letter, 0)
            )

            difference += abs(
                text_frequency - language_frequency
            )


        # Compare special characters
        for letter in special:

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



