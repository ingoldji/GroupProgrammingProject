# -*- coding: utf-8 -*-
"""
Keywords Analysis
"""
###In this file, we flag software skills, job titles and education levels and create title- and education level-focused summary tables
import pandas as pd
combinedJobs = pd.DataFrame.from_csv("combinedJobs.csv", header=0, index_col=None)
combinedJobs = combinedJobs[["COMPANY","JOB_TITLE","REGION","JOB_BRIEF"]]

#adding software skills flags
combinedJobs['f_R'] = combinedJobs.JOB_BRIEF.str.contains(" r ")
combinedJobs['f_SAS'] = combinedJobs.JOB_BRIEF.str.contains(" sas ")
combinedJobs['f_SPSS'] = combinedJobs.JOB_BRIEF.str.contains(" spss ")
combinedJobs['f_SQL'] = combinedJobs.JOB_BRIEF.str.contains("sql")
combinedJobs['f_TABLEAU'] = combinedJobs.JOB_BRIEF.str.contains(" tableau ")
combinedJobs['f_PYTHON'] = combinedJobs.JOB_BRIEF.str.contains(" python ")
combinedJobs['f_JAVA'] = combinedJobs.JOB_BRIEF.str.contains(" java ")
combinedJobs['f_ACCESS'] = combinedJobs.JOB_BRIEF.str.contains(" access ")
combinedJobs['f_EXCEL'] = combinedJobs.JOB_BRIEF.str.contains(" excel ")
combinedJobs['f_HADOOP'] = combinedJobs.JOB_BRIEF.str.contains(" hadoop ")
combinedJobs['f_PERL'] = combinedJobs.JOB_BRIEF.str.contains(" perl ")
combinedJobs['f_MATLAB'] = combinedJobs.JOB_BRIEF.str.contains(" matlab ")

#adding education level flags
combinedJobs['f_MASTERS'] = combinedJobs.JOB_BRIEF.str.contains(" ma ") | combinedJobs.JOB_BRIEF.str.contains("masters") | combinedJobs.JOB_BRIEF.str.contains("mba") | combinedJobs.JOB_BRIEF.str.contains(" ms ") | combinedJobs.JOB_BRIEF.str.contains(" master science") | combinedJobs.JOB_BRIEF.str.contains(" master arts") |combinedJobs.JOB_BRIEF.str.contains(" master degree") | combinedJobs.JOB_BRIEF.str.contains(" graduate degree") | combinedJobs.JOB_BRIEF.str.contains("advanced degree") | combinedJobs.JOB_BRIEF.str.contains("mams") | combinedJobs.JOB_BRIEF.str.contains("msma")
combinedJobs['f_BACHELORS'] = combinedJobs.JOB_BRIEF.str.contains(" ba ") | combinedJobs.JOB_BRIEF.str.contains("bachelor") | combinedJobs.JOB_BRIEF.str.contains(" bs ") | combinedJobs.JOB_BRIEF.str.contains("undergraduate") | combinedJobs.JOB_BRIEF.str.contains("babs") | combinedJobs.JOB_BRIEF.str.contains("bsba")
combinedJobs['f_PHD'] = combinedJobs.JOB_BRIEF.str.contains("phd") | combinedJobs.JOB_BRIEF.str.contains(" doctor ") | combinedJobs.JOB_BRIEF.str.contains("doctorate")

#replacing education flags with flags for highest education level mentioned
combinedJobs['h_ALL'] = combinedJobs.apply(lambda x:'%s%s%s' % (x['f_BACHELORS'],x['f_MASTERS'],x['f_PHD']),axis=1)
combinedJobs['h_ALL'] = combinedJobs.h_ALL.astype(str)

cond1 = combinedJobs.h_ALL == 'TrueFalseFalse'
combinedJobs.f_BACHELORS[cond1] = combinedJobs.h_ALL[cond1]
combinedJobs['f_BACHELORS'] = combinedJobs.f_BACHELORS.astype(str)
combinedJobs['f_BACHELORS'] = combinedJobs['f_BACHELORS'].replace('True', False)
combinedJobs['f_BACHELORS'] = combinedJobs['f_BACHELORS'].replace('False', False)
combinedJobs['f_BACHELORS'] = combinedJobs['f_BACHELORS'].replace('TrueFalseFalse', True)

