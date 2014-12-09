# -*- coding: utf-8 -*-
"""
Indeed Data Gathering
"""
#Step 1: Define the web scraping function
import urllib2
from bs4 import BeautifulSoup

def getJobInfo(aURL):
    ''' Get Business Analytics realted job information from Indeed '''
    URL = aURL
    Page = urllib2.urlopen(URL)
    Soup = BeautifulSoup(Page)
    
    dataTable = []

    job_title = str(Soup.find('b').text.strip())
    
    company = Soup.find('span',attrs={'class':'company'})
    if company != None:
        company = str(company.text.strip())
    elif company == None:
        company = 'NULL'
        
    location = str(Soup.find('span',attrs={'class':'location'}).text.strip())
        
    job_summary = Soup.find('span',attrs={'class':'summary'})
    # Dinfine a funtion to remove the </br> and </li> tags
    def text_with_newlines(element):
        text = ''
        for e in element.recursiveChildGenerator():
            if isinstance(e, basestring):
                text += e.strip()
            elif e.name == 'br':
                text += '\n'
            elif e.name == 'li':
                text += '\n*'
        return text
    job_summary = text_with_newlines(job_summary)
    job_summary = str(job_summary)
    
    dataTable = [job_title,company,location,job_summary]
    return dataTable


# Step 2: Obtain the target URLs
from indeed import IndeedClient

#Target locations and job titles
Locations = ["New York, NY", "San Jose, CA", "Seattle, WA", "San Francisco, CA", "Austin, TX", "Boston, MA", "Washington, DC", "Chicago, IL"]
Titles = ["Data+analyst","Data+Scientist","Quantitative+Analyst", "Quantitative+Researcher", "Business+Analyst", "Big+Data", "Web+Analyst"]

#Obtain the URLs for the top maximum 25 jobs meeting the search criteria in each city
client = IndeedClient(publisher = "261623550181466")
urllistNYC = []
urllistSJ = []
urllistSEA = []
urllistSF = []
urllistAUS = []
urllistBOS = []
urllistDC = []
urllistCHI = []

for L in Locations:
    for T in Titles:
        params = {
            'q' : T,
            'l' : L,
            'userip' : "1.2.3.4",
            'useragent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)",
            'limit' : 25
        } 
        urllist = []
        search_response = client.search(**params)
        data = search_response.get('results')  
        urllist = [item['url'] for item in data]
        if L == "New York, NY":
            urllistNYC.extend(urllist)
        if L == "San Jose, CA":
            urllistSJ.extend(urllist)
        if L == "Seattle, WA":
            urllistSEA.extend(urllist)
        if L == "San Francisco, CA":
            urllistSF.extend(urllist)
        if L == "Austin, TX":
            urllistAUS.extend(urllist)
        if L == "Boston, MA":
            urllistBOS.extend(urllist)
        if L == "Washington, DC":
            urllistDC.extend(urllist)
        if L == "Chicago, IL":
            urllistCHI.extend(urllist)


# Step 3: Scrape data from the websites
NYCjobinfo=[]
for aURL in urllistNYC:
    jobInfo = getJobInfo(aURL)
    NYCjobinfo.append(jobInfo)

SJjobinfo=[]
for aURL in urllistSJ:
    jobInfo = getJobInfo(aURL)
    SJjobinfo.append(jobInfo)

SEAjobinfo=[]
for aURL in urllistSEA:
    jobInfo = getJobInfo(aURL)
    SEAjobinfo.append(jobInfo)

SFjobinfo=[]
for aURL in urllistSF:
    jobInfo = getJobInfo(aURL)
    SFjobinfo.append(jobInfo)

AUSjobinfo=[]
for aURL in urllistAUS:
    jobInfo = getJobInfo(aURL)
    AUSjobinfo.append(jobInfo)

BOSjobinfo=[]
for aURL in urllistBOS:
    jobInfo = getJobInfo(aURL)
    BOSjobinfo.append(jobInfo)

DCjobinfo=[]
for aURL in urllistDC:
    jobInfo = getJobInfo(aURL)
    DCjobinfo.append(jobInfo)

CHIjobinfo=[]
for aURL in urllistCHI:
    jobInfo = getJobInfo(aURL)
    CHIjobinfo.append(jobInfo)


# Step 4: Save the data in DataFrame and csv files
import pandas as pd
allJobs = [NYCjobinfo,SJjobinfo,SEAjobinfo,SFjobinfo,AUSjobinfo,BOSjobinfo,DCjobinfo,CHIjobinfo]

