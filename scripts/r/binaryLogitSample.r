listOfPakcages <- c("aod", "ggplot2")

newPackages <- listOfPakcages[!(listOfPakcages %in% installed.packages()[,"Package"])]

if (length(newPackages) > 0) {
  install.packages(newPackages, repos = "http://cran.rstudio.com/")
} 
# install.packages("countreg", repos="http://R-Forge.R-project.org")
library("aod")
library("ggplot2")

rm(list=ls())

# read the data
mydata <- read.csv("https://stats.idre.ucla.edu/stat/data/binary.csv")

head(mydata)
summary(mydata)

mydata$rank <- factor(mydata$rank)
mylogit <- glm(admit ~ gre + gpa + rank, data = mydata, family = "binomial")

summary(mylogit)
