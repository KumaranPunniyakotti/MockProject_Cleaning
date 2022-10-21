from calendar import c
import pandas as pd
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\new_csv.csv'
df = pd.read_csv(csv_directory)
df["company_name"].fillna(value= "NA",inplace=True)
# count = 0
# for i in range(len(df["company_name"])):
#     if(df.loc[i,"company_name"]== "NA"):
#         count += 1
# print(count)