cond2 = combinedJobs.h_ALL == 'TrueTrueFalse' 
cond3 = combinedJobs.h_ALL == 'FalseTrueFalse'
combinedJobs.f_MASTERS[cond2] = combinedJobs.h_ALL[cond2]
combinedJobs.f_MASTERS[cond3] = combinedJobs.h_ALL[cond3]
combinedJobs['f_MASTERS'] = combinedJobs.f_MASTERS.astype(str)
combinedJobs['f_MASTERS'] = combinedJobs['f_MASTERS'].replace('True', False)
combinedJobs['f_MASTERS'] = combinedJobs['f_MASTERS'].replace('False', False)
combinedJobs['f_MASTERS'] = combinedJobs['f_MASTERS'].replace('TrueTrueFalse', True)
combinedJobs['f_MASTERS'] = combinedJobs['f_MASTERS'].replace('FalseTrueFalse', True)


#adding job title flags
combinedJobs['f_DIRECTOR'] = combinedJobs.JOB_TITLE.str.contains("Director") | combinedJobs.JOB_TITLE.str.contains("director") | combinedJobs.JOB_TITLE.str.contains("DIRECTOR")
combinedJobs['f_ANALYT'] = combinedJobs.JOB_TITLE.str.contains("Analyst") | combinedJobs.JOB_TITLE.str.contains("analyst") | combinedJobs.JOB_TITLE.str.contains("ANALYST")
combinedJobs['f_SCIENTIST'] = combinedJobs.JOB_TITLE.str.contains("Science") | combinedJobs.JOB_TITLE.str.contains("Scientist") | combinedJobs.JOB_TITLE.str.contains("scientist") | combinedJobs.JOB_TITLE.str.contains("SCIENTIST") | combinedJobs.JOB_TITLE.str.contains("science") | combinedJobs.JOB_TITLE.str.contains("SCIENCE")
combinedJobs['f_MANAGER'] = combinedJobs.JOB_TITLE.str.contains("Manager") | combinedJobs.JOB_TITLE.str.contains("manager") | combinedJobs.JOB_TITLE.str.contains("MANAGER")
combinedJobs['f_ENGINEER'] = combinedJobs.JOB_TITLE.str.contains("Engineer") | combinedJobs.JOB_TITLE.str.contains("engineer") | combinedJobs.JOB_TITLE.str.contains("ENGINEER")
combinedJobs['f_CONSULTANT'] = combinedJobs.JOB_TITLE.str.contains("Consultant") | combinedJobs.JOB_TITLE.str.contains("consultant") | combinedJobs.JOB_TITLE.str.contains("CONSULTANT")
combinedJobs['f_ARCHITECT'] = combinedJobs.JOB_TITLE.str.contains("Architect") | combinedJobs.JOB_TITLE.str.contains("architect") | combinedJobs.JOB_TITLE.str.contains("ARCHITECT")
combinedJobs['f_DEVELOPER'] = combinedJobs.JOB_TITLE.str.contains("Developer") | combinedJobs.JOB_TITLE.str.contains("developer") | combinedJobs.JOB_TITLE.str.contains("DEVELOPER")
combinedJobs['f_RESEARCHER'] = combinedJobs.JOB_TITLE.str.contains("Research") | combinedJobs.JOB_TITLE.str.contains("Researcher") | combinedJobs.JOB_TITLE.str.contains("researcher") | combinedJobs.JOB_TITLE.str.contains("research") | combinedJobs.JOB_TITLE.str.contains("RESEARCHER") | combinedJobs.JOB_TITLE.str.contains("RESEARCH")

#exporting job title-focused table to csv
combinedJobs.to_csv('combinedJobs.csv')

##Making table with count of keywords by region for regional analysis
byregion = combinedJobs.groupby('REGION', as_index=False).sum()
byregion.to_csv('byRegion.csv')

##Making table of counts of keywords and percentages by job title
import numpy as np        
focus_c = ['f_DIRECTOR', 'f_ANALYT', 'f_SCIENTIST', 'f_MANAGER', 'f_ENGINEER', 'f_CONSULTANT', 'f_ARCHITECT', 'f_DEVELOPER', 'f_RESEARCHER']
focus = pd.DataFrame(index=focus_c)

