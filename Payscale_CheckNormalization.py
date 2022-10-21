import pandas as pd
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\new_csv2.csv'
df = pd.read_csv(csv_directory)
# fl,st = 0,0
# for i in range(1,len(df["pp_1"])):
#     value = df.loc[i,"pp_1"]
#     if(type(value) == float):
#         fl += 1
#         continue
#     if(type(value) == str):
#         st += 1
#         continue
# print(df["pp_1"].isna().sum())
# print(fl,st)
    
# for i in range(1,len(df["pp_1"])):
#     # if(not(pd.isna(df.loc[i,"pp_1"]))):
#     value = df.loc[i,"pp_1"]
#     # if(value !=  "" and type(value) != float):
#     if(type(value) != float):
#         if(value.replace('.','').isdigit()):
#             pass
#         else:
#             df.loc[i,"pp_1"] = "NA"

# fl,st = 0,0
# for i in range(1,len(df["pp_1"])):
#     value = df.loc[i,"pp_1"]
#     # if(type(value) == float):
#     #     fl += 1
#     #     continue
#     # if(type(value) == str):
#     #     st += 1
#     #     continue
#     if(value == "NA"):
#         fl+=1
# print(fl,st)
# df.to_csv(r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\new_csv2.csv')
print(df["pp_1"].isna().sum())