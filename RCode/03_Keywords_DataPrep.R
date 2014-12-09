# Prepare Data for R-shiny: Keywords Analysis

# Read the initial data
data <- read.table("byRegion.csv",header=TRUE,sep=",")

# 1. software skills
software <- data[1:8,3:14]
dimnames(software) <-list(data[,2],
                          c("R", "SAS", "SPSS","SQL","TABLEAU","PYTHON","JAVA","ACCESS",
                             "EXCEL","HADOOP","PERL","MATLAB"))
      
education <- data[1:8,15:17]
dimnames(education) <-list(data[,2],
                          c("Bachelor", "Master", "PhD"))

jobTitle <- data[1:8,18:26]
dimnames(jobTitle) <-list(data[,2],
                           c("Director", "Analyst","Scientist","Manager","Engineer","Consultant",
                             "Architect","Developer","Researcher"))

KeywordData <- list(software,education,jobTitle)
