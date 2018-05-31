import pandas
import re

name_df = pandas.read_csv(input("Input file: "))

first_regex = re.compile(r"^\w+ ")

last_regex = re.compile(r" [\w-]+$")

#name_df["First Name"] = name_df["Name"].split(" ")[0]
name_df["First Name"] = name_df["Name"].replace(last_regex,"")

columns = name_df.columns.tolist()

columns = columns[-1:] + columns[:-1]
name_df = name_df[columns]

name_df.to_csv(input("Output File: " ))