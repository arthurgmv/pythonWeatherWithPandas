import pandas as pd
data = pd.read_csv("weather_data.csv")

temp_lista = data["temp"].to_list
print(data["temp"].mean().round(2))

