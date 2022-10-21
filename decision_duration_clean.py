import pandas as pd
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\CSVs\duration_csv.csv'
df = pd.read_csv(csv_directory)
cnt = 0
for i in range(1,len(df["decision_duration"])):
    if df.loc[i,"decision_duration"] == "0:00:00" :
        df.loc[i,"decision_duration"] = 0
df.to_csv(r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\CSVs\duration_csv_2.csv')
