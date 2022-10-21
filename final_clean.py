import pandas as pd
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\aftr_pay_packet_to.csv'
df = pd.read_csv(csv_directory)
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
df.to_csv(r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\final_Clean.csv')