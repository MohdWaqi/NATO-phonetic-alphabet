import pandas

######################### Reading the phonetic alphabet from the csv file ################################

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_code():
    user = input("Enter a word: ").upper()
    try:
        phonetic_code = [phonetic_alphabet[letter] for letter in user]

########################## Catching key error if user type other than alphabet #########################

    except KeyError:
        print("Type only alphabet")
        generate_code()
    else:
        print(phonetic_code)


generate_code()