i=0
for eachCity in allJobs:
    i = i +1
    
    job_title = [x[0] for x in eachCity]
    company = [x[1] for x in eachCity]
    location = [x[2] for x in eachCity]
    job_summary = [x[3] for x in eachCity]
    
    myDict = {
              'JOB_TITLE':job_title,
              'COMPANY':company,
              'LOCATION': location,
              'JOB_SUMMARY':job_summary
              }
              
    if i == 1:
        jobNYC = pd.DataFrame(myDict)
        jobNYC = jobNYC.drop_duplicates()
    if i == 2:
        jobSJ = pd.DataFrame(myDict)
        jobSJ = jobSJ.drop_duplicates()
    if i == 3:
        jobSEA = pd.DataFrame(myDict)
        jobSEA = jobSEA.drop_duplicates()
    if i == 4:
        jobSF = pd.DataFrame(myDict)
        jobSF = jobSF.drop_duplicates()
    if i == 5:
        jobAUS = pd.DataFrame(myDict)
        jobAUS = jobAUS.drop_duplicates()
    if i == 6:
        jobBOS = pd.DataFrame(myDict)
        jobBOS = jobBOS.drop_duplicates()
    if i == 7:
        jobDC = pd.DataFrame(myDict)
        jobDC = jobDC.drop_duplicates()
    if i == 8:
        jobCHI = pd.DataFrame(myDict)
        jobCHI = jobCHI.drop_duplicates()

# Save the files in csv format
jobNYC.to_csv("jobNYC.csv",index=False)
jobSJ.to_csv("jobSJ.csv",index=False)
jobSEA.to_csv("jobSEA.csv",index=False)
jobSF.to_csv("jobSF.csv",index=False)
jobAUS.to_csv("jobAUS.csv",index=False)
jobBOS.to_csv("jobBOS.csv",index=False)
jobDC.to_csv("jobDC.csv",index=False)
jobCHI.to_csv("jobCHI.csv",index=False)


# Step 5: Import the csv files into MySQL
import csv
import MySQLdb

# Establish a connection to the database
conn = MySQLdb.connect(host='localhost',user='root', passwd='pass_word')

# create a cursor
cursor = conn.cursor()

# create a database
sql = 'CREATE DATABASE GroupProject;'
cursor.execute(sql)

sql = 'USE GroupProject;'
cursor.execute(sql)

cursor.close()

# create table jobNYC
mydb = MySQLdb.connect(host='localhost',user='root', passwd='pass_word',db='GroupProject')
cursor = mydb.cursor()

sql = '''
          CREATE TABLE jobNYC (
                            COMPANY CHAR(100) NOT NULL, 
                            JOB_SUMMARY VARCHAR(5000),
                            JOB_TITLE CHAR(100) NOT NULL,                           
                            LOCATION CHAR(100) NOT NULL);
        '''
cursor.execute(sql)

# load data jobNYC.csv
jobNYC_csv_data = csv.reader(file('jobNYC.csv'))
header=jobNYC_csv_data.next()
for row in jobNYC_csv_data:
    sql = 'INSERT INTO jobNYC VALUES(%s,%s,%s,%s);'
    cursor.execute(sql,row)
mydb.commit()
cursor.close()

# create table jobSJ
mydb = MySQLdb.connect(host='localhost',user='root', passwd='pass_word',db='GroupProject')
cursor = mydb.cursor()

sql = '''
          CREATE TABLE jobSJ (
                            COMPANY CHAR(100) NOT NULL, 
                            JOB_SUMMARY VARCHAR(5000),
                            JOB_TITLE CHAR(100) NOT NULL,                           
                            LOCATION CHAR(100) NOT NULL);
        '''
cursor.execute(sql)

# load data jobSJ.csv
jobSJ_csv_data = csv.reader(file('jobSJ.csv'))
header=jobSJ_csv_data.next()
for row in jobSJ_csv_data:
    sql = 'INSERT INTO jobSJ VALUES(%s,%s,%s,%s);'
    cursor.execute(sql,row)
mydb.commit()
cursor.close()

# create table jobSEA
mydb = MySQLdb.connect(host='localhost',user='root', passwd='pass_word',db='GroupProject')
cursor = mydb.cursor()

sql = '''
          CREATE TABLE jobSEA (
                            COMPANY CHAR(100) NOT NULL, 
                            JOB_SUMMARY VARCHAR(5000),
                            JOB_TITLE CHAR(100) NOT NULL,                           
                            LOCATION CHAR(100) NOT NULL);
        '''
cursor.execute(sql)

