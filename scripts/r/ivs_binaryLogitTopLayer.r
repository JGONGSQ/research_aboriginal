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
mydata <- read.csv("/Users/daddyspro/Desktop/GitHub/research_aboriginal/resources/2012/IVS_2012_LOGIT_ALL_PROCESSED.csv")

head(mydata)
summary(mydata)

# category variables included in the logit model
mydata$GENDER <- factor(mydata$GENDER)
mydata$AGEGROUP <- factor(mydata$AGEGROUP)
mydata$TRIP_PURPOSE <- factor(mydata$TRIP_PURPOSE)
mydata$PARTYPE <- factor(mydata$PARTYPE)
mydata$MARITAL <- factor(mydata$MARITAL)
mydata$INT_BOOKING <- factor(mydata$INT_BOOKING)
mydata$PARENT <- factor(mydata$PARENT)
mydata$CUSTOMS <- factor(mydata$CUSTOMS)
mydata$COUNTRY <- factor(mydata$COUNTRY)
mydata$AIRLINE <- factor(mydata$AIRLINE)

mylogit <- glm(PARTICIPATE_IND ~ GENDER + AGEGROUP + TRIP_PURPOSE + 
                 PARTYPE + MARITAL + INT_BOOKING + PARENT + CUSTOMS + 
                 COUNTRY + AIRLINE, data = mydata, family = "binomial")

summary(mylogit)
