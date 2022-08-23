#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.options.mode.chained_assignment = None
data = pd.read_csv('cowin_vaccine_data_districtwise.csv', header = [0], skiprows = [1])
com = pd.read_csv('cowin_vaccine_data_districtwise.csv', header = [0], nrows = 1)
l = com.loc[0]
n = list(data)
dis_list = pd.DataFrame(columns = ['districtid', 'first dose', 'second dose'])
dis_list['districtid'] = data['District_Key']



k = 0
for i in range(len(l)):
    if (l[i] == 'First Dose Administered') and (n[i].split('.')[0] == '14/08/2021'):
        dis_list['first dose'] = data[n[i]]
    elif (l[i] == 'Second Dose Administered') and (n[i].split('.')[0] == '14/08/2021'):
        dis_list['second dose'] = data[n[i]]

dis_list = dis_list.groupby(['districtid']).sum()          
fs_dis = pd.DataFrame(columns = ['districtid', 'first dose', 'second dose'])        
fs_dis['districtid'] = dis_list.index        
fs_dis['first dose'] = list(dis_list['first dose'])
fs_dis['second dose'] = list(dis_list['second dose'])

st_id = list()
for i in range(len(fs_dis['districtid'])):
    sc = (str(fs_dis['districtid'].loc[i]).split('_')[0])
    st_id.append(sc)
f_data = list(fs_dis['first dose'])
s_data = list(fs_dis['second dose'])
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

fs_stt = pd.DataFrame(columns = ['stateid', 'first dose', 'second dose'])
fs_stt['stateid'] = us_id
fs_stt['first dose'] = fd_data
fs_stt['second dose'] = sd_data


fs_over = pd.DataFrame(columns = ['countryid', 'first dose', 'second dose'])

fs_over['countryid'] = ['IND']
fs_over['first dose'] = fs_stt['first dose'].sum()
fs_over['second dose'] = fs_stt['second dose'].sum()





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

p_over = p_data.loc[p_data['Level'] == 'India']


p_stt = p_data.loc[p_data['Level'] == 'STATE']
p = list((p_stt['TOT_P'].loc[p_stt['Name'] == 'DAMAN AND DIU']))[0] + list((p_stt['TOT_P'].loc[p_stt['Name'] == 'DADRA AND NAGAR HAVELI']))[0]
p_stt.loc[len(p_stt.index)] = ['STATE', 'DADRA AND NAGAR HAVELI AND DAMAN AND DIU', 'TOTAL', p]
p_stt.sort_values(by = 'Name')


temp = p_data.loc[p_data['Level'] != 'India']
temp.index = [i for i in range(0,len(temp['Name']))]

temp2 = pd.DataFrame(columns = ['state', 'district', 'TOT_P'])

state, district, TOT_P = list(), list(), list()
for i in range(len(temp)):
    if temp.Level.loc[i] == 'STATE':
        s = temp['Name'].loc[i]
        continue
    state.append(s)
    district.append(temp['Name'].loc[i])
    TOT_P.append(temp['TOT_P'].loc[i])

temp2['state'] = state
temp2['district'] = district
temp2['TOT_P'] = TOT_P




p_dis =  temp2.sort_values(by = 'state')
p_dis.index = [i for i in range(0,len(p_dis['district']))]




did = list(data['District_Key'])
ku = list(data['District'])
dname = list()

for i in range(len(ku)):
    dname.append(ku[i].lower())
        
z = 1
id_list = list()
fratio_list = list()
sratio_list = list()
for i in range(0,len(p_dis['district'])):
    nam = p_dis['district'].loc[i].lower()
    
    if nam in dname:
        for j in range(0, len(dname)-1):
            if nam == dname[j]:
                nam = did[j]
                did.remove(did[j])
                dname.remove(dname[j])
                break
                
                
        id_list.append(nam)
        a = list(fs_dis['first dose'].loc[fs_dis['districtid']  == nam])[0]
        b = float(p_dis['TOT_P'].loc[i])
        fratio_list.append(a / b)
        a = list(fs_dis['second dose'].loc[fs_dis['districtid']  == nam])[0]
        b = float(p_dis['TOT_P'].loc[i])
        sratio_list.append(a / b)

r_dis = pd.DataFrame(columns = ['districtid', 'vaccinateddose1ratio', 'vaccinateddose2ratio'])
r_dis['districtid'] = id_list
r_dis['vaccinateddose1ratio'] = fratio_list
r_dis['vaccinateddose2ratio'] = sratio_list
r_dis = r_dis.sort_values(by = 'vaccinateddose1ratio')
r_dis.index = [i for i in range(0,len(r_dis['districtid']))]                     
                     
                     
                     
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
fratio_list = list()
sratio_list = list()
for i in range(0,len(p_stt['Name'])):
    nam = p_stt['Name'].loc[i].lower()
    
    if nam in dic_sid.keys():
        id_list.append(dic_sid[nam])
        fratio_list.append(list(fs_stt['first dose'].loc[fs_stt['stateid']  == dic_sid[nam]])[0] / (p_stt['TOT_P'].loc[i]))
        sratio_list.append(list(fs_stt['second dose'].loc[fs_stt['stateid']  == dic_sid[nam]])[0] / (p_stt['TOT_P'].loc[i]))
      
    
r_stt = pd.DataFrame(columns = ['stateid', 'vaccinateddose1ratio', 'vaccinateddose2ratio'])
r_stt['stateid'] = id_list
r_stt['vaccinateddose1ratio'] = fratio_list
r_stt['vaccinateddose2ratio'] = sratio_list
r_stt = r_stt.sort_values(by = 'vaccinateddose1ratio')
r_stt.index = [i for i in range(0,len(r_stt['stateid']))]      

    
r_over = pd.DataFrame(columns = ['countryid', 'vaccinateddose1ratio', 'vaccinateddose2ratio'])
r_over['countryid'] = fs_over['countryid']
r_over['vaccinateddose1ratio'] = fs_over['first dose'] / p_over['TOT_P']
r_over['vaccinateddose2ratio'] = fs_over['second dose'] / p_over['TOT_P']
r_over = r_over.sort_values(by = 'vaccinateddose1ratio')
r_over.index = [i for i in range(0,len(r_over['countryid']))]


r_dis.to_csv("output-files/district-vaccinated-dose-ratio.csv", index = False)
r_stt.to_csv("output-files/state-vaccinated-dose-ratio.csv", index = False)
r_over.to_csv("output-files/overall-vaccinated-dose-ratio.csv", index = False)

