# Step 1: Load the term-document matrix & Prepare the data for LDA model
# Read data
NYCmatrix <- read.table("NYCmatrix.csv",header=TRUE,sep=",")
SJmatrix <- read.table("SJmatrix.csv",header=TRUE,sep=",")
SEAmatrix <- read.table("SEAmatrix.csv",header=TRUE,sep=",")
SFmatrix <- read.table("SFmatrix.csv",header=TRUE,sep=",")
AUSmatrix <- read.table("AUSmatrix.csv",header=TRUE,sep=",")
BOSmatrix <- read.table("BOSmatrix.csv",header=TRUE,sep=",")
DCmatrix <- read.table("DCmatrix.csv",header=TRUE,sep=",")
CHImatrix <- read.table("CHImatrix.csv",header=TRUE,sep=",")

TDMatrix <- list (NYCmatrix,SJmatrix,SEAmatrix,SFmatrix,AUSmatrix,BOSmatrix,DCmatrix,CHImatrix)

VocabList <- vector("list",8)
CityList  <- vector("list",8)

for (k in 1:8)
    {citymatrix <- TDMatrix[[k]]
     
     #1. Update VocabList
     vocab <- colnames(citymatrix)
     VocabList[[k]] <- vocab
     
     #2. Update CityList
     # number of jobs
     job_num <- dim(citymatrix)[1]
     # number of words
     vocab_length <- dim(citymatrix)[2]
     
     FreqData <- vector("list",job_num)
     for (i in 1:job_num)
         {for (j in 1:vocab_length)
              {if (citymatrix[i,j]!=0)
                {word_num <- as.integer(j-1)
                 word_freq <- as.integer(citymatrix[i,j])
                 data <- rbind(word_num,word_freq)
                 FreqData[[i]]= cbind(FreqData[[i]],data)}
              }
         }
     CityList[[k]] <- FreqData
}
