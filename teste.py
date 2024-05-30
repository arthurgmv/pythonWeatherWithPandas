# #versão tradicional:
# with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)
#
# #Usando a csv lib:
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#Usando pandas:
import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])
