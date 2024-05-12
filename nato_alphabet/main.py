import pandas

name = input("please type a name? ").upper()
data =pandas.read_csv("./nato_phonetic_alphabet.csv")

new_data = { row.letter: row.code for (index, row) in data.iterrows()}
print(new_data)
name_list = [new_data[letter] for letter in name]
print(name_list)
