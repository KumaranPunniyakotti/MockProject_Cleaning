from cmath import nan
import pandas as pd
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\new_csv.csv'
df = pd.read_csv(csv_directory)
# hourly,monthly,Weekly,BiWeekly,yearly = [],[],[],[],[]
# for i in range(1,len(df["pp_1"])):
#     if(df.loc[i,"pp_unit_1"] == "Year"):
#         yearly.append(float(df.loc[i,"pp_1"]))
#         continue
#     if(df.loc[i,"pp_unit_1"] == "Hour"):
#         hourly.append(float(df.loc[i,"pp_1"]))
#         continue
#     if(df.loc[i,"pp_unit_1"] == "Month"):
#         monthly.append(float(df.loc[i,"pp_1"]))  
#         continue
#     if(df.loc[i,"pp_unit_1"] == "Week"):
#         Weekly.append(float(df.loc[i,"pp_1"]))
#         continue
#     if(df.loc[i,"pp_unit_1"] == "Bi-Weekly"):
#         BiWeekly.append(float(df.loc[i,"pp_1"]))
#         continue
# hourdf = pd.DataFrame(hourly,columns=["Hour"])
# monthdf = pd.DataFrame(monthly,columns=["Month"])
# weekdf = pd.DataFrame(Weekly,columns=["Week"])
# biWeekdf = pd.DataFrame(BiWeekly,columns=["Bi-Weekly"])
# yeardf = pd.DataFrame(yearly,columns=["Year"])
# hourlymean = hourdf.mean()
# monthlymean = monthdf.mean()
# weeklymean = weekdf.mean()
# biweeklymean = biWeekdf.mean()
# yearlymean = yeardf.mean()
"""
min of  4.55 1500.0 27.63 13.02 0.0
max of  166400.0 166400.0 106330.0 64500.0 6144361443.0
hourlymean Hour    539.654227
dtype: float64 monthlymean Month    10547.498774
dtype: float64 weeklymean Week    2964.146282
dtype: float64 biweeklymean Bi-Weekly    4263.298696
dtype: float64 yearlymean Year    86200.933543
dtype: float64
"""
# print("min of ",min(hourly),min(monthly),min(Weekly),min(BiWeekly),min(yearly))
# print("max of ",max(hourly),max(monthly),max(Weekly),max(BiWeekly),max(yearly))
# print("hourlymean",hourlymean,"monthlymean",monthlymean,"weeklymean",weeklymean,"biweeklymean",biweeklymean,"yearlymean",yearlymean)
# print([i for i in hourly])
    
# nullcnt = 0
# floatcnt = 0
# val = df.isnull()

for i in range(1,len(df["pp_1"])):
    # if(not(pd.isna(df.loc[i,"pp_1"]))):
    value = df.loc[i,"pp_1"]
    # if(value !=  "" and type(value) != float):
    if(type(value) != float):
        if(value.replace('.','').isdigit()):
            df.loc[i,"pp_1"] = float(value)
        # else:
            # print(df.loc[i,"pp_1"])
            # nextColumn = df.loc[i,"pp_unit_1"]
            # if( nextColumn == "Year"):
            #     df.loc[i,"pp_1"] = 86200.933543
            #     continue
            # if(nextColumn == "Hour"):
            #     df.loc[i,"pp_1"] = 539.654227
            #     continue
            # if(nextColumn == "Month"):
            #     df.loc[i,"pp_1"] = 10547.498774
            #     continue
            # if(nextColumn == "Week"):
            #     df.loc[i,"pp_1"] = 2964.146282 
            #     continue
            # if(nextColumn == "Bi-Weekly"):
            #     df.loc[i,"pp_1"] = 4263.298696
            #     continue


        # floatcnt+=1
    else:
        nextColumn = df.loc[i,"pp_unit_1"]
        # print("in else",i)
        if( nextColumn == "Year"):
            df.loc[i,"pp_1"] = 86200.933543
            continue
        if(nextColumn == "Hour"):
            df.loc[i,"pp_1"] = 539.654227
            continue
        if(nextColumn == "Month"):
            df.loc[i,"pp_1"] = 10547.498774
            continue
        if(nextColumn == "Week"):
            df.loc[i,"pp_1"] = 2964.146282 
            continue
        if(nextColumn == "Bi-Weekly"):
            df.loc[i,"pp_1"] = 4263.298696
            continue
        # nullcnt+=1
df.to_csv(r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\new_csv1.csv')

        
# print(nullcnt,floatcnt)
# df["pp_1"].info()

# print(df["decision_date"].isna().sum())