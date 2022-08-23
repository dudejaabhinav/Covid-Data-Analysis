#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import math
import datetime
pd.options.mode.chained_assignment = None
data = pd.read_csv('cowin_vaccine_data_districtwise.csv', header = [0], skiprows = [1])
com = pd.read_csv('cowin_vaccine_data_districtwise.csv', header = [0], nrows = 1)
l = com.loc[0]
n = list(data)
f_dis = pd.DataFrame(columns = ['districtid', '14/08/2021', '07/08/2021'])
f_dis['districtid'] = data['District_Key']
k = 0
for i in range(len(l)):
    if (l[i] == 'First Dose Administered') and ((n[i].split('.')[0] == '07/08/2021')):
        f_dis['07/08/2021'] = data[n[i]]
    elif (l[i] == 'First Dose Administered') and ((n[i].split('.')[0] == '14/08/2021')):
        f_dis['14/08/2021'] = data[n[i]]


st_id = list(data['State_Code'])
d14_data = list(f_dis['14/08/2021'])
d07_data = list(f_dis['07/08/2021'])

us_id = list()
dm_data = list()
dl_data = list()
un = None
d14sum, d07sum = 0, 0

for i in range(len(st_id)):
    if un != st_id[i]:
        if un != None:
            us_id.append(un)
            dm_data.append(d14sum)
            dl_data.append(d07sum)
            d14sum, d07sum = 0, 0
        un = st_id[i]
    d14sum = d14sum + d14_data[i]
    d07sum = d07sum + d07_data[i]
us_id.append(un)
dm_data.append(d14sum)
dl_data.append(d07sum)

f_stt = pd.DataFrame(columns = ['stateid', '14/08/2021', '07/08/2021'])
f_stt['stateid'] = us_id
f_stt['14/08/2021'] = dm_data
f_stt['07/08/2021'] = dl_data


cols = ['Level', 'Name', 'TRU', 'TOT_P']
pop_data = pd.read_csv('DDW_PCA0000_2011_Indiastatedist.csv', usecols = cols)
crct = pd.read_csv('old_to_new_map.csv')
for i in range(len(crct['old'])):
    str1 = str(crct['old'].loc[i]).split('/')[1]
    str2 = str(crct['new'].loc[i]).split('/')[1]
    if str1 == str2:
        continue
    else:
        pop_data['Name'].loc[pop_data['Name'] == str1] = str2

p_data = pop_data.loc[pop_data['TRU'] == 'Total']

p_stt = p_data.loc[p_data['Level'] == 'STATE']
p = list((p_stt['TOT_P'].loc[p_stt['Name'] == 'DAMAN AND DIU']))[0] + list((p_stt['TOT_P'].loc[p_stt['Name'] == 'DADRA AND NAGAR HAVELI']))[0]
p_stt.loc[len(p_stt.index)] = ['STATE', 'DADRA AND NAGAR HAVELI AND DAMAN AND DIU', 'TOTAL', p]
p_stt.sort_values(by = 'Name')
p_stt.index = [i for i in range(0,len(p_stt['Name']))]


ku = list(data.State.unique())
ku_id = list(data.State_Code.unique())

dic_sid = {}
for key in ku:
    for value in ku_id:
        k = key.lower()
        dic_sid[k] = value
        ku_id.remove(value)
        break  

id_list = list()
rate = list()
pop_left = list()
for i in range(0,len(p_stt['Name'])):
    nam = p_stt['Name'].loc[i].lower()
    
    if nam in dic_sid.keys():
        id_list.append(dic_sid[nam])
        a = list(f_stt['14/08/2021'].loc[f_stt['stateid']  == dic_sid[nam]])[0]
        b = list(f_stt['07/08/2021'].loc[f_stt['stateid']  == dic_sid[nam]])[0]
        rate.append((a-b)/7)
        pl = float(p_stt['TOT_P'].loc[i]) - a
        if pl < 0:
            pop_left.append(0)
        else:
            pop_left.append(pl)
        
cv = pd.DataFrame(columns = ['stateid', 'populationleft', 'rateofvaccination', 'date'])
cv['stateid'] = id_list
cv['populationleft'] = pop_left
cv['rateofvaccination'] = rate
l = cv['populationleft'] / cv['rateofvaccination']

d = []
x = datetime.datetime(2021, 8, 14)
for i in l:
    d.append(x + datetime.timedelta(days=(math.ceil(i))))


cv['date'] = d
cv = cv.sort_values(by = 'stateid')
cv.to_csv('output-files/complete-vaccination.csv', index = False)


# In[ ]:




