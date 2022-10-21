import pandas as pd
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\new_csv_drop1.csv'
df = pd.read_csv(csv_directory)
# df = df.dropna(subset=['decision_date', 'pp_1'])
# df.to_csv(r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\new_csv_drop1.csv')
df.info()