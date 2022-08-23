#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import datetime
data = pd.read_csv("districts.csv")
dis_id = pd.read_csv("cowin_vaccine_data_districtwise.csv", header = [0], skiprows = [1])
over = pd.DataFrame(columns = ['districtid', 'overall'])


z = 1
i = 0
x = str(datetime.datetime(2021, 8, 14)).split(' ')[0]
sta_lis = list(set(data['State']))
sta_lis.sort()
for s in sta_lis:
    st = data.loc[data['State'] == s]
    st_id = dis_id.loc[dis_id['State'] == s]
    dname = list(set(st['District']))
    dname.sort()
    did = list(st_id['District'])
    for d in dname:
        if d == 'Unknown':
            if len(dname) == 1:
                dt = st.loc[st['District'] == d]
                tot = list(dt['Confirmed'].loc[dt['Date'] == x])[0]
                sid = list(st_id['State_Code'])[0]
                over.loc[i] = [sid, tot]
            else:
                continue
        elif d in did:
            
            dt = st.loc[st['District'] == d]
            dt_id = list(st_id['District_Key'].loc[st_id['District'] == d])[0]
            tot = list(dt['Confirmed'].loc[dt['Date'] == x])[0]
            over.loc[i] = [dt_id, tot]
        elif d == s:
            dt = st.loc[st['District'] == d]
            tot = list(dt['Confirmed'].loc[dt['Date'] == x])[0]
            sid = list(st_id['State_Code'])[0]
            over.loc[i] = [sid, tot]
        else:
            continue
        i = i + 1





week = pd.DataFrame(columns = ['districtid', 'weekid', 'cases'])

i = 0
for s in sta_lis:
    st = data.loc[data['State'] == s]
    st_id = dis_id.loc[dis_id['State'] == s]
    dname = list(set(st['District']))
    dname.sort()
    did = list(st_id['District'])
    for d in dname:
        w = 1
        l_case = 0
        l_date = datetime.datetime(2020,3,14)
        if d == 'Unknown':
            if len(dname) == 1:
                dt = st.loc[st['District'] == d]
                sid = list(st_id['State_Code'])[0]
                for j in range(0, 517, 7):
                    c_date = l_date + datetime.timedelta(days=(7))
                    temp = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                    if temp == []:
                        c_case = 0
                    else:
                        c_case = temp[0]
                    if c_case < l_case:
                        c_case = l_case
                    w_case = c_case - l_case
                    l_case = c_case
                    l_date = c_date
                    week.loc[i] = [sid, w, w_case]
                    i = i + 1
                    w = w + 1
            else:
                continue
        elif d in did:
            
            dt = st.loc[st['District'] == d]
            dt_id = list(st_id['District_Key'].loc[st_id['District'] == d])[0]
            for j in range(0, 517, 7):
                c_date = l_date + datetime.timedelta(days=(7))
                temp = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                if temp == []:
                    c_case = 0
                else:
                    c_case = temp[0]
                if c_case < l_case:
                    c_case = l_case
                w_case = c_case - l_case
                l_case = c_case
                l_date = c_date
                week.loc[i] = [dt_id, w, w_case]
                i = i + 1
                w = w + 1
        elif d == s:
            dt = st.loc[st['District'] == d]
            sid = list(st_id['State_Code'])[0]
            for j in range(0, 517, 7):
                c_date = l_date + datetime.timedelta(days=(7))
                temp = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                if temp == []:
                    c_case = 0
                else:
                    c_case = temp[0]
                if c_case < l_case:
                    c_case = l_case
                w_case = c_case - l_case
                l_case = c_case
                l_date = c_date
                week.loc[i] = [sid, w, w_case]
                i = i + 1
                w = w + 1
        
week.to_csv("output-files/cases-week.csv", index = False)
                
                
                
                
                
