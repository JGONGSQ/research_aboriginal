listOfPakcages <- c("foreign", "ggplot2", "MASS")

newPackages <- listOfPakcages[!(listOfPakcages %in% installed.packages()[,"Package"])]

if (length(newPackages) > 0) {
  install.packages(newPackages, repos = "http://cran.rstudio.com/")
} 
# install.packages("countreg", repos="http://R-Forge.R-project.org")
library("foreign")
library("ggplot2")
library("MASS")

rm(list=ls())

# read the data
# data <- read.table("/Users/daddyspro/Desktop/GitHub/research_aboriginal/resources/2012/IVS_2012_PROCESSED.csv", header = T, sep = ",")
data <- read.table("/Users/daddyspro/Desktop/GitHub/research_aboriginal/resources/2012/IVS_2012_ALL_PROCESSED.csv", header = T, sep = ",")
# qplot(data$Duration, geom="histogram", binwidth = 1)
outfile <- "/Users/daddyspro/Desktop/GitHub/research_aboriginal/results/ivs_negative_binomial.txt"
# NUMSTOP + NUMVISIT + RANDOMSTOP + PARTYPE
# estimate the model with Negative Binomial
# nbm <- glm.nb(AUSNITES ~ GENDER + MARITAL + AGEGROUP + NUMSTOP +
 #               PARTYPE + TRIP_PURPOSE + CUSTOMS, data=data)

nbm <- glm.nb(AUSNITES ~ GENDER + MARITAL + AGEGROUP + NUMSTOP + TRIP_PURPOSE + CUSTOMS + COUNTRY, data=data)

summary(nbm)

# sink(outfile,append=FALSE)
# summary(nbm)
# sink()
# simulate the results
#simulateResults <- rnegbin(fitted(nbm), theta=nbm$theta)
print(nbm$theta)
simulateResults <- rnegbin(fitted(nbm), theta=nbm$theta)
simulateResults_with_offset <- simulateResults + 1
# predicte result
# predictResult <- predict.glm(nbm, newdata = data, type = "response")
# predictResult <- predict(nbm, newdata = data)

# write the results to the csv file
# outputFile = "/Users/daddyspro/Desktop/GitHub/research_aboriginal/results/nb_ivs_coefficients.csv"
# write.csv(summary.glm(nbm)$coefficients, outputFile)

# initial the data with data frame
durationInput <- data.frame(Duration = data$AUSNITES)
# durationOutput <- data.frame(Duration = predictResult)
# durationOutput <- data.frame(Duration = simulateResults)
durationOutput <- data.frame(Duration = simulateResults_with_offset)

# define the data type
durationInput$type <- 'Observed'
durationOutput$type <- 'Simulated'

# combine the values
durationValues <- rbind(durationInput, durationOutput)

# plot the compared results
ggplot(durationValues, aes(Duration, fill = type), binwidth = 2) + geom_histogram(alpha = 0.5, position = 'identity', binwidth = 2) + xlim(0, 365)


