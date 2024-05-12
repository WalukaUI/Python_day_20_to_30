#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open('./Output/ReadyToSend/example.txt', mode="r") as output:
    txt = output.read()

with open('./Input/Names/invited_names.txt', mode="r") as names:
    for single_line in names:
        line = single_line.strip()
        with open(f"./Output/ReadyToSend/letter_for_{line}.txt", mode="w") as output_letter:
            output_letter.write(f"{txt[0:4]} {line}, \n {txt[11:len(txt)]}")
