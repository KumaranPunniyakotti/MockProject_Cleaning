from cmath import isnan, nan
from re import T
import pandas as pd
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\aftr_pincode2.csv'
df = pd.read_csv(csv_directory)
for i in range(1,len(df["pay_packet_to"])):
    if(isnan(df.loc[i,"pay_packet_to"])):
        df.loc[i,"pay_packet_to"] = df.loc[i,"pay_packet_from"]
df.dropna(subset=['pay_packet_to'],inplace=True)
df.reset_index(drop=True, inplace=True)
df.to_csv(r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\aftr_pay_packet_to.csv')