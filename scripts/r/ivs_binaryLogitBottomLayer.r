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
mydata <- read.csv("/Users/daddyspro/Desktop/GitHub/research_aboriginal/resources/2012/IVS_2012_BOT_LOGIT_ALL_PROCESSED.csv")

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

# mylogit <- glm(PARTICIPATE_IND ~ GENDER + AGEGROUP + TRIP_PURPOSE + 
#                 PARTYPE + MARITAL + INT_BOOKING + PARENT + CUSTOMS + 
#                 COUNTRY + AIRLINE + SYD + NONSYD + MEL + NONMEL + BNE + NONBNE + 
#                 ADL + NONADL + PER + NONPER + HBA + NONHBA + DRW + NONDRW + CAN, data = mydata, family = "binomial")
mydata$SYD_B <- factor(mydata$SYD_B)
mydata$NONSYD_B <- factor(mydata$NONSYD_B)
mydata$MEL_B <- factor(mydata$MEL_B)
mydata$NONMEL_B <- factor(mydata$NONMEL_B)
mydata$BNE_B <- factor(mydata$BNE_B)
mydata$NONBNE_B <- factor(mydata$NONBNE_B)
mydata$ADL_B <- factor(mydata$ADL_B)
mydata$NONADL_B <- factor(mydata$NONADL_B)
mydata$PER_B <- factor(mydata$PER_B)
mydata$NONPER_B <- factor(mydata$NONPER_B)
mydata$HBA_B <- factor(mydata$HBA_B)
mydata$NONHBA_B <- factor(mydata$NONHBA_B)
mydata$DRW_B <- factor(mydata$DRW_B)
mydata$NONDRW_B <- factor(mydata$NONDRW_B)
mydata$CAN_B <- factor(mydata$CAN_B)

mylogit <- glm(PARTICIPATE_IND ~ GENDER + AGEGROUP + TRIP_PURPOSE + 
                 PARTYPE + MARITAL + INT_BOOKING + PARENT + CUSTOMS + 
                 COUNTRY + AIRLINE + SYD_B + NONSYD_B + MEL_B + NONMEL_B + BNE_B + NONBNE_B + 
                 ADL_B + NONADL_B + PER_B + NONPER_B + HBA_B + NONHBA_B + DRW_B + NONDRW_B + CAN_B, data = mydata, family = "binomial")

summary(mylogit)
