setwd("E:/R Shiny/TopicModel")
library(shiny)
library(wordcloud)
library(RColorBrewer)
load("JobData.RData")

#server.r
shinyServer(
  function(input, output) {
    
    output$WordCloud <- renderPlot({
      vocab <- switch(input$city, 
                       "New York, NY" = TopicWords[[1]],
                       "San Jose, CA" = TopicWords[[2]],
                       "Seattle, WA" = TopicWords[[3]],
                       "San Francisco, CA" = TopicWords[[4]],
                       "Austin, TX" = TopicWords[[5]],
                       "Boston, MA" = TopicWords[[6]],
                       "Washington, DC" = TopicWords[[7]],
                       "Chicago, IL" = TopicWords[[8]])
      
      topics <- switch(input$city, 
                     "New York, NY" = JobTopics[[1]],
                     "San Jose, CA" = JobTopics[[2]],
                     "Seattle, WA" = JobTopics[[3]],
                     "San Francisco, CA" = JobTopics[[4]],
                     "Austin, TX" = JobTopics[[5]],
                     "Boston, MA" = JobTopics[[6]],
                     "Washington, DC" = JobTopics[[7]],
                     "Chicago, IL" = JobTopics[[8]])
      
      pal <- brewer.pal(9, "Set1")
      wordcloud(vocab,topics,max.words=input$number,scale=c(5,0.3),rot.per=.15,random.order=FALSE,colors=pal)
      })
    
  }
)