# load data jobSEA.csv
jobSEA_csv_data = csv.reader(file('jobSEA.csv'))
header=jobSEA_csv_data.next()
for row in jobSEA_csv_data:
    sql = 'INSERT INTO jobSEA VALUES(%s,%s,%s,%s);'
    cursor.execute(sql,row)
mydb.commit()
cursor.close()

# create table jobSF
mydb = MySQLdb.connect(host='localhost',user='root', passwd='pass_word',db='GroupProject')
cursor = mydb.cursor()

sql = '''
          CREATE TABLE jobSF (
                            COMPANY CHAR(100) NOT NULL, 
                            JOB_SUMMARY VARCHAR(5000),
                            JOB_TITLE CHAR(100) NOT NULL,                           
                            LOCATION CHAR(100) NOT NULL);
        '''
cursor.execute(sql)

# load data jobSF.csv
jobSF_csv_data = csv.reader(file('jobSF.csv'))
header=jobSF_csv_data.next()
for row in jobSF_csv_data:
    sql = 'INSERT INTO jobSF VALUES(%s,%s,%s,%s);'
    cursor.execute(sql,row)
mydb.commit()
cursor.close()

# create table jobAUS
mydb = MySQLdb.connect(host='localhost',user='root', passwd='pass_word',db='GroupProject')
cursor = mydb.cursor()

sql = '''
          CREATE TABLE jobAUS (
                            COMPANY CHAR(100) NOT NULL, 
                            JOB_SUMMARY VARCHAR(5000),
                            JOB_TITLE CHAR(100) NOT NULL,                           
                            LOCATION CHAR(100) NOT NULL);
        '''
cursor.execute(sql)

# load data jobAUS.csv
jobAUS_csv_data = csv.reader(file('jobAUS.csv'))
header=jobAUS_csv_data.next()
for row in jobAUS_csv_data:
    sql = 'INSERT INTO jobAUS VALUES(%s,%s,%s,%s);'
    cursor.execute(sql,row)
mydb.commit()
cursor.close()

# create table jobBOS
mydb = MySQLdb.connect(host='localhost',user='root', passwd='pass_word',db='GroupProject')
cursor = mydb.cursor()

sql = '''
          CREATE TABLE jobBOS (
                            COMPANY CHAR(100) NOT NULL, 
                            JOB_SUMMARY VARCHAR(5000),
                            JOB_TITLE CHAR(100) NOT NULL,                           
                            LOCATION CHAR(100) NOT NULL);
        '''
cursor.execute(sql)

# load data jobBOS.csv
jobBOS_csv_data = csv.reader(file('jobBOS.csv'))
header=jobBOS_csv_data.next()
for row in jobBOS_csv_data:
    sql = 'INSERT INTO jobBOS VALUES(%s,%s,%s,%s);'
    cursor.execute(sql,row)
mydb.commit()
cursor.close()

# create table jobDC
mydb = MySQLdb.connect(host='localhost',user='root', passwd='pass_word',db='GroupProject')
cursor = mydb.cursor()

sql = '''
          CREATE TABLE jobDC (
                            COMPANY CHAR(100) NOT NULL, 
                            JOB_SUMMARY VARCHAR(5000),
                            JOB_TITLE CHAR(100) NOT NULL,                           
                            LOCATION CHAR(100) NOT NULL);
        '''
cursor.execute(sql)

# load data jobDC.csv
jobDC_csv_data = csv.reader(file('jobDC.csv'))
header=jobDC_csv_data.next()
for row in jobDC_csv_data:
    sql = 'INSERT INTO jobDC VALUES(%s,%s,%s,%s);'
    cursor.execute(sql,row)
mydb.commit()
cursor.close()

# create table jobCHI
mydb = MySQLdb.connect(host='localhost',user='root', passwd='pass_word',db='GroupProject')
cursor = mydb.cursor()

sql = '''
          CREATE TABLE jobCHI (
                            COMPANY CHAR(100) NOT NULL, 
                            JOB_SUMMARY VARCHAR(5000),
                            JOB_TITLE CHAR(100) NOT NULL,                           
                            LOCATION CHAR(100) NOT NULL);
        '''
cursor.execute(sql)

# load data jobCHI.csv
jobCHI_csv_data = csv.reader(file('jobCHI.csv'))
header=jobCHI_csv_data.next()
for row in jobCHI_csv_data:
    sql = 'INSERT INTO jobCHI VALUES(%s,%s,%s,%s);'
    cursor.execute(sql,row)
mydb.commit()
cursor.close()
