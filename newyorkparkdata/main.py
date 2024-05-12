import pandas

datafile = pandas.read_csv("./2018_Central_Park.csv")

gray_count = len(datafile[datafile["Primary Fur Color"] == "Gray"])
cinnoman_count = len(datafile[datafile["Primary Fur Color"] == "Cinnamon"])
black_count = len(datafile[datafile["Primary Fur Color"] == "Black"])

final = {"colors":["Gray", "Cinnamon", "Black"],
         "count":[gray_count, cinnoman_count, black_count]}

print(final)

file = pandas.DataFrame(final)
file.to_csv("report.csv")
