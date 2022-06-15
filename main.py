import pandas
import sys
FILEPATH = r"nato_phonetic_alphabet.csv"

csv_data = pandas.read_csv(FILEPATH)
csv_data = pandas.DataFrame.from_dict(csv_data)
print(csv_data)
nato_dict = {row.letter: row.code for (index, row) in csv_data.iterrows()}
print(nato_dict)

word = str(input("Enter a word to be converted to NATO code: ")).upper()
word_list = list(word)
for i in word_list:
    try:
        nato_word_list = [nato_dict[letter] for letter in word_list]
    except KeyError:
        print("Please only enter letters.")
        sys.exit(1)
    else: print(nato_word_list)