month = pd.DataFrame(columns = ['districtid', 'monthid', 'cases'])
e_date = str(datetime.datetime(2021,8,14)).split(' ')[0]
i = 0
for s in sta_lis:
    st = data.loc[data['State'] == s]
    st_id = dis_id.loc[dis_id['State'] == s]
    dname = list(set(st['District']))
    dname.sort()
    did = list(st_id['District'])
    for d in dname:
        m = 1
        l_case = 0
        l_date = datetime.datetime(2020,3,14)
        if d == 'Unknown':
            if len(dname) == 1:
                dt = st.loc[st['District'] == d]
                sid = list(st_id['State_Code'])[0]
                for j in range(0,17):
                    mon = l_date.strftime("%m")
                    if mon == '01' or mon == '03' or mon == '05' or mon == '07' or mon == '08' or mon == '10' or mon == '12':
                        c_date = l_date + datetime.timedelta(days=(31))
                    elif mon == '04' or mon == '06' or mon == '09' or mon == '11':
                        c_date = l_date + datetime.timedelta(days=(30))
                    else:
                        c_date = l_date + datetime.timedelta(days=(28))
                    temp = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                    if temp == []:
                        c_case = 0
                    else:
                        c_case = temp[0]
                    if c_case < l_case:
                        c_case = l_case
                    m_case = c_case - l_case
                    l_case = c_case
                    l_date = c_date
                    month.loc[i] = [sid, m, m_case]
                    i = i + 1
                    m = m + 1
            else:
                continue
        elif d in did:
            
            dt = st.loc[st['District'] == d]
            dt_id = list(st_id['District_Key'].loc[st_id['District'] == d])[0]
            for j in range(0,17):
                mon = l_date.strftime("%m")
                if mon == '01' or mon == '03' or mon == '05' or mon == '07' or mon == '08' or mon == '10' or mon == '12':
                    c_date = l_date + datetime.timedelta(days=(31))
                elif mon == '04' or mon == '06' or mon == '09' or mon == '11':
                    c_date = l_date + datetime.timedelta(days=(30))
                else:
                    c_date = l_date + datetime.timedelta(days=(28))
                temp = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                if temp == []:
                    c_case = 0
                else:
                    c_case = temp[0]
                if c_case < l_case:
                    c_case = l_case
                m_case = c_case - l_case
                l_case = c_case
                l_date = c_date
                month.loc[i] = [dt_id, m, m_case]
                i = i + 1
                m = m + 1
        elif d == s:
            dt = st.loc[st['District'] == d]
            sid = list(st_id['State_Code'])[0]
            for j in range(0,17):
                mon = l_date.strftime("%m")
                if mon == '01' or mon == '03' or mon == '05' or mon == '07' or mon == '08' or mon == '10' or mon == '12':
                    c_date = l_date + datetime.timedelta(days=(31))
                elif mon == '04' or mon == '06' or mon == '09' or mon == '11':
                    c_date = l_date + datetime.timedelta(days=(30))
                else:
                    c_date = l_date + datetime.timedelta(days=(28))
                temp = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                if temp == []:
                    c_case = 0
                else:
                    c_case = temp[0]
                if c_case < l_case:
                    c_case = l_case
                m_case = c_case - l_case
                l_case = c_case
                l_date = c_date
                month.loc[i] = [sid, m, m_case]
                i = i + 1
                m = m + 1
                
month.to_csv("output-files/cases-month.csv", index = False)


over = pd.DataFrame(columns = ['districtid', 'overallid', 'cases'])
i = 0
for s in sta_lis:
    st = data.loc[data['State'] == s]
    st_id = dis_id.loc[dis_id['State'] == s]
    dname = list(set(st['District']))
    dname.sort()
    did = list(st_id['District'])
    for d in dname:
        l_case = 0
        l_date = datetime.datetime(2020,3,14)
        c_date = datetime.datetime(2021,8,14)
        if d == 'Unknown':
            if len(dname) == 1:
                dt = st.loc[st['District'] == d]
                sid = list(st_id['State_Code'])[0]
                temp = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
                if temp == []:
                    c_case = 0
                else:
                    c_case = temp[0]
                if c_case < l_case:
                    c_case = l_case
                o_case = c_case - l_case
                over.loc[i] = [sid, 1, o_case]
                i = i + 1
            else:
                continue
        elif d in did:
            
            dt = st.loc[st['District'] == d]
            dt_id = list(st_id['District_Key'].loc[st_id['District'] == d])[0]
            temp = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
            if temp == []:
                c_case = 0
            else:
                c_case = temp[0]
            if c_case < l_case:
                c_case = l_case
            o_case = c_case - l_case
            over.loc[i] = [dt_id, 1, o_case]
            i = i + 1
        elif d == s:
            dt = st.loc[st['District'] == d]
            sid = list(st_id['State_Code'])[0]
            temp = list(dt['Confirmed'].loc[dt['Date'] == (str(c_date).split(' ')[0])])
            if temp == []:
                c_case = 0
            else:
                c_case = temp[0]
            if c_case < l_case:
                c_case = l_case
            o_case = c_case - l_case
            over.loc[i] = [sid, 1, o_case]
            i = i + 1
over.to_csv("output-files/cases-overall.csv", index = False)


# In[ ]:




