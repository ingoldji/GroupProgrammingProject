# Step 2: Run LDA model to extract topics in the job information

# Load the term-document matrix
load("TermDocumentMatrix.RData")

library(lda)
# Define the final data structure
TopicWords <- vector("list",8)
JobTopics <- vector("list",8)

for (k in 1:8)
    {vocab <- VocabList[[k]]
     corpus <- CityList[[k]]
     
     # Number of topics
     K <- 30
     result <-lda.collapsed.gibbs.sampler(corpus,K,vocab,num.iterations=1000,alpha=0.1,eta=0.1)
     
     # Top 10 topics
     topic_rank <- rank(result$topic_sums)
     top_topics <- apply(result$topics[topic_rank>=10,],2,sum)
     
     TopicWords[[k]] <- vocab
     JobTopics[[k]] <- top_topics}

