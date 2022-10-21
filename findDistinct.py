import pandas as pd
import os
from datetime import datetime

data,data2,duration,sponsorship_type,render_date,decision_date,acceptance_duration= [],[],[],[],[],[],[]
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\employment_onsite_opportunity.csv'
df = pd.read_csv(csv_directory)
data.extend(df['appointment_start_date'].tolist())
data2.extend(df['appointment_end_date'].tolist())
sponsorship_type.extend(df['sponsorship_type'].tolist())
render_date.extend(df['render_date'].tolist())
decision_date.extend(df['decision_date'].tolist())
print(type(data[0])) #check type
"""for i in range(1,len(data)):
    if(not(data[i]!=data[i]) and not(data2[i]!=data2[i]) ): #skip all nan values
        data[i] = str(data[i]).replace('T'," ")
        data[i] = datetime.strptime(data[i], '%Y-%m-%d %H:%M:%S')
        data2[i] = str(data2[i]).replace('T'," ")
        data2[i] = datetime.strptime(data2[i], '%Y-%m-%d %H:%M:%S')
        duration.append(str(data2[i] - data[i]).split(',')[0])"""
    #print(duration[i-1])
data_unique = list(set(sponsorship_type))
print(data_unique,len(data_unique))
"""for i in range(1,len(render_date)):
    if(not(render_date[i]!=render_date[i]) and not(decision_date[i]!=decision_date[i]) ):
        render_date[i] = str(render_date[i]).replace('T'," ")
        render_date[i] = datetime.strptime(render_date[i], '%Y-%m-%d %H:%M:%S')
        decision_date[i] = str(decision_date[i]).replace('T'," ")
        decision_date[i] = datetime.strptime(decision_date[i], '%Y-%m-%d %H:%M:%S')
        acceptance_duration.append(str(decision_date[i] - render_date[i]).split(',')[0])"""
""" for items in set(acceptance_duration):
    print(items);
""""""for column_name in df.head(1):
    print(column_name)"""""""""


