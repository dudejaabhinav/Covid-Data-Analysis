#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

data = pd.read_csv('cowin_vaccine_data_districtwise.csv', header = [0], skiprows = [1])
com = pd.read_csv('cowin_vaccine_data_districtwise.csv', header = [0], nrows = 1)
l = com.loc[0]
n = list(data)
dis_list = pd.DataFrame(columns = ['districtid','cvsd','cvxn'])
dis_list['districtid'] = data['District_Key']



k = 0
for i in range(len(l)):
    if (l[i] == 'CoviShield (Doses Administered)') and (n[i].split('.')[0] == '14/08/2021'):
        dis_list['cvsd'] = data[n[i]]
    elif (l[i] == 'Covaxin (Doses Administered)') and (n[i].split('.')[0] == '14/08/2021'):
        dis_list['cvxn'] = data[n[i]]

dis_list = dis_list.groupby(['districtid']).sum()        
dx_dis = pd.DataFrame(columns = ['districtid', 'vaccineratio', 'cvsd', 'cvxn'])
dx_dis['districtid'] = dis_list.index
dx_dis['cvsd'] = list(dis_list['cvsd'])
dx_dis['cvxn'] = list(dis_list['cvxn'])
dx_dis['vaccineratio'] = dx_dis['cvsd'] / dx_dis['cvxn']




st_id = list()
for i in range(len(dx_dis['districtid'])):
    sc = (str(dx_dis['districtid'].loc[i]).split('_')[0])
    st_id.append(sc)
cd_data = list(dx_dis['cvsd'])
cx_data = list(dx_dis['cvxn'])
us_id = list()
csd_data = list()
cxn_data = list()
un = None
cdsum, cxsum = 0, 0

for i in range(len(st_id)):
    if un != st_id[i]:
        if un != None:
            us_id.append(un)
            csd_data.append(cdsum)
            cxn_data.append(cxsum)
            cdsum, cxsum = 0, 0
        un = st_id[i]
    cdsum = cdsum + cd_data[i]
    cxsum = cxsum + cx_data[i]
us_id.append(un)
csd_data.append(cdsum)
cxn_data.append(cxsum)

dx_stt = pd.DataFrame(columns = ['stateid', 'vaccineratio', 'covishield', 'covaxin'])
dx_stt['stateid'] = us_id
dx_stt['covishield'] = csd_data
dx_stt['covaxin'] = cxn_data
dx_stt['vaccineratio'] = dx_stt['covishield'] / dx_stt['covaxin']




dx_over = pd.DataFrame(columns = ['countryid', 'vaccineratio', 'covishield', 'covaxin'])
dx_over['countryid'] = ['IND']
dx_over['covishield'] = dx_stt['covishield'].sum()
dx_over['covaxin'] = dx_stt['covaxin'].sum()
dx_over['vaccineratio'] = dx_over['covishield'] / dx_over['covaxin']



dx_over.drop(dx_over.iloc[:, 2:], inplace = True, axis = 1)
dx_stt.drop(dx_stt.iloc[:, 2:], inplace = True, axis = 1)
dx_dis.drop(dx_dis.iloc[:, 2:], inplace = True, axis = 1)

dx_dis = dx_dis.sort_values(by = 'vaccineratio')
dx_stt = dx_stt.sort_values(by = 'vaccineratio')
dx_over = dx_over.sort_values(by = 'vaccineratio')

dx_dis.replace([np.inf], "NaN", inplace=True)
dx_stt.replace([np.inf], "NaN", inplace=True)
dx_over.replace([np.inf], "NaN", inplace=True)

dx_dis.to_csv("output-files/district-vaccine-type-ratio.csv", index = False)
dx_stt.to_csv("output-files/state-vaccine-type-ratio.csv", index = False)
dx_over.to_csv("output-files/overall-vaccine-type-ratio.csv", index = False)

