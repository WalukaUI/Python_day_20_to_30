
# with open("./weather_data.csv", mode="r") as csv_file:
#     list_1 = csv_file.readlines()
#     print(list_1[1:len(list_1)])


#****************easy way********************

# import csv
#
# with open("./weather_data.csv", mode="r") as csv_file:
#     data = csv.reader(csv_file)
#     tempature = []
#     for line in data:
#         if line[1] != 'temp':
#             tempature.append(int(line[1]))
#     print(tempature)


#****************Using pandas********************

import pandas

data = pandas.read_csv("./weather_data.csv")
maxx = data["temp"].max()
datalarge = data[data["temp"] == maxx]
print(datalarge)

monday = data[data.day == "Monday"]
print(monday)

#**********write a file*******
datadict = {
    "students" : ["amy", "james", "angi"],
    "scores" : [5,6,15]
}
datafile = pandas.DataFrame(datadict)
datafile.to_csv("file_name.csv")