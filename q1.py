#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import json
f = open('neighbor-districts.json',)
n_dist = json.load(f)
chng_dist = {'aizwal' : 'aizawl','anugul' : 'angul','ashok nagar' : 'ashoknagar','badgam' : 'budgam',
                'baleshwar' : 'balasore','banas kantha' : 'banaskantha','bangalore rural' : 'bengaluru rural',
                'bangalore urban' : 'bengaluru urban','baramula' : 'baramulla','baudh' : 'boudh','belgaum' : 'belagavi',
                'bellary' : 'ballari','bemetara' : 'bametara','bid' : 'beed','bishwanath' : 'biswanath',
                'chamarajanagar' : 'chamarajanagara','dantewada' : 'dakshin bastar dantewada','debagarh' : 'deogarh',
                'devbhumi dwaraka' : 'devbhumi dwarka','dhaulpur' : 'dholpur','east karbi anglong' : 'karbi anglong',
                'faizabad' : 'ayodhya','fategarh sahib' : 'fatehgarh sahib','firozpur' : 'ferozepur','gondiya' : 'gondia',
                'hugli' : 'hooghly','jagatsinghapur' : 'jagatsinghpur','jajapur' : 'jajpur','jalor' : 'jalore',
                'janjgir-champa' : 'janjgir champa','jhunjhunun' : 'jhunjhunu','jyotiba phule nagar' : 'amroha',
                'kabirdham' : 'kabeerdham','kaimur (bhabua)' : 'kaimur','kanchipuram' : 'kancheepuram',
                'kochbihar' : 'cooch behar','kodarma' : 'koderma','komram bheem' : 'komaram bheem',
                'lahul and spiti' : 'lahaul and spiti','mahesana' : 'mehsana','mahrajganj' : 'maharajganj','maldah' : 'malda',
                'marigaon' : 'morigaon','medchal–malkajgiri' : 'medchal malkajgiri','muktsar' : 'sri muktsar sahib',
                'mumbai city' : 'mumbai','nandubar' : 'nandurbar','narsimhapur' : 'narsinghpur','nav sari' : 'navsari',
                'pakaur' : 'pakur','palghat' : 'palakkad','panch mahal' : 'panchmahal','pashchim champaran' : 'west champaran',
                'pashchimi singhbhum' : 'west singhbhum',
                'purba champaran' : 'east champaran','purbi singhbhum' : 'east singhbhum','puruliya' : 'purulia',
                'rae bareilly' : 'rae bareli','rajauri' : 'rajouri','rangareddy' : 'ranga reddy','ri-bhoi' : 'ribhoi',
                'sabar kantha' : 'sabarkantha','sahibzada ajit singh nagar' : 's.a.s. nagar',
                'sait kibir nagar' : 'sant kabir nagar','sant ravidas nagar' : 'bhadohi','sepahijala' : 'sipahijala',
                'seraikela kharsawan' : 'saraikela-kharsawan','shaheed bhagat singh nagar' : 'shahid bhagat singh nagar',
                'sharawasti' : 'shrawasti','shimoga' : 'shivamogga','shopian' : 'shopiyan','siddharth nagar' : 'siddharthnagar',
                'sivagangai' : 'sivaganga','sonapur' : 'subarnapur','south salmara-mankachar' : 'south salmara mankachar',
                'sri ganganagar' : 'ganganagar','sri potti sriramulu nellore' : 's.p.s. nellore','the dangs' : 'dang',
                'the nilgiris' : 'nilgiris','thoothukudi' : 'thoothukkudi','tiruchchirappalli' : 'tiruchirappalli',
                'tirunelveli kattabo' : 'tirunelveli','tiruvanamalai' : 'tiruvannamalai','tumkur' : 'tumakuru',
                'yadagiri' : 'yadgir','ysr' : 'y.s.r. kadapa'
 }
v_dist = pd.read_csv('cowin_vaccine_data_districtwise.csv',header=[0],skiprows=[1])
v_dist = v_dist.sort_values(by = 'District_Key')
v_dist["District"] = v_dist["District"].str.lower()

crt_name = {}
for key in sorted(n_dist):
    name = key.split('/')[0]
    n_code = key.split('/')[1]
    name = name.replace("_"," ")
    name = name.replace(" district","")
    val = []
    for value in sorted(n_dist[key]):
        v_name = value.split('/')[0]
        v_code = value.split('/')[1]
        v_name = v_name.replace("_"," ")
        v_name = v_name.replace(" district","")
        if v_name in chng_dist.keys():
            c_name = chng_dist[v_name] + '/' + v_code
            val.append(c_name)
        else:
            c_name = v_name + '/' + v_code
            val.append(c_name)
    if name in chng_dist.keys():
        c_name = chng_dist[name] + '/' + n_code
        crt_name[c_name] = val
    else:
        c_name = name + '/' + n_code
        crt_name[c_name] = val

id_name = {}
for key in crt_name:
    name = key.split('/')[0]
    n_code = key.split('/')[1]
    if name == 'hamirpur' or name == 'pratapgarh':
        if n_code == 'Q2019757':
            c_name = 'UP_Hamirpur' + '/' + n_code
            id_name[c_name] = crt_name[key]
        elif n_code == 'Q2086180':
            c_name = 'HP_Hamirpur' + '/' + n_code
            id_name[c_name] = crt_name[key]
        elif n_code == 'Q1473962':
            c_name = 'UP_Pratapgarh' + '/' + n_code
            id_name[c_name] = crt_name[key]
        else:
            c_name = 'RJ_Pratapgarh' + '/' + n_code
            id_name[c_name] = crt_name[key]
    else:
        for i in range(len(v_dist["District"])):
            if v_dist['District'].iloc[i] == name:
                c_name = v_dist['District_Key'].iloc[i] + '/' + n_code
                id_name[c_name] = crt_name[key]
                v_dist.drop([i])
                continue
n_list = list(id_name.keys())
final_dict = {}
for key in sorted(id_name):
    name = key.split('/')[0]
    n_code = key.split('/')[1]
    v_list = []
    for val in sorted(id_name[key]):
        v_name = val.split('/')[0]
        v_code = val.split('/')[1]
        for i in range(len(n_list)):
            code = n_list[i].split('/')[1]
            if v_code == code:
                v_list.append(n_list[i].split('/')[0])
                break
    final_dict[name] = v_list
with open("output-files/neighbor-districts-modified.json", "w") as f:
    json.dump(final_dict, f)


# In[ ]:




