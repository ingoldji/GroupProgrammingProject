setwd("E:/R Shiny/KeyWords")
library(shiny)
library(ggplot2)
library(wordcloud)
library(RColorBrewer)
#Package: RColorBrewer is used to generate colors used in the plot
load("KeywordData.RData")

#server.r
shinyServer(
  function(input, output) {
    
    output$FinalPlot <- renderPlot({
      Data <- switch(input$content,
                     "Software Skills"=KeywordData[[1]],
                     "Education Requirement"=KeywordData[[2]],
                     "Job Titles"=KeywordData[[3]])
      
      data_to_plot <- Data[input$city,]
      
      if (input$content=="Software Skills")
         {counts <- data.frame(sort(apply(data_to_plot,2,sum)))
          skills <- rownames(counts)
          df <- data.frame(skills,counts)
          colnames(df) <- c("skills","counts")
          rownames(df) <- NULL
       
          pal <- brewer.pal(9, "Set1")
          wordcloud(df$skills,df$counts,scale=c(5,0.2),rot.per=.15,colors=pal,random.order=FALSE,max.words=Inf)
          title(main = "Word Cloud of Software Skills Requirement",font.main= 1.2)}
            
      else {
          if (input$content=="Education Requirement")
              {counts <- data.frame(apply(data_to_plot,2,sum))
              education <- rownames(counts)
              df <- data.frame(education,counts)
              colnames(df) <- c("education","counts")
              rownames(df) <- NULL
         
              df['percent'] <- round(counts/sum(counts)*100,2)
              for (i in 1:dim(df['percent'])[1])
                  {df['percent'][i,1] <- paste(df['percent'][i,1], "%", sep="")}
         
              ggplot(df, aes(x="", y = counts, fill = education)) + 
               geom_bar(width = 1,stat="identity") +
               coord_polar(theta = "y") +
               geom_text(aes(x= rep(1.2,3),y =counts/3 + c(0, cumsum(counts)[-length(counts)]) ,label=percent),size=5,angle = 0) +
               scale_fill_brewer() +
               xlab(" ") +
               ylab("Percent") +
               ggtitle("Pie Chart of Education Requirement")}
          
          else {
               if (input$content=="Job Titles")
                  {counts <- data.frame(sort(apply(data_to_plot,2,sum)))
                  title <- factor(rownames(counts),levels=rownames(counts))
                  df <- data.frame(title,counts)
                  colnames(df) <- c("title","counts")
                  rownames(df) <- NULL
             
                  df['percent'] <- round(counts/sum(counts)*100,2)
                  for (i in 1:dim(df['percent'])[1])
                       {df['percent'][i,1] <- paste(df['percent'][i,1], "%", sep="") }
             
                  ggplot(df, aes( x= title, y = counts, fill=title)) +
                       geom_bar(stat = "identity") + 
                       xlab("Job Title") +
                       ylab("Counts") +
                       ggtitle("Bar Plot of Job Titles")}
                 }}
      })
    
})
