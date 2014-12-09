# -*- coding: utf-8 -*-
"""
Creating Term-Document Matrix
"""

# Step 1: Define the function to generate term-document matrix
import textmining

def term_document_matrix(text):
    '''This function is used to create term-document matrix from text.'''
    
    # Initialize class to create term-document matrix
    tdm = textmining.TermDocumentMatrix()
    
     # Add the documents
    for eachDoc in text:
        tdm.add_doc(eachDoc)
    
    return tdm

# Step 2: Import data
import pandas as pd
import MySQLdb

# Establish a connection to the database
conn = MySQLdb.connect(host='localhost',user='root', passwd='pass_word',db='GroupProject')

# Read the SQL tables
NYC = pd.read_sql("SELECT * from combinedJobs where REGION='New York, NY'", conn)
SJ = pd.read_sql("SELECT * from combinedJobs where REGION='San Jose, CA'", conn)
SEA = pd.read_sql("SELECT * from combinedJobs where REGION='Seattle, WA'", conn)
SF = pd.read_sql("SELECT * from combinedJobs where REGION='San Francisco, CA'", conn)
AUS = pd.read_sql("SELECT * from combinedJobs where REGION='Austin, TX'", conn)
BOS = pd.read_sql("SELECT * from combinedJobs where REGION='Boston, MA'", conn)
DC = pd.read_sql("SELECT * from combinedJobs where REGION='Washington, DC'", conn)
CHI = pd.read_sql("SELECT * from combinedJobs where REGION='Chicago, IL'", conn)

# Step 3: Create term-document matrix
text = NYC['JOB_BRIEF']
NYCmatrix = term_document_matrix(text)
# Include words which appear in more than 5 jobs
NYCmatrix.write_csv("NYCmatrix.csv",cutoff=5)

text = SJ['JOB_BRIEF']
SJmatrix = term_document_matrix(text)
SJmatrix.write_csv("SJmatrix.csv",cutoff=5)

text = SEA['JOB_BRIEF']
SEAmatrix = term_document_matrix(text)
SEAmatrix.write_csv("SEAmatrix.csv",cutoff=5)

text = SF['JOB_BRIEF']
SFmatrix = term_document_matrix(text)
SFmatrix.write_csv("SFmatrix.csv",cutoff=5)

text = AUS['JOB_BRIEF']
AUSmatrix = term_document_matrix(text)
AUSmatrix.write_csv("AUSmatrix.csv",cutoff=5)

text = BOS['JOB_BRIEF']
BOSmatrix = term_document_matrix(text)
BOSmatrix.write_csv("BOSmatrix.csv",cutoff=5)

text = DC['JOB_BRIEF']
DCmatrix = term_document_matrix(text)
DCmatrix.write_csv("DCmatrix.csv",cutoff=5)

text = CHI['JOB_BRIEF']
CHImatrix = term_document_matrix(text)
CHImatrix.write_csv("CHImatrix.csv",cutoff=5)

