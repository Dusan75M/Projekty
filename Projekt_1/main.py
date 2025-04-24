"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Dušan Machů
email: dumadum@centrum.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
    "bob": 123,
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

separator = "-" * 40

username = input("username: ")
password = input("password: ")

if username in users and password in str(users[username]):
    print(separator)
    print("Welcome to the app,", username)
else:
    print("unregistered user, terminating the program..")
    quit()

print("We have", len(TEXTS), "texts to be analyzed.")
print(separator)

text_range = list(range(1, len(TEXTS)+1))

text_number = input("Enter a number btw. " + str(text_range[0]) + " and " + str(text_range[-1]) + " to select: ")

if text_number.isnumeric():
    if int(text_number) in text_range:
        print(separator)
    else:
        print("Invalid text number, terminating the program..")
        quit()
else:
    print("Invalid character, terminating the program..")
    quit()

chosen_text = TEXTS[int(text_number)-1]

clean_text = []

for word in chosen_text.split():
    clean_word = word.strip(",.:;'")
    clean_text.append(clean_word)

words_number = len(clean_text)

print("There are " + str(words_number) + " words in the selected text.")

titlecase_words = []

for t_word in clean_text:
    if t_word.istitle():
        titlecase_words.append(t_word)

print("There are " + str(len(titlecase_words)) + " titlecase words.")

uppercase_words = []

for u_word in clean_text:
    if u_word.isupper():
        uppercase_words.append(u_word)

print("There are " + str(len(uppercase_words)) + " uppercase words.")

lowercase_words = [l_word for l_word in clean_text if l_word.islower()]

print("There are " + str(len(lowercase_words)) + " lowercase words.")

numeric_string = [number for number in clean_text if number.isnumeric()]

print("There are " + str(len(numeric_string)) + " numeric strings.")

numeric_integer = [int(number) for number in numeric_string]
sum_numbers = sum(numeric_integer)

print("The sum of all the numbers " + str(sum_numbers))
print(separator)

word_length = {}

for word_l in clean_text:
    length = len(word_l)
    if length in word_length:
        word_length[length] += 1
    else:
        word_length[length] = 1

length_list_sorted = [word_length[key] for key in sorted(word_length.keys())]

print("LEN|" + "OCCURENCES".center(15) + "|NR.", separator, sep="\n")

for index, length_w in enumerate(length_list_sorted, 1):
    print(f"{index:>3}|" + ('*'*length_w).ljust(20) + f"|{length_w}", sep="\n")
