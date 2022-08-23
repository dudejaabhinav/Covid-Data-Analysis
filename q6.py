#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
pd.options.mode.chained_assignment = None
data = pd.read_csv('cowin_vaccine_data_districtwise.csv', header = [0], skiprows = [1])
com = pd.read_csv('cowin_vaccine_data_districtwise.csv', header = [0], nrows = 1)
l = com.loc[0]
n = list(data)
dis_list = pd.DataFrame(columns = ['districtid','female','male'])
dis_list['districtid'] = data['District_Key']


k = 0
for i in range(len(l)):
    if (l[i] == 'Female(Individuals Vaccinated)') and (n[i].split('.')[0] == '14/08/2021'):
        dis_list['female'] = data[n[i]]
    elif (l[i] == 'Male(Individuals Vaccinated)') and (n[i].split('.')[0] == '14/08/2021'):
        dis_list['male'] = data[n[i]]
        
dis_list = dis_list.groupby(['districtid']).sum()        
fm_dis = pd.DataFrame(columns = ['districtid','ratio','female','male'])
fm_dis['districtid'] = dis_list.index
fm_dis['female'] = list(dis_list['female'])
fm_dis['male'] = list(dis_list['male'])
fm_dis['ratio'] = fm_dis['female'] / fm_dis['male']




st_id = list()
for i in range(len(fm_dis['districtid'])):
    sc = (str(fm_dis['districtid'].loc[i]).split('_')[0])
    st_id.append(sc)
f_data = list(fm_dis['female'])
m_data = list(fm_dis['male'])
us_id = list()
fs_data = list()
ms_data = list()
un = None
fsum, msum = 0, 0

for i in range(len(st_id)):
    if un != st_id[i]:
        if un != None:
            us_id.append(un)
            fs_data.append(fsum)
            ms_data.append(msum)
            fsum, msum = 0, 0
        un = st_id[i]
    fsum = fsum + f_data[i]
    msum = msum + m_data[i]
us_id.append(un)
fs_data.append(fsum)
ms_data.append(msum)

fm_stt = pd.DataFrame(columns = ['stateid', 'ratio', 'female', 'male'])
fm_stt['stateid'] = us_id
fm_stt['female'] = fs_data
fm_stt['male'] = ms_data
fm_stt['ratio'] = fm_stt['female'] / fm_stt['male']


fm_over = pd.DataFrame(columns = ['countryid', 'ratio', 'female', 'male'])
fm_over['countryid'] = ['IND']
fm_over['female'] = fm_stt['female'].sum()
fm_over['male'] = fm_stt['male'].sum()
fm_over['ratio'] = fm_over['female'] / fm_over['male']

fm_over.drop(fm_over.iloc[:, 2:], inplace = True, axis = 1)
fm_stt.drop(fm_stt.iloc[:, 2:], inplace = True, axis = 1)
fm_dis.drop(fm_dis.iloc[:, 2:], inplace = True, axis = 1)








cols = ['Level', 'Name', 'TRU', 'TOT_M', 'TOT_F']
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
f = (p_stt['TOT_F'].loc[p_stt['Name'] == 'DAMAN AND DIU']) + (p_stt['TOT_F'].loc[p_stt['Name'] == 'DADRA AND NAGAR HAVELI'])
m = p_stt['TOT_M'].loc[p_stt['Name'] == 'DAMAN AND DIU'] + p_stt['TOT_M'].loc[p_stt['Name'] == 'DADRA AND NAGAR HAVELI']
p_stt.loc[len(p_stt.index)] = ['STATE', 'DADRA AND NAGAR HAVELI AND DAMAN AND DIU', 'TOTAL', m, f]
p_stt.sort_values(by = 'Name')

temp = p_data.loc[p_data['Level'] != 'India']
temp.index = [i for i in range(0,len(temp['Name']))]

temp2 = pd.DataFrame(columns = ['state', 'district', 'ratio'])

state, district, ratio = list(), list(), list()
for i in range(len(temp)):
    if temp.Level.loc[i] == 'STATE':
        s = temp['Name'].loc[i]
        continue
    state.append(s)
    district.append(temp['Name'].loc[i])
    ratio.append(temp['TOT_M'].loc[i] / temp['TOT_F'].loc[i])

temp2['state'] = state
temp2['district'] = district
temp2['ratio'] = ratio




p_dis =  temp2.sort_values(by = 'state')
p_dis.index = [i for i in range(0,len(p_dis['district']))]




did = list(data['District_Key'])
ku = list(data['District'])
dname = list()

for i in range(len(ku)):
    dname.append(ku[i].lower())
        

id_list = list()
pratio_list = list()
vratio_list = list()
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
        pratio_list.append(float(p_dis['ratio'].loc[i]))
        vratio_list.append(list(fm_dis['ratio'].loc[fm_dis['districtid']  == nam])[0])
        
r_dis = pd.DataFrame(columns = ['districtid', 'vaccinationratio', 'populationratio', 'ratioofratios'])    
r_dis['districtid'] = id_list
r_dis['vaccinationratio'] = vratio_list
r_dis['populationratio'] = pratio_list
r_dis['ratioofratios'] = r_dis['vaccinationratio'] / r_dis['populationratio']
r_dis = r_dis.sort_values(by = 'ratioofratios')
r_dis.index = [i for i in range(0,len(r_dis['ratioofratios']))]





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
ratio_list = list()
for i in range(0,len(p_stt['Name'])):
    nam = p_stt['Name'].loc[i].lower()
    
    if nam in dic_sid.keys():
        id_list.append(dic_sid[nam])
    
       
for i in id_list:
    ratio_list.append(float(fm_stt['ratio'].loc[fm_stt['stateid']  == i]))
    
    
r_stt = pd.DataFrame(columns = ['stateid', 'vaccinationratio', 'populationratio', 'ratioofratios'])
r_stt['stateid'] = id_list
r_stt['vaccinationratio'] = ratio_list
r_stt['populationratio'] = p_stt['TOT_F'] / p_stt['TOT_M']
r_stt['ratioofratios'] = r_stt['vaccinationratio'] / r_stt['populationratio']
r_stt = r_stt.sort_values(by = 'ratioofratios')
r_stt.index = [i for i in range(0,len(r_stt['ratioofratios']))]




r_over = pd.DataFrame(columns = ['countryid', 'vaccinationratio', 'populationratio', 'ratioofratios'])
r_over['countryid'] = fm_over['countryid']
r_over['vaccinationratio'] = fm_over['ratio']
r_over['populationratio'] = p_over['TOT_F'] / p_over['TOT_M']
r_over['ratioofratios'] = r_over['vaccinationratio'] / r_over['populationratio']
r_over = r_over.sort_values(by = 'ratioofratios')
r_over.index = [i for i in range(0,len(r_over['ratioofratios']))]

r_dis.to_csv("output-files/district-vaccination-population-ratio.csv", index = False)
r_stt.to_csv("output-files/state-vaccination-population-ratio.csv", index = False)
r_over.to_csv("output-files/overall-vaccination-population-ratio.csv", index = False)

