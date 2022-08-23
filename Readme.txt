Please read this before executing the assignment:-

Plugins-
Software: python3(.sh files run python3 files)

Dependencies-
Python Libraries: pandas, numpy, json, datetime

Programs-

.sh files:

assign1.sh 
  Top level script that runs the entire assignment

neighbor-modifer.sh(No naming convention was given for Ques1)
  Runs q1.py python file
  Generates neighbor-districts-modified.json 

edge-generator.sh
  Runs q2.py python file
  Generates edge-graph.csv

case-generator.sh
  Runs q3.py python file
  Generates cases-time.csv

peaks-generator.sh
  Runs q4.py python file
  Generates area-peaks.csv

vaccinated-count-generator.sh
  Runs q5.py python file
  Generates area-vaccinated-count-time.csv

vaccination-population-ratio-generator.sh
  Runs q6.py python file
  Generates area-vaccination-population-ratio.csv

vaccine-type-ratio-generator.sh
  Runs q7.py python file
  Generates area-vaccine-type-ratio.csv

vaccinated-ratio-generator.sh
  Runs q8.py python file
  Generates area-vaccinated-dose-ratio.csv

complete-vaccination-generator.sh
  Runs q9.py python file
  Generates complete-vaccination.csv

How to use:
To run the whole assignment at once run the following command from the terminal-
bash assign1.sh 

To run each code seperately run the following command from the terminal-
bash FILE_NAME.sh
where FILE_NAME is the name of the .sh file you want to run

Output-
All the output files generated are stored in the 'output-files' folder.

I have used state code for those districts that are merged in the covid data(like Andaman and Nicobars(AN), Delhi(DL), and a few others)

In question 4, for some districts and states there were not enough cases to cause a peak in either wave1 or wave2 or both. For such cases I have used 'NaN' to represent that there
is no wave.

In question 7, for some districts and states no covaxin doses were administered so the ratio for those districts and state is shown as 'NaN'.

In question 9, for some states the number of vaccinated people already crossed the total population before 14/08/2021 thus, for those states I have changed populationleft to 0. The
date column shows the date in "yy/mm/dd" pattern.

For each question whose output required seperate csv file for district, state and overall, I have added area to the name of those output files. Here area is district, state and overall
as required for the output file.


Some points to keep in mind:

If any sh file does not execute please change permissions for the file and try again.

All the python programs and the datasets are provided in the same folder. Python program are named q1,q2,q3, and so on for each question repectively

Along with all the datasets provided for this assignment I have created and used a dataset named old_to_new_map.csv to map the old names given in the census data to the new names given 
in Cowin data. 
   
Please keep all the python programs, the datasets and the CSV files folder within the same directory otherwise, there will be execution errors.

Please do not use any dataset other than those provided by me as I have removed some Null values from the dataset manually and the programming is done with these datasets in
consideration.
  