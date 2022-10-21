import pandas as pd
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\CSVs\duration_csv_2.csv'
df = pd.read_csv(csv_directory)
for i in range(len(df["pp_1"])):
    if(df.loc[i,"pp_unit_1"] == "Hour"):
        df.loc[i,"pp_1"] = float(df.loc[i,"pp_1"])*8*260
        continue
    if(df.loc[i,"pp_unit_1"] == "Month"):
        df.loc[i,"pp_1"] = float(df.loc[i,"pp_1"])*12
        continue
    if(df.loc[i,"pp_unit_1"] == "Week"):
        df.loc[i,"pp_1"] = float(df.loc[i,"pp_1"])*52
        continue
    if(df.loc[i,"pp_unit_1"] == "Bi-Weekly"):
        df.loc[i,"pp_1"] = float(df.loc[i,"pp_1"])*26
        continue
df.to_csv(r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\CSVs\pay_packet_normalized1.csv')