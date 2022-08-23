#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import datetime
import numpy as np
data = pd.read_csv("districts.csv")
dis_id = pd.read_csv("cowin_vaccine_data_districtwise.csv", header = [0], skiprows = [1])

peak_dis = pd.DataFrame(columns = ['districtid', 'wave1-weekid', 'wave2-weekid', 'wave1-monthid', 'wave2-monthid'])

did_list, w1_list, w2_list, m1_list, m2_list = list(), list(), list(), list(), list()


sta_lis = list(set(data['State']))
sta_lis.sort()
i = 0
for s in sta_lis:
    st = data.loc[data['State'] == s]
    st_id = dis_id.loc[dis_id['State'] == s]
    dname = list(set(st['District']))
    dname.sort()
    d_list = list(st_id['District'])
    
    for d in dname:
        w = 1
        l_case1 = 0
        l_date1 = datetime.datetime(2020,3,14)
        l_date2 = datetime.datetime(2020,3,19)
        m_w,pm_w = 0,0
        c = 0
        m_list, id_list = list(), list()
        
        if d == 'Unknown':
            if len(dname) == 1:
                dt = st.loc[st['District'] == d]
                did = list(st_id['State_Code'])[0]
                for j in range(0, 517, 7):
                    c_date1 = l_date1 + datetime.timedelta(days=(7))
                    temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date1).split(' ')[0])])
                    temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(c_date1).split(' ')[0])])
                    temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(c_date1).split(' ')[0])])
                    if temp_c == []:
                        c_case1 = 0
                    else:
                        c_case1 = temp_c[0] - temp_r[0] - temp_d[0]
                    if c_case1 < l_case1:
                        c_case1 = l_case1
                    w_case1 = c_case1 - l_case1
                    l_case1 = c_case1
                    l_date1 = c_date1
                    
                    if l_date2 == datetime.datetime(2020,3,19):
                        temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(l_date2).split(' ')[0])])
                        temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(l_date2).split(' ')[0])])
                        temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(l_date2).split(' ')[0])])
                        if temp_c == []:
                            l_case2 = 0
                        else:
                            l_case2 = temp_c[0] - temp_r[0] - temp_d[0]
                    c_date2 = l_date2 + datetime.timedelta(days=(7))
                    temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date2).split(' ')[0])])
                    temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(c_date2).split(' ')[0])])
                    temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(c_date2).split(' ')[0])])
                    if temp_c == []:
                        c_case2 = 0
                    else:
                        c_case2 = temp_c[0] - temp_r[0] - temp_d[0]
                        
                    if c_case2 < l_case2:
                        c_case2 = l_case2
                    w_case2 = c_case2 - l_case2
                    l_case2 = c_case2
                    l_date2 = c_date2
                    
                    if w_case1 > m_w:
                        m_w = w_case1
                        wid = w
                    if w_case2 > m_w:
                        m_w = w_case2
                        wid = w + 1
                    if m_w == pm_w and m_w != 0:
                        c = c + 1
                    if m_w != pm_w:
                        c = 0
                    pm_w = m_w
                    if c == 8:
                        m_list.append(m_w)
                        id_list.append(wid)
                        m_w = 0
                        pm_w = 0
                        c = 0

                    
                    i = i + 2
                    w = w + 2
            else:
                continue
        elif d in d_list:
            
            dt = st.loc[st['District'] == d]
            did = list(st_id['District_Key'].loc[st_id['District'] == d])[0]
            for j in range(0, 517, 7):
                    c_date1 = l_date1 + datetime.timedelta(days=(7))
                    temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date1).split(' ')[0])])
                    temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(c_date1).split(' ')[0])])
                    temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(c_date1).split(' ')[0])])
                    if temp_c == []:
                        c_case1 = 0
                    else:
                        c_case1 = temp_c[0] - temp_r[0] - temp_d[0]
                    if c_case1 < l_case1:
                        c_case1 = l_case1
                    w_case1 = c_case1 - l_case1
                    l_case1 = c_case1
                    l_date1 = c_date1
                    
                    if l_date2 == datetime.datetime(2020,3,19):
                        temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(l_date2).split(' ')[0])])
                        temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(l_date2).split(' ')[0])])
                        temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(l_date2).split(' ')[0])])
                        if temp_c == []:
                            l_case2 = 0
                        else:
                            l_case2 = temp_c[0] - temp_r[0] - temp_d[0]
                    c_date2 = l_date2 + datetime.timedelta(days=(7))
                    temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date2).split(' ')[0])])
                    temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(c_date2).split(' ')[0])])
                    temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(c_date2).split(' ')[0])])
                    if temp_c == []:
                        c_case2 = 0
                    else:
                        c_case2 = temp_c[0] - temp_r[0] - temp_d[0]
                    if c_case2 < l_case2:
                        c_case2 = l_case2
                    w_case2 = c_case2 - l_case2
                    l_case2 = c_case2
                    l_date2 = c_date2
                    
                    
                    if w_case1 > m_w:
                        m_w = w_case1
                        wid = w
                    if w_case2 > m_w:
                        m_w = w_case2
                        wid = w + 1
                    if m_w == pm_w and m_w != 0:
                        c = c + 1
                    if m_w != pm_w:
                        c = 0
                    pm_w = m_w
                    if c == 8:
                        m_list.append(m_w)
                        id_list.append(wid)
                        m_w = 0
                        pm_w = 0
                        c = 0
                    
                   
                    i = i + 2
                    w = w + 2
        elif d == s:
            dt = st.loc[st['District'] == d]
            did = list(st_id['State_Code'])[0]
            for j in range(0, 517, 7):
                    c_date1 = l_date1 + datetime.timedelta(days=(7))
                    temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date1).split(' ')[0])])
                    temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(c_date1).split(' ')[0])])
                    temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(c_date1).split(' ')[0])])
                    if temp_c == []:
                        c_case1 = 0
                    else:
                        c_case1 = temp_c[0] - temp_r[0] - temp_d[0]
                    if c_case1 < l_case1:
                        c_case1 = l_case1
                    w_case1 = c_case1 - l_case1
                    l_case1 = c_case1
                    l_date1 = c_date1
                    
                    if l_date2 == datetime.datetime(2020,3,19):
                        temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(l_date2).split(' ')[0])])
                        temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(l_date2).split(' ')[0])])
                        temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(l_date2).split(' ')[0])])
                        if temp_c == []:
                            l_case2 = 0
                        else:
                            l_case2 = temp_c[0] - temp_r[0] - temp_d[0]
                    c_date2 = l_date2 + datetime.timedelta(days=(7))
                    temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date2).split(' ')[0])])
                    temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(c_date2).split(' ')[0])])
                    temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(c_date2).split(' ')[0])])
                    if temp_c == []:
                        c_case2 = 0
                    else:
                        c_case2 = temp_c[0] - temp_r[0] - temp_d[0]
                    if c_case2 < l_case2:
                        c_case2 = l_case2
                    w_case2 = c_case2 - l_case2
                    l_case2 = c_case2
                    l_date2 = c_date2
                    
                    
                    if w_case1 > m_w:
                        m_w = w_case1
                        wid = w
                    if w_case2 > m_w:
                        m_w = w_case2
                        wid = w + 1
                    if m_w == pm_w and m_w != 0:
                        c = c + 1
                    if m_w != pm_w:
                        c = 0
                    pm_w = m_w
                    if c == 8:
                        m_list.append(m_w)
                        id_list.append(wid)
                        m_w = 0
                        pm_w = 0
                        c = 0
                    
                    i = i + 2
                    w = w + 2
        
        did_list.append(did)
        if len(id_list) < 2:
            if len(id_list) < 1:
                w1_list.append(int(-1))
                w2_list.append(int(-1))
            else:
                if id_list[0] < 100:
                    w1_list.append(id_list[0])
                    w2_list.append(int(-1))
                else:
                    w2_list.append(id_list[0])
                    w1_list.append(int(-1))
        else:
            idx = np.argsort(m_list)
            wave1 = id_list[idx[-1]]
            wave2 = id_list[idx[-2]]
            if wave2 < wave1:
                wave1, wave2 = wave2, wave1
            if wave1 > 100:
                wave2 = wave1
                wave1 = -1
            if wave2 < 100:
                wave1 = wave2
                wave2 = -1
            w1_list.append(wave1)
            w2_list.append(wave2)

              
                

i = 0
for s in sta_lis:
    st = data.loc[data['State'] == s]
    st_id = dis_id.loc[dis_id['State'] == s]
    dname = list(set(st['District']))
    dname.sort()
    d_list = list(st_id['District'])
    for d in dname:
        m = 1
        l_case = 0
        l_date = datetime.datetime(2020,3,14)
        m_m,pm_m = 0,0
        c = 0
        m_list, id_list = list(), list()
        if d == 'Unknown':
            if len(dname) == 1:
                dt = st.loc[st['District'] == d]
                did = list(st_id['State_Code'])[0]
                for j in range(0,17):
                    mon = l_date.strftime("%m")
                    if mon == '01' or mon == '03' or mon == '05' or mon == '07' or mon == '08' or mon == '10' or mon == '12':
                        c_date = l_date + datetime.timedelta(days=(31))
                    elif mon == '04' or mon == '06' or mon == '09' or mon == '11':
                        c_date = l_date + datetime.timedelta(days=(30))
                    else:
                        c_date = l_date + datetime.timedelta(days=(28))
                    temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                    temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                    temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                    if temp_c == []:
                        c_case = 0
                    else:
                        c_case = temp_c[0] - temp_r[0] - temp_d[0]
                    if c_case < l_case:
                        c_case = l_case
                    m_case = c_case - l_case
                    l_case = c_case
                    l_date = c_date
                    if m_case > m_m:
                        m_m = m_case
                        mid = m
                    if m_m == pm_m and m_m != 0:
                        c = c + 1
                    if m_m != pm_m:
                        c = 0
                        pm_m = m_m
                    if c == 2:
                        m_list.append(m_m)
                        id_list.append(mid)
                        m_m = 0
                        pm_m = 0
                        c = 0
                    i = i + 1
                    m = m + 1
            else:
                continue
        elif d in d_list:
            
            dt = st.loc[st['District'] == d]
            did = list(st_id['District_Key'].loc[st_id['District'] == d])[0]
            for j in range(0,17):
                mon = l_date.strftime("%m")
                if mon == '01' or mon == '03' or mon == '05' or mon == '07' or mon == '08' or mon == '10' or mon == '12':
                    c_date = l_date + datetime.timedelta(days=(31))
                elif mon == '04' or mon == '06' or mon == '09' or mon == '11':
                    c_date = l_date + datetime.timedelta(days=(30))
                else:
                    c_date = l_date + datetime.timedelta(days=(28))
                temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                if temp_c == []:
                    c_case = 0
                else:
                    c_case = temp_c[0] - temp_r[0] - temp_d[0]
                if c_case < l_case:
                    c_case = l_case
                m_case = c_case - l_case
                l_case = c_case
                l_date = c_date
                if m_case > m_m:
                    m_m = m_case
                    mid = m
                if m_m == pm_m and m_m != 0:
                    c = c + 1
                if m_m != pm_m:
                    c = 0
                    pm_m = m_m
                if c == 2:
                    m_list.append(m_m)
                    id_list.append(mid)
                    m_m = 0
                    pm_m = 0
                    c = 0
                i = i + 1
                m = m + 1
        elif d == s:
            dt = st.loc[st['District'] == d]
            did = list(st_id['State_Code'])[0]
            for j in range(0,17):
                mon = l_date.strftime("%m")
                if mon == '01' or mon == '03' or mon == '05' or mon == '07' or mon == '08' or mon == '10' or mon == '12':
                    c_date = l_date + datetime.timedelta(days=(31))
                elif mon == '04' or mon == '06' or mon == '09' or mon == '11':
                    c_date = l_date + datetime.timedelta(days=(30))
                else:
                    c_date = l_date + datetime.timedelta(days=(28))
                temp_c = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                temp_r = list(dt['Recovered'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                temp_d = list(dt['Deceased'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                if temp_c == []:
                    c_case = 0
                else:
                    c_case = temp_c[0] - temp_r[0] - temp_d[0]
                if c_case < l_case:
                    c_case = l_case
                m_case = c_case - l_case
                l_case = c_case
                l_date = c_date
                if m_case > m_m:
                    m_m = m_case
                    mid = m
                if m_m == pm_m and m_m != 0:
                    c = c + 1
                if m_m != pm_m:
                    c = 0
                    pm_m = m_m
                if c == 2:
                    m_list.append(m_m)
                    id_list.append(mid)
                    m_m = 0
                    pm_m = 0
                    c = 0
                i = i + 1
                m = m + 1
                
                
        
        if len(id_list) < 2:
            if len(id_list) < 1:
                m1_list.append(int(-1))
                m2_list.append(int(-1))
            else:
                if id_list[0] < 10:
                    m1_list.append(id_list[0])
                    m2_list.append(int(-1))
                else:
                    m2_list.append(id_list[0])
                    m1_list.append(int(-1))
        else:
            idx = np.argsort(m_list)
            wave1 = id_list[idx[-1]]
            wave2 = id_list[idx[-2]]
            if wave2 < wave1:
                wave1, wave2 = wave2, wave1
            if wave1 > 10:
                wave2 = wave1
                wave1 = -1
            if wave2 < 10:
                wave1 = wave2
                wave2 = -1
            m1_list.append(wave1)
            m2_list.append(wave2)
            
for i in range(0,len(did_list)):
    peak_dis.loc[i] = [did_list[i], w1_list[i], w2_list[i], m1_list[i], m2_list[i]]

    
    
    
peak_sta = pd.DataFrame(columns = ['stateid', 'wave1-weekid', 'wave2-weekid', 'wave1-monthid', 'wave2-monthid'])

sid_list, w1_list, w2_list, m1_list, m2_list = list(), list(), list(), list(), list()

sta_lis = list(set(data['State']))
sta_lis.sort()
i = 0
for s in sta_lis:
    st = data.loc[data['State'] == s]
    st_id = dis_id.loc[dis_id['State'] == s]
    w = 1
    l_case1 = 0
    l_date1 = datetime.datetime(2020,3,14)
    l_date2 = datetime.datetime(2020,3,19)
    temp = st.loc[st['Date'] == (str(l_date2).split(' ')[0])]
    if temp.empty:
        temp_c = 0
        temp_r = 0
        temp_d = 0
    else:
        temp_c = temp['Confirmed'].sum()
        temp_r = temp['Recovered'].sum()
        temp_d = temp['Deceased'].sum()
    l_case2 = temp_c - temp_r - temp_d
    sid = list(st_id['State_Code'])[0]
    
    m_w,pm_w = 0,0
    c = 0
    m_list, id_list = list(), list()
    
    for j in range(0, 517, 7):
        c_date1 = l_date1 + datetime.timedelta(days=(7))
        temp = st.loc[st['Date'] == (str(c_date1).split(' ')[0])]
        if temp.empty:
            temp_c = 0
            temp_r = 0
            temp_d = 0
        else:
            temp_c = temp['Confirmed'].sum()
            temp_r = temp['Recovered'].sum()
            temp_d = temp['Deceased'].sum()
        c_case1 = temp_c - temp_r - temp_d
        if c_case1 < l_case1:
            c_case1 = l_case1
        w_case1 = c_case1 - l_case1
        l_case1 = c_case1
        l_date1 = c_date1
            
        c_date2 = l_date2 + datetime.timedelta(days=(7))
        temp = st.loc[st['Date'] == (str(c_date2).split(' ')[0])]
        if temp.empty:
            temp_c = 0
            temp_r = 0
            temp_d = 0
        else:
            temp_c = temp['Confirmed'].sum()
            temp_r = temp['Recovered'].sum()
            temp_d = temp['Deceased'].sum()
        c_case2 = temp_c - temp_r - temp_d
        if c_case2 < l_case2:
            c_case2 = l_case2
        w_case2 = c_case2 - l_case2
        l_case2 = c_case2
        l_date2 = c_date2
        if w_case1 > m_w:
            m_w = w_case1
            wid = w
        if w_case2 > m_w:
            m_w = w_case2
            wid = w + 1
        if m_w == pm_w and m_w != 0:
            c = c + 1
        if m_w != pm_w:
            c = 0
        pm_w = m_w
        if c == 8:
            m_list.append(m_w)
            id_list.append(wid)
            m_w = 0
            pm_w = 0
            c = 0
    
        i = i + 2
        w = w + 2  
        
    sid_list.append(sid)
    if len(id_list) < 2:
        if len(id_list) < 1:
            w1_list.append(int(-1))
        else:
            if id_list[0] < 100:
                w1_list.append(id_list[0])
                w2_list.append(int(-1))
            else:
                w2_list.append(id_list[0])
                w1_list.append(int(-1))
    else:
        idx = np.argsort(m_list)
        wave1 = id_list[idx[-1]]
        wave2 = id_list[idx[-2]]
        if wave2 < wave1:
            wave1, wave2 = wave2, wave1
        if wave1 > 100:
            wave2 = wave1
            wave1 = -1
        if wave2 < 100:
            wave1 = wave2
            wave2 = -1
        w1_list.append(wave1)
        w2_list.append(wave2)

                
                
               



i = 0

for s in sta_lis:
    st = data.loc[data['State'] == s]
    st_id = dis_id.loc[dis_id['State'] == s]    
    m = 1
    l_case = 0
    l_date = datetime.datetime(2020,3,14)
    sid = list(st_id['State_Code'])[0]
    m_m,pm_m = 0,0
    c = 0
    m_list, id_list = list(), list()
    for j in range(0,17):
        mon = l_date.strftime("%m")
        if mon == '01' or mon == '03' or mon == '05' or mon == '07' or mon == '08' or mon == '10' or mon == '12':
            c_date = l_date + datetime.timedelta(days=(31))
        elif mon == '04' or mon == '06' or mon == '09' or mon == '11':
            c_date = l_date + datetime.timedelta(days=(30))
        else:
            c_date = l_date + datetime.timedelta(days=(28))
        temp = st.loc[st['Date'] == (str(c_date).split(' ')[0])]
        if temp.empty:
            temp_c = 0
            temp_r = 0
            temp_d = 0
        else:
            temp_c = temp['Confirmed'].sum()
            temp_r = temp['Recovered'].sum()
            temp_d = temp['Deceased'].sum()
        c_case = temp_c - temp_r - temp_d
        if c_case < l_case:
            c_case = l_case
        m_case = c_case - l_case
        l_case = c_case
        l_date = c_date
        
        if m_case > m_m:
            m_m = m_case
            mid = m
        if m_m == pm_m and m_m != 0:
            c = c + 1
        if m_m != pm_m:
            c = 0
            pm_m = m_m
        if c == 2:
            m_list.append(m_m)
            id_list.append(mid)
            m_m = 0
            pm_m = 0
            c = 0
        i = i + 1
        m = m + 1
    if len(id_list) < 2:
        if len(id_list) < 1:
            m1_list.append(int(-1))
        else:
            if id_list[0] < 10:
                m1_list.append(id_list[0])
                m2_list.append(int(-1))
            else:
                m2_list.append(id_list[0])
                m1_list.append(int(-1))
    else:
        idx = np.argsort(m_list)
        wave1 = id_list[-1]
        wave2 = id_list[-2]
        if wave2 < wave1:
            wave1, wave2 = wave2, wave1
        if wave1 > 10:
            wave2 = wave1
            wave1 = -1
        if wave2 < 10:
            wave1 = wave2
            wave2 = -1
        m1_list.append(wave1)
        m2_list.append(wave2)
    
for i in range(0,len(sid_list)):
    peak_sta.loc[i] = [sid_list[i], w1_list[i], w2_list[i], m1_list[i], m2_list[i]]
    
    
i = 0
w = 1
l_case1 = 0
l_date1 = datetime.datetime(2020,3,14)
l_date2 = datetime.datetime(2020,3,19)
temp = data.loc[data['Date'] == (str(l_date2).split(' ')[0])]
if temp.empty:
    temp_c = 0
    temp_r = 0
    temp_d = 0
else:
    temp_c = temp['Confirmed'].sum()
    temp_r = temp['Recovered'].sum()
    temp_d = temp['Deceased'].sum()
l_case2 = temp_c - temp_r - temp_d



m_w,pm_w = 0,0
c = 0
m_list, id_list = list(), list()
for j in range(0, 517, 7):
    c_date1 = l_date1 + datetime.timedelta(days=(7))
    temp = data.loc[data['Date'] == (str(c_date1).split(' ')[0])]
    if temp.empty:
        temp_c = 0
        temp_r = 0
        temp_d = 0
    else:
        temp_c = temp['Confirmed'].sum()
        temp_r = temp['Recovered'].sum()
        temp_d = temp['Deceased'].sum()
    c_case1 = temp_c - temp_r - temp_d
    if c_case1 < l_case1:
        c_case1 = l_case1
    w_case1 = c_case1 - l_case1
    l_case1 = c_case1
    l_date1 = c_date1
        
    c_date2 = l_date2 + datetime.timedelta(days=(7))
    temp = data.loc[data['Date'] == (str(c_date2).split(' ')[0])]
    if temp.empty:
        temp_c = 0
        temp_r = 0
        temp_d = 0
    else:
        temp_c = temp['Confirmed'].sum()
        temp_r = temp['Recovered'].sum()
        temp_d = temp['Deceased'].sum()
    c_case2 = temp_c - temp_r - temp_d
    if c_case2 < l_case2:
        c_case2 = l_case2
    w_case2 = c_case2 - l_case2
    l_case2 = c_case2
    l_date2 = c_date2
    if w_case1 > m_w:
        m_w = w_case1
        wid = w
    if w_case2 > m_w:
        m_w = w_case2
        wid = w + 1
    if m_w == pm_w and m_w != 0:
        c = c + 1
    if m_w != pm_w:
        c = 0
    pm_w = m_w
    if c == 8:
        m_list.append(m_w)
        id_list.append(wid)
        m_w = 0
        pm_w = 0
        c = 0

    i = i + 2
    w = w + 2
            


m_m,pm_m = 0,0
c = 0
i = 0
m = 1
l_case = 0
l_date = datetime.datetime(2020,3,14)
for j in range(0,17):
    mon = l_date.strftime("%m")
    if mon == '01' or mon == '03' or mon == '05' or mon == '07' or mon == '08' or mon == '10' or mon == '12':
        c_date = l_date + datetime.timedelta(days=(31))
    elif mon == '04' or mon == '06' or mon == '09' or mon == '11':
        c_date = l_date + datetime.timedelta(days=(30))
    else:
        c_date = l_date + datetime.timedelta(days=(28))
    temp = data.loc[data['Date'] == (str(c_date).split(' ')[0])]
    if temp.empty:
        temp_c = 0
        temp_r = 0
        temp_d = 0
    else:
        temp_c = temp['Confirmed'].sum()
        temp_r = temp['Recovered'].sum()
        temp_d = temp['Deceased'].sum()
    c_case = temp_c - temp_r - temp_d
    if c_case < l_case:
        c_case = l_case
    m_case = c_case - l_case
    l_case = c_case
    l_date = c_date
    if m_case > m_m:
        m_m = m_case
        mid = m
    if m_m == pm_m and m_m != 0:
        c = c + 1
    if m_m != pm_m:
        c = 0
    pm_m = m_m
    if c == 2:
        m_list.append(m_m)
        id_list.append(mid)
        m_m = 0
        pm_m = 0
        c = 0
    i = i + 1
    m = m + 1


peak_over = pd.DataFrame(columns = ['countryid', 'wave1-weekid', 'wave2-weekid', 'wave1-monthid', 'wave2-monthid'])
peak_over.loc[0] = ['IND', id_list[0], id_list[1], id_list[2], id_list[3]]


peak_dis.replace([-1], "NaN", inplace = True)
peak_sta.replace([-1], "NaN", inplace = True)
peak_over.replace([-1], "NaN", inplace = True)



peak_dis.to_csv('output-files/district-peaks.csv', index = False)
peak_sta.to_csv('output-files/state-peaks.csv', index = False)
peak_over.to_csv('output-files/overall-peaks.csv', index = False)

