import pandas as pd
from datetime import datetime
render_date,decision_date,acceptance_duration,appointment_start_date,appointment_end_date,job_duration= [],[],[],[],[],[]
csv_directory = r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\CSVs\final_Clean.csv'
df = pd.read_csv(csv_directory)
render_date.extend(df['render_date'].tolist())
decision_date.extend(df['decision_date'].tolist())
appointment_start_date.extend(df['appointment_start_date'].tolist())
appointment_end_date.extend(df['appointment_end_date'].tolist())
for i in range(len(render_date)): 
    render_date[i] = str(render_date[i]).replace('T'," ")
    render_date[i] = datetime.strptime(render_date[i], '%Y-%m-%d %H:%M:%S')
    decision_date[i] = str(decision_date[i]).replace('T'," ")
    decision_date[i] = datetime.strptime(decision_date[i], '%Y-%m-%d %H:%M:%S')
    acceptance_duration.append(str(str(decision_date[i] - render_date[i]).split(',')[0]).split(" ")[0])
for i in range(len(appointment_end_date)):
    appointment_start_date[i] = str(appointment_start_date[i]).replace('T'," ")
    appointment_start_date[i] = datetime.strptime(appointment_start_date[i], '%Y-%m-%d %H:%M:%S')
    appointment_end_date[i] = str(appointment_end_date[i]).replace('T'," ")
    appointment_end_date[i] = datetime.strptime(appointment_end_date[i], '%Y-%m-%d %H:%M:%S')
    job_duration.append(str(str(appointment_end_date[i] - appointment_start_date[i]).split(',')[0]).split(" ")[0])
df['acceptance_duration'] = acceptance_duration
df['job_duration'] = job_duration
df.to_csv(r'C:\Users\kumar\Downloads\employment_onsite_opportunity-20220311T165157Z-001\CSVs\duration_csv.csv')
