# numbers = [1,2,3]
# new_num = [n + 2 for n in numbers]
# print(new_num)
#
# new_range = [x * 2 for x in range(1,5)]
# print(new_range)
#
# names = ["Alex", "Beth", "Saman", "kamal", "Tharanga", "Rajapaksha"]
# new_names = [x for x in names if len(x) < 5]
# print(new_names)
#
# newnames = [x.upper() for x in names]
# print(newnames)
import random
import pandas
with open("file.txt") as txt1:
    file1 = txt1.readlines()
    print(file1)

with open("file2.txt") as txt2:
    file2 = txt2.readlines()
    print(file2)

filtered = [x for x in file2 if x in file1]
print(filtered)

names = ["ranga", "saman", "kamal" , "nimal"]

new_dict = {x: random.randrange(10,100) for x in names}
print(new_dict)

passed = { key: val for (key, val) in new_dict.items() if val > 50}
print(passed)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentolist = sentence.split()
print(sentolist)
sentodict = {name:len(name) for name in sentolist }
print(sentodict)

temp = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
new_c_temp = {day: val * 9/5 + 32 for (day, val) in temp.items()}
print(new_c_temp)



student_dict = {
    "student" : ["ranga", "jaya", "kamal"],
    "score" : [70, 10, 20]
}
student_data_frame = pandas.DataFrame(student_dict)

for(index, row) in student_data_frame.iterrows():
    if row.student == "ranga":
        print(row.score)