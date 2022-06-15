import pandas
import sys
FILEPATH = r"nato_phonetic_alphabet.csv"
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass
#
# student_data_frame = pandas.DataFrame(student_dict)
#
# # Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

csv_data = pandas.read_csv(FILEPATH)
csv_data = pandas.DataFrame.from_dict(csv_data)
print(csv_data)
nato_dict = {row.letter: row.code for (index, row) in csv_data.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = str(input("Enter a word to be converted to NATO code: ")).upper()
word_list = list(word)
for i in word_list:
    try:
        nato_word_list = [nato_dict[letter] for letter in word_list]
    except KeyError:
        print("Please only enter letters.")
        sys.exit(1)
    else: print(nato_word_list)
