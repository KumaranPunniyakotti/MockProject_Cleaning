import pandas as pd
import math
import os
from datetime import datetime
render_date,decision_date,acceptance_duration= [],[],[]
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\new_csv.csv'
df = pd.read_csv(csv_directory)
render_date.extend(df['render_date'].tolist())
decision_date.extend(df['decision_date'].tolist())
for i in range(1,len(render_date)):
    if(decision_date[i] is not None and not(decision_date[i] != decision_date[i])):
        render_date[i] = str(render_date[i]).replace('T'," ")
        render_date[i] = datetime.strptime(render_date[i], '%Y-%m-%d %H:%M:%S')
        decision_date[i] = str(decision_date[i]).replace('T'," ")
        #print(decision_date[i])
        decision_date[i] = datetime.strptime(decision_date[i], '%Y-%m-%d %H:%M:%S')
        acceptance_duration.append(str(decision_date[i] - render_date[i]).split(',')[0])
for items in set(acceptance_duration):
    print(items);
print(len(acceptance_duration))

r'''
inn = 0
f = 0
for i in range(1,len(render_date)):
    if(isinstance(decision_date[i],float)):
        f+=1
        #print(decision_date[i])
        decision_date[i] = None
        continue
    if(decision_date[i].isdigit()):
        if(isinstance(int(decision_date[i]),int)):
            #print(decision_date[i])
            inn+=1
            continue 
print(inn,f)
    #if(not(render_date[i]!=render_date[i]) and not(decision_date[i]!=decision_date[i]) ):
        #render_date[i] = str(render_date[i]).replace('T'," ")
        #render_date[i] = datetime.strptime(render_date[i], '%Y-%m-%d %H:%M:%S')
        #decision_date[i] = str(decision_date[i]).replace('T'," ")
        #decision_date[i] = datetime.strptime(decision_date[i], '%Y-%m-%d %H:%M:%S')
        #acceptance_duration.append(str(decision_date[i] - render_date[i]).split(',')[0])

for i in range(len(df)):
    if(isinstance(df.loc[i,"decision_date"],float) or df.loc[i,"decision_date"].isdigit()):
    #if(isinstance(df.loc[i,"decision_date"],float) ):
        df.loc[i,"decision_date"] = "NA"
        #print(df.loc[i,"decision_date"])
#df.to_csv(r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\employment_onsite_opportunity\new_csv.csv')
#print(df.describe())
counter = 0
for i in range(len(df)):
    if(df.loc[i,"decision_date"] == "NA"):
        counter +=1
print("endd",counter)
'''
