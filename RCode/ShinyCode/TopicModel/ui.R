setwd("E:/R Shiny/TopicModel")
library(shiny)

shinyUI(fluidPage(
  titlePanel("Data Scientist Career Information Analysis"),
  
  sidebarLayout(
    sidebarPanel(
      helpText("Create word cloud of Data Scientist career 
                information with data from Indeed."),
      
      selectInput("city", 
                  label = "Select a city to analyze",
                  choices = c("New York, NY", "San Jose, CA", 
                              "Seattle, WA", "San Francisco, CA",
                              "Austin, TX", "Boston, MA", 
                              "Washington, DC", "Chicago, IL"),
                  selected = "New York, NY"),
      
      sliderInput("number",
                  label = "Number of words",
                  min = 1, max = 150, value = 50)
      ),
    
    mainPanel(plotOutput("WordCloud"))
  )
))
