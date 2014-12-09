# -*- coding: utf-8 -*-
"""
Data Cleaning
"""
# Step 1: Read MySQL data tables back to Python as Pandas Data Frame
import pandas as pd
import MySQLdb

# Establish a connection to the database
conn = MySQLdb.connect(host='localhost',user='root', passwd='pass_word',db='GroupProject')

# Read the SQL tables
jobNYC = pd.read_sql("SELECT * from jobNYC", conn)
jobSJ = pd.read_sql("SELECT * from jobSJ", conn)
jobSEA = pd.read_sql("SELECT * from jobSEA", conn)
jobSF = pd.read_sql("SELECT * from jobSF", conn)
jobAUS = pd.read_sql("SELECT * from jobAUS", conn)
jobBOS = pd.read_sql("SELECT * from jobBOS", conn)
jobDC = pd.read_sql("SELECT * from jobDC", conn)
jobCHI = pd.read_sql("SELECT * from jobCHI", conn)


# Step 2: Create region columns
jobNYC['REGION'] = 'New York, NY'
jobSJ['REGION'] = "San Jose, CA"
jobSEA['REGION'] = "Seattle, WA"
jobSF['REGION'] = "San Francisco, CA"
jobAUS['REGION'] = "Austin, TX"
jobBOS['REGION'] = "Boston, MA"
jobDC['REGION'] = 'Washington, DC'
jobCHI['REGION'] = "Chicago, IL"


# Step 3: Create Job_Summary columns cleansed of capitalization and punctuation
#         and save the data in Data Frames

allJobs = [jobNYC, jobSJ, jobSEA, jobSF, jobAUS, jobBOS, jobDC, jobCHI]

i=0
for eachJob in allJobs:
    i = i +1
    
    if i == 1:
        jobNYC['JOB_SUMMARY2'] = jobNYC['JOB_SUMMARY'].str.replace('[^\w\s]','')
        jobNYC['JOB_SUMMARY2'] = jobNYC.JOB_SUMMARY2.str.lower()
    
    if i == 2:
        jobSJ['JOB_SUMMARY2'] = jobSJ['JOB_SUMMARY'].str.replace('[^\w\s]','')
        jobSJ['JOB_SUMMARY2'] = jobSJ.JOB_SUMMARY2.str.lower()
    
    if i == 3:
        jobSEA['JOB_SUMMARY2'] = jobSEA['JOB_SUMMARY'].str.replace('[^\w\s]','')
        jobSEA['JOB_SUMMARY2'] = jobSEA.JOB_SUMMARY2.str.lower()
    
    if i == 4:
        jobSF['JOB_SUMMARY2'] = jobSF['JOB_SUMMARY'].str.replace('[^\w\s]','')
        jobSF['JOB_SUMMARY2'] = jobSF.JOB_SUMMARY2.str.lower()
    
    if i == 5:
        jobAUS['JOB_SUMMARY2'] = jobAUS['JOB_SUMMARY'].str.replace('[^\w\s]','')
        jobAUS['JOB_SUMMARY2'] = jobAUS.JOB_SUMMARY2.str.lower()
    
    if i == 6:
        jobBOS['JOB_SUMMARY2'] = jobBOS['JOB_SUMMARY'].str.replace('[^\w\s]','')
        jobBOS['JOB_SUMMARY2'] = jobBOS.JOB_SUMMARY2.str.lower()
    
    if i == 7:
        jobDC['JOB_SUMMARY2'] = jobDC['JOB_SUMMARY'].str.replace('[^\w\s]','')
        jobDC['JOB_SUMMARY2'] = jobDC.JOB_SUMMARY2.str.lower()
    
    if i == 8:
        jobCHI['JOB_SUMMARY2'] = jobCHI['JOB_SUMMARY'].str.replace('[^\w\s]','')
        jobCHI['JOB_SUMMARY2'] = jobCHI.JOB_SUMMARY2.str.lower()

    
# Step 4 : Remove stop words in JOB_SUMMARY2
from nltk.corpus import stopwords

def textClean(text):
    # Remove stop words    
    text_result = ' '.join([word for word in text.split() if word not in stopwords.words("english")])
    return text_result

allJobs = [jobNYC,jobSJ,jobSEA,jobSF,jobAUS,jobBOS,jobDC,jobCHI]

i=0
for eachCity in allJobs:
    i = i +1
    job_brief = []
    
    for text in eachCity['JOB_SUMMARY2']:
        result_text = textClean(text)
        job_brief.append(result_text)
    
    if i == 1:
        jobNYC['JOB_BRIEF'] = pd.Series(job_brief)
    
    if i == 2:
        jobSJ['JOB_BRIEF'] = pd.Series(job_brief)

    if i == 3:
        jobSEA['JOB_BRIEF'] = pd.Series(job_brief) 

    if i == 4:
        jobSF['JOB_BRIEF'] = pd.Series(job_brief) 

    if i == 5:
        jobAUS['JOB_BRIEF'] = pd.Series(job_brief) 

    if i == 6:
        jobBOS['JOB_BRIEF'] = pd.Series(job_brief) 
        
    if i == 7:
        jobDC['JOB_BRIEF'] = pd.Series(job_brief)
        
    if i == 8:
        jobCHI['JOB_BRIEF'] = pd.Series(job_brief) 

# Step 5: Save the combined data file
combinedJobs = jobNYC
combinedJobs = combinedJobs.append(jobSJ)
combinedJobs = combinedJobs.append(jobSEA)
combinedJobs = combinedJobs.append(jobSF)
combinedJobs = combinedJobs.append(jobAUS)
combinedJobs = combinedJobs.append(jobBOS)
combinedJobs = combinedJobs.append(jobDC)
combinedJobs = combinedJobs.append(jobCHI)

combinedJobs.to_csv("combinedJobs.csv",index=False)

# Step 6: Import the Data Frame combinedJobs into MySQL
import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',user='root', passwd='pass_word',db='GroupProject')
cursor = mydb.cursor()

sql = '''
          CREATE TABLE combinedJobs (
                                    COMPANY CHAR(100) NOT NULL, 
                                    JOB_SUMMARY VARCHAR(5000),
                                    JOB_TITLE CHAR(100) NOT NULL,                           
                                    LOCATION CHAR(100) NOT NULL,
                                    REGION CHAR(100),
                                    JOB_SUMMARY2 VARCHAR(5000),
                                    JOB_BRIEF VARCHAR(5000));
        '''
cursor.execute(sql)

# load data combinedJobs
combinedJobs_csv_data = csv.reader(file('combinedJobs.csv'))
header=combinedJobs_csv_data.next()
for row in combinedJobs_csv_data:
    sql = '''
          INSERT INTO combinedJobs VALUES(%s,%s,%s,%s,%s,%s,%s);
          '''
    cursor.execute(sql,row)
mydb.commit()
cursor.close()