def count(a,x,y,z,q):
    a = pd.pivot_table(combinedJobs, rows=[x], aggfunc=np.sum)
    a = a.transpose()
    a.columns = [y, z]
    a[q] = a[z]/(a[z] + a[y])
    a[z] = a[z].astype(int)
    a[y] = a[y].astype(int)
    global focus 
    focus = focus.join(a, how='left')

#for education
count('masters_table', 'f_MASTERS', 'mas_no', 'mas_yes', 'mas_perc')
count('bachelors_table', 'f_BACHELORS', 'bac_no', 'bac_yes', 'bac_perc')
count('phd_table', 'f_PHD', 'phd_no', 'phd_yes', 'phd_perc')

#for skills
count('access_table', 'f_ACCESS', 'acc_no', 'acc_yes', 'acc_perc')
count('excel_table', 'f_EXCEL', 'exc_no', 'exc_yes', 'exc_perc')
count('hadoop_table', 'f_HADOOP', 'had_no', 'had_yes', 'had_perc')
count('java_table', 'f_JAVA', 'jav_no', 'jav_yes', 'jav_perc')
count('matlab_table', 'f_MATLAB', 'mat_no', 'mat_yes', 'mat_perc')
count('perl_table', 'f_PERL', 'per_no', 'per_yes', 'per_perc')
count('python_table', 'f_PYTHON', 'pyt_no', 'pyt_yes', 'pyt_perc')
count('r_table', 'f_R', 'r_no', 'r_yes', 'r_perc')
count('sas_table', 'f_SAS', 'sas_no', 'sas_yes', 'sas_perc')
count('spss_table', 'f_SPSS', 'sps_no', 'sps_yes', 'sps_perc')
count('sql_table', 'f_SQL', 'sql_no', 'sql_yes', 'sql_perc')
count('tableau_table', 'f_TABLEAU', 'tab_no', 'tab_yes', 'tab_perc')

focus.to_csv('byJobTitle.csv')

##Making table of counts of keywords and percentages by education       
focus_c = ['f_MASTERS', 'f_BACHELORS', 'f_PHD']
focus = pd.DataFrame(index=focus_c)

#for title
count('manager_table', 'f_MANAGER', 'man_no', 'man_yes', 'man_perc')
count('engineer_table', 'f_ENGINEER', 'eng_no', 'eng_yes', 'eng_perc')
count('consultant_table', 'f_CONSULTANT', 'con_no', 'con_yes', 'con_perc')
count('architect_table', 'f_ARCHITECT', 'arc_no', 'arc_yes', 'arc_perc')
count('developer_table', 'f_DEVELOPER', 'dev_no', 'dev_yes', 'dev_perc')
count('researcher_table', 'f_RESEARCHER', 'res_no', 'res_yes', 'res_perc')

#for skills
count('access_table', 'f_ACCESS', 'acc_no', 'acc_yes', 'acc_perc')
count('excel_table', 'f_EXCEL', 'exc_no', 'exc_yes', 'exc_perc')
count('hadoop_table', 'f_HADOOP', 'had_no', 'had_yes', 'had_perc')
count('java_table', 'f_JAVA', 'jav_no', 'jav_yes', 'jav_perc')
count('matlab_table', 'f_MATLAB', 'mat_no', 'mat_yes', 'mat_perc')
count('perl_table', 'f_PERL', 'per_no', 'per_yes', 'per_perc')
count('python_table', 'f_PYTHON', 'pyt_no', 'pyt_yes', 'pyt_perc')
count('r_table', 'f_R', 'r_no', 'r_yes', 'r_perc')
count('sas_table', 'f_SAS', 'sas_no', 'sas_yes', 'sas_perc')
count('spss_table', 'f_SPSS', 'sps_no', 'sps_yes', 'sps_perc')
count('sql_table', 'f_SQL', 'sql_no', 'sql_yes', 'sql_perc')
count('tableau_table', 'f_TABLEAU', 'tab_no', 'tab_yes', 'tab_perc')

focus.to_csv('byEducation.csv')
