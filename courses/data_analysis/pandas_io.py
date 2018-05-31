import pandas

dataframe = pandas.read_csv("food_info.csv")

dataframe.to_csv("output.csv")