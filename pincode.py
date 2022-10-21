from operator import le
import pandas as pd
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\new_csv_drop1.csv'
df = pd.read_csv(csv_directory)
df.dropna(subset=["company_pincode"],inplace=True)
df.reset_index(drop=True, inplace=True)
for i in range(1,len(df["company_pincode"])):
    value = df.loc[i,"company_pincode"].split('-')[0]
    if(value.isdigit()):
        if(len(value) < 5):
            df.loc[i,"company_pincode"] = value.rjust(5,'0')
        elif(len(value) > 5):
            df.loc[i,"company_pincode"] = value[:5]
        else:
            df.loc[i,"company_pincode"] = value
    else:
        df.drop(i, axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
fivelen,normlen = 0,0
for i in range(1,len(df["company_pincode"])):
    normlen += 1
    if(len(df.loc[i,"company_pincode"]) == 5):
        fivelen+=1

print(normlen,fivelen)
df.to_csv(r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\aftr_pincode2.csv')


# print("90".rjust(5,'0'))
# print("9009887".split('-')[0].rjust(5,'0'))
