setwd("E:/R Shiny/KeyWords")
library(shiny)

shinyUI(fluidPage(
  titlePanel("Data Scientist Career Information Key Word Analysis"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Analyze the keywords of Data Scientist 
               career information with data from Indeed."),
            
      radioButtons("city", 
                   label = "Select cities to analyze",
                    choices = c("New York, NY" ,"San Jose, CA" , 
                                "Seattle, WA" , "San Francisco, CA",
                                 "Austin, TX", "Boston, MA", 
                                 "Washington, DC", "Chicago, IL"),
                                  selected = "New York, NY"),
      
      selectInput("content", 
                  label = "Select a type of information to analyze",
                  choices = c("Software Skills","Education Requirement","Job Titles"),
                  selected = "Software Skills")
      
     ),
    
    mainPanel(plotOutput("FinalPlot"))
  )
))
