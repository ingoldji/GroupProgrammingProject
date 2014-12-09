# -*- coding: utf-8 -*-
"""
SIC Code Analysis
"""
#PROGRAMMING FOR ANALYTICS - GROUP PROJECT - SIC CODE ANALYSES
#IN ORDER FOR THIS CODE TO WORK, THERE MUST EXIST A TABLE WITH A LIST OF EMPLOYERS CALLED "COMPANY."
#THE DATA CURRENTLY RETRIEVES INFORMATION FROM A TABLE CALLED "JOBALL" BUT CAN BE CHANGED IF NECESSARY AS LONG AS IT FITS THE ABOVE REQUIREMENT.
#CHANGE MYSQL CREDENTIALS AS NEEDED.

#IMPORTING OF PACKAGES:
import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import MySQLdb
import csv


#First Generate the list of Unique Employers:
myDB = MySQLdb.connect(host='localhost',user='root', passwd='root',db='GroupProject')
cursor = myDB.cursor()
cursor.execute("select distinct company from jobALL;")
employers = [row[0] for row in cursor.fetchall()]  

#In order for the program to work, the list of employers has to be cleaned. This includes remove characters like commas:
employersrevisedlist=[]
for employer in employers:
    employerrevised = employer.replace(",","")
    employersrevisedlist.append(employerrevised)
    

#Define a Base URL:
base_url= 'http://siccode.com/en/search/'
my_urls=[]

#MORE CLEANING IS OCURRING HERE:
#THIS MEANS REMOVING ALL +++, and paranthesis ( or )
for eachemployer in employersrevisedlist:
    full_url = base_url + eachemployer
    full_url_formatted = full_url.replace(" ","+")   
    #Three Plusses:
    full_url_formatted = full_url_formatted.replace("+++"," + ")    
   #Removal of Parantheses:
    full_url_formatted = full_url_formatted.replace("(","+")
    full_url_formatted = full_url_formatted.replace(")","+")
    my_urls.append(full_url_formatted)
    
#THIS IS A FUNCTION DEFINED TO ACTUALLY RETRIEVE THE SIC CODE FROM A WEB PAGE.
def getSicCode(aurl):
    optionsUrl = aurl
    newPage = urllib2.urlopen(optionsUrl)
    soup = BeautifulSoup(newPage)
    base = soup.findAll('span',attrs={'class':'code'})
    base2 = str(base)
    allRows = BeautifulSoup(base2)
    #tableData = []
    for cell in allRows:
        tableData = str(cell.text.strip())
    tableData1 = tableData[1:]
    tableData2 = tableData1[:-1]
    mylist = tableData2.split(',')
    mylist2 = [s.strip() for s in mylist]
    shortened_list = mylist2[0:1]
    return shortened_list

allemployers = []
allsiccodes = []

C=0

#THE FOLLOWING RUNS THE FUNCTION FOR EACH SIC CODE AND STORES THE INFORMATION INTO LISTS:
for each_url in my_urls:
    new_sic_codes = getSicCode(each_url)
    
    for i in range(0,len(new_sic_codes)):
        #print new_sic_codes[i]
        #allemployers.append()
        allsiccodes.append(new_sic_codes[i])
        allemployers.append(employers[C])
        
    C= C+1   
    print "Employer Number",C, " SIC Codes Added"
   
#FROM LISTS THE DATA THEN GOES INTO A DICTIONARY:   
employer_sic = {
            'employer' : allemployers,
            'SIC' : allsiccodes
        }
           
#FROM A DICTIONARY THE DATA MOVES ONTO A PANDAS DATAFRAME
df_employer_sic = pd.DataFrame(employer_sic)

                  
#FROM A DATAFRAME THE DATA MOVES ON TO A MYSQL DATABASE
df_employer_sic.to_sql(con=myDB,
                name='employer_sic_1',
                if_exists='replace',
                flavor='mysql')  
                
print "***********************Job Complete****************************"


#cursor = myDB.cursor()

#ANOTHER DATABASE IS SUBSEQUENTLY GENERATED THAT INCLUDES THE SIC CODE AND THE COUNT RELATED TO THAT SIC CODE
sql ='''

select sic, count(sic)  as count from employer_sic_1 group by sic having count(sic)>2;

'''

cursor.execute(sql)
SIC = [row[0] for row in cursor.fetchall()]

cursor.execute(sql)
SIC_COUNT = [row[1] for row in cursor.fetchall()]    

SIC_COUNT_REVISED=[]
for sic_count_item in SIC_COUNT:
    sic_count_item_revised = str(sic_count_item)
    sic_count_item_revised = int(sic_count_item_revised)
    SIC_COUNT_REVISED.append(sic_count_item_revised)
 

   
employer_sic_count = {
            'SIC' : SIC,
            'COUNT' : SIC_COUNT_REVISED
        }

df_employer_sic_count = pd.DataFrame(employer_sic_count)


#THIS DOES A PLOT DIRECTLY FROM DATAFRAME. I'VE COMMENTED THIS PORTION OUT FOR NOW:
df_employer_sic_count.plot(x="SIC", y="COUNT", kind="bar")  



    
#THIS IS A STANDARD MATPLOT GRAPH
import numpy as np
import matplotlib.pyplot as plt


n_groups = len(SIC_COUNT_REVISED)
bar_sic_code = SIC_COUNT_REVISED
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.30
opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, bar_sic_code, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 )

plt.xticks(index + .15, (SIC))
plt.legend()
plt.show()

