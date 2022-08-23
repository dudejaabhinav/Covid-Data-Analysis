#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None
data = pd.read_csv('cowin_vaccine_data_districtwise.csv',header = [0],skiprows = [1])
com = pd.read_csv('cowin_vaccine_data_districtwise.csv',header = [0],nrows = 1)
l = com.loc[0]
n = list(data)
df = pd.DataFrame(columns = ['districtid'])
df['districtid'] = data['District_Key']

k = 0
n1, n2 = list(), list()
for i in range(len(l)):
    if l[i] == 'First Dose Administered':
        n1.append(n[i])
    elif l[i] == 'Second Dose Administered':
        n2.append(n[i])

n1_df = data[n1]
n2_df = data[n2]
new_data1 = pd.concat((df, n1_df), axis = 1)
new_data2 = pd.concat((df, n2_df), axis = 1)





n_d = {}
n = list(new_data1)
for i in range(1,len(n)):
    a = n[i].split('.')[0]
    n_d[n[i]] = a
    

new_data1 = new_data1.rename(columns = n_d, inplace = False)



n_d = {}
n = list(new_data2)
for i in range(1,len(n)):
    a = n[i].split('.')[0]
    n_d[n[i]] = a
    

new_data2 = new_data2.rename(columns = n_d, inplace = False)


ind = new_data1.columns.get_loc('17/08/2021')
new_data1.drop(new_data1.iloc[:, ind:], inplace = True, axis = 1)
ind = new_data2.columns.get_loc('17/08/2021')
new_data2.drop(new_data2.iloc[:, ind:], inplace = True, axis = 1)



new_data1 = new_data1.groupby(['districtid']).sum()
new_data2 = new_data2.groupby(['districtid']).sum()




week_data1 = pd.DataFrame(columns = ['districtid'])
week_data1['districtid'] = new_data1.index
week_data1['1'] = list(new_data1['16/01/2021'])

week_data2 = pd.DataFrame(columns = ['districtid'])
week_data2['districtid'] = new_data2.index
week_data2['1'] = list(new_data2['16/01/2021'])

for i in range(8, len(new_data1.columns), 7):
    j = str(int((i-1)/7+1))
    week_data1[j] = np.array(new_data1.iloc[:,i]) - np.array(new_data1.iloc[:,i-7])
    week_data2[j] = np.array(new_data2.iloc[:,i]) - np.array(new_data2.iloc[:,i-7])

k = 0
dn = 0
week_data = pd.DataFrame(columns = ['districtid', 'weekid', 'dose1', 'dose2'])
for i in week_data1['districtid']:
    list1 = list(week_data1.loc[dn])[1:]
    list2 = list(week_data2.loc[dn])[1:]
    dn = dn + 1
    
    for j in range(len(list1)):
        week_data.loc[k] = [i, str(int(j+1)), list1[j], list2[j]]
        k = k + 1

        
        
st_id = list()
for i in range(len(week_data['districtid'])):
    sc = (str(week_data['districtid'].loc[i]).split('_')[0])
    st_id.append(sc)
week_sort = pd.DataFrame(columns = ['stateid', 'weekid', 'dose1', 'dose2'])
week_sort['stateid'] = st_id
week_sort['weekid'] = week_data['weekid']
week_sort['dose1'] = week_data['dose1']
week_sort['dose2'] = week_data['dose2']


week_stt = pd.DataFrame(columns = ['stateid', 'weekid', 'dose1', 'dose2'])
st_id = list(set(data['State_Code']))
st_id.sort()
i = 0
for s in st_id:
    temp1 = week_sort.loc[week_sort['stateid'] == s]
    for t in range(1,32):
        temp2 = temp1.loc[temp1['weekid'] == str(t)]
        a = temp2['dose1'].sum()
        b = temp2['dose2'].sum()
        week_stt.loc[i] = [s,t,a,b]
        i = i + 1

week_data.to_csv("output-files/district-vaccinated-count-week.csv", index = False)
week_stt.to_csv("output-files/state-vaccinated-count-week.csv", index = False)
        
        
        
        
month_data1 = pd.DataFrame(columns = ['districtid'])
month_data1['districtid'] = new_data1.index
month_data1['0'] = list(new_data1['16/01/2021'])

month_data2 = pd.DataFrame(columns = ['districtid'])
month_data2['districtid'] = new_data2.index
month_data2['0'] = list(new_data2['16/01/2021'])        


cm = 1
cr = 0
while cm < 8:
    if cm in [1,3,5,7,8,10,12]:
        month_data1[str(cm)] = np.array(new_data1.iloc[:,cr+31]) - np.array(new_data1.iloc[:,cr])
        month_data2[str(cm)] = np.array(new_data2.iloc[:,cr+31]) - np.array(new_data2.iloc[:,cr])
        cr = cr + 31
    elif cm in [4,6,9,11]:
        month_data1[str(cm)] = np.array(new_data1.iloc[:,cr+30]) - np.array(new_data1.iloc[:,cr])
        month_data2[str(cm)] = np.array(new_data2.iloc[:,cr+30]) - np.array(new_data2.iloc[:,cr])
        cr = cr + 30
    else:
        month_data1[str(cm)] = np.array(new_data1.iloc[:,cr+28]) - np.array(new_data1.iloc[:,cr])
        month_data2[str(cm)] = np.array(new_data2.iloc[:,cr+28]) - np.array(new_data2.iloc[:,cr])
        cr = cr + 28
    cm = cm + 1
        
    
    
k = 0
dn = 0
month_data = pd.DataFrame(columns = ['districtid', 'monthid', 'dose1', 'dose2'])
for i in month_data1['districtid']:
    list1 = list(month_data1.loc[dn])[1:]
    list2 = list(month_data2.loc[dn])[1:]
    dn = dn + 1
    
    for j in range(len(list1)):
        month_data.loc[k] = [i, str(int(j+1)), list1[j], list2[j]]
        k = k + 1
        
st_id = list()
for i in range(len(month_data['districtid'])):
    sc = (str(month_data['districtid'].loc[i]).split('_')[0])
    st_id.append(sc)
month_sort = pd.DataFrame(columns = ['stateid', 'monthid', 'dose1', 'dose2'])
month_sort['stateid'] = st_id
month_sort['monthid'] = month_data['monthid']
month_sort['dose1'] = month_data['dose1']
month_sort['dose2'] = month_data['dose2']


month_stt = pd.DataFrame(columns = ['stateid', 'monthid', 'dose1', 'dose2'])
st_id = list(set(data['State_Code']))
st_id.sort()
i = 0
for s in st_id:
    temp1 = month_sort.loc[month_sort['stateid'] == s]
    for t in range(1,9):
        temp2 = temp1.loc[temp1['monthid'] == str(t)]
        a = temp2['dose1'].sum()
        b = temp2['dose2'].sum()
        month_stt.loc[i] = [s,t,a,b]
        i = i + 1

month_data.to_csv("output-files/district-vaccinated-count-month.csv", index = False)
month_stt.to_csv("output-files/state-vaccinated-count-month.csv", index = False)
        
        
        
over_data = pd.DataFrame(columns = ['districtid', 'overallid', 'dose1', 'dose2'])
over_data['districtid'] = new_data1.index
over_data['overallid'] = 'overall'
over_data['dose1'] = list(new_data1['14/08/2021'])
over_data['dose2'] = list(new_data2['14/08/2021'])



d_list = list(over_data['districtid'])
st_id = list()
for i in d_list:
    st_id.append(i.split('_')[0])
f_data = list(over_data['dose1'])
s_data = list(over_data['dose2'])
us_id = list()
fd_data = list()
sd_data = list()
un = None
fsum, ssum = 0, 0

for i in range(len(st_id)):
    if un != st_id[i]:
        if un != None:
            us_id.append(un)
            fd_data.append(fsum)
            sd_data.append(ssum)
            fsum, ssum = 0, 0
        un = st_id[i]
    fsum = fsum + f_data[i]
    ssum = ssum + s_data[i]
us_id.append(un)
fd_data.append(fsum)
sd_data.append(ssum)

over_stt = pd.DataFrame(columns = ['stateid', 'overallid', 'dose1', 'dose2'])
over_stt['stateid'] = us_id
over_stt['overallid'] = 'overall'
over_stt['dose1'] = fd_data
over_stt['dose2'] = sd_data

over_data.to_csv("output-files/district-vaccinated-count-overall.csv", index = False)
over_stt.to_csv("output-files/state-vaccinated-count-overall.csv", index = False)

