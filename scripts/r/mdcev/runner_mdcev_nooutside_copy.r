list_of_packages = c("utils","foreign","pastecs","mlogit","graphics","VGAM","ZeligChoice","aod","plotrix", "maxLik", "miscTools")

new_packages <- list_of_packages[!(list_of_packages %in% installed.packages()[,"Package"])]
rm(list=ls())
print("-----> Start Loading Packages <-----")
# source("scripts/r/mdcev/mdcev_nooutside.r");
source("/Users/daddyspro/Desktop/GitHub/research_aboriginal/scripts/r/mdcev/mdcev_nooutside.r");
if(length(new_packages) > 0) {
  install.packages(new_packages, repos="http://cran.rstudio.com/")
}

args <- commandArgs(trailingOnly = TRUE)


if (length(args)==0) {
    stop("At least one argument must be supplied", call.=FALSE)
}

# input_file_path = args[1]
# number_of_alternatives = strtoi(args[2])
# case_config = strtoi(args[3])
# utility_variables = args[4]
# city_variables = args[5]
# output_results_path = args[6]
# alternative_variables_str = args[7]

input_file_path = "/Users/daddyspro/Desktop/GitHub/research_aboriginal/resources/2012/IVS_2012_MDCEV_ALL_PROCESSED25_3_Sep.csv"
number_of_alternatives = 15
case_config = 4
# utility_variables = args[4]
city_variables = "NSW_SYD,NSW_NON_SYD,VIC_MEL,VIC_NON_MEL,QLD_BNE,QLD_NON_BNE,SA_ADL,SA_NON_ADL,WA_PER,WA_NON_PER,TAS_HBA,TAS_NON_HBA,NT_DRW,NT_NON_DRW,ACT_CAN"
output_results_path = "/Users/daddyspro/Desktop/GitHub/research_aboriginal/results/mdcev/estimation_4_TEMP.txt"
alternative_variables_str = "GENDER_MALE,GENDER_FEMALE"

# alternative_variables <- list();

# for (i in 1:number_of_alternatives){
#  if (i == 1){
#    print("first alternative does not get any variables") # Base alternative
#  }
#  else {
#    alternative_variables[[i]] = list_creator(strsplit(alternative_variables_str, ",") )
#  }
#}

alternative_variables_list = list_creator(strsplit(alternative_variables_str, ",") )

print("### This is the number of alternaives", number_of_alternatives)

print("### This is the case config")
print(case_config)

print("###### This is the utility variables")
# variable_list = list_creator(strsplit(utility_variables, ",") )
# print(variable_list)

print("### This is the city variables")
print(city_variables)

print("-----> Reading Table <-----")
Data <<- read.table(input_file_path, header=T, sep=",");

table_headers = names(Data)

config <- case_config;     # Utility specification configuration, possible values: 1,4,7
alp0to1 <- 1;    # 1 if you want the Alpha values to be constrained between 0 and 1, 0 otherwise
                 # putting _alp0to1 = 1 is recommended practice and can provide estimation stability
price <- 0;      # 1 if there is price variation across goods, 0 otherwise
nc <- number_of_alternatives;         # Number of alternatives (in the universal choice set) including outside goods
# po <- match("id", table_headers, 0);         # Index number of ID column in input data
po <- 1;

ivuno <- "uno"
ivsero <-"sero"
wtind <<- "uno"

maxlikmethod1 <- "BHHH"; # Method of maximum likelihood for initial estimation ("BHHH" or "BFGS") 
maxlikmethod2 <- "BFGS"; # Method of maximum likelihood for final estimation ("BHHH" or "BFGS") 

# Position of the DEPENDENT variables (i.e., the consumption quantities for each alternative - NOT consumption expenditures for each alternative).
# Number of labels = number of alternatives. 
def <- list_creator(strsplit(city_variables, ",") )
# Positions of PRICE variables
# Provide labels of price variables (one label in each double-quote). Number of labels = number of alternatives.
# Provide all UNO variables if there is no price variation 
fp_list = c()
for (i in 1:nc){
  fp_list = c(ivuno, fp_list)
}
fp <- fp_list

# In the following specification, ivm1, ivm2, ivm3 contain independent variable specifications (on right hand side) for baseline utility (PSI) 
# for alternatives 1, 2, and 3;
# Add a row for ivm4 below if there is a 4th alternative, another addiitonal row for ivm5 if there is a 5th alternative, ...  
# (number of rows = number of alternatives);
# Number of columns = Number of variables including alternative specific constants; consider first alternative as base
ivmt <- list();
# ivmt[[1]] <- c("");   # Base alternative
# ivmt[[2]] <- c("uno", alternative_variable_2);
# ivmt[[3]] <- c("uno", alternative_variable_3);
# ivmt[[4]] <- c("uno", alternative_variable_4);
# ivmt[[5]] <- c("uno", alternative_variable_5);
# ivmt[[6]] <- c("uno", alternative_variable_6);
# ivmt[[7]] <- c("uno", alternative_variable_7);
# ivmt[[8]] <- c("uno", alternative_variable_8);

for (i in 1:nc){
  if (i == 1){
    ivmt[[i]] <- c(""); # Base alternative
  }
  else {
    ivmt[[i]] <- c("uno", alternative_variables_list);
  }
}
print("This is the ivmt")
print(ivmt)

# In the following specification, ivdts[[1]], ivdts[[2]], ivdts[[3]] contain input data specifications (on right hand side) for satiation parameters (Alphas) 
# for alternatives 1, 2, and 3;
# Add a row below for ivd4 if there is a 4th alternative, another additional row for ivd5 if there is a 5th alternative,.... 
# (number of rows = number of alternatives);
# Number of columns = Number of alternatives; Note that you can also add individual-specific variables below, so that satiation varies across individuals; 
# However, you will then have to translate outputs to compute actual alpha parameters; 
# This code is written to provide you with the alpha parameters directly for the case when there is no variation in alpha across individuals
ivdts <- list();
# ivdts[[1]] <- c("uno");
# ivdts[[2]] <- c("uno");
# ivdts[[3]] <- c("uno");
# ivdts[[4]] <- c("uno");
# ivdts[[5]] <- c("uno");
# ivdts[[6]] <- c("uno");

for (i in 1:nc){
  ivdts[[i]] <- c("uno");
}



# In the following specification, ivgts[[1]], ivgts[[2]], ivgts[[3]] contain input data specifications (on the right hand side) for translation parameters (Gammas) 
# for alternatives 1, 2, and 3
# Add a row for ivgts[[4]] if there is a 4th alternative another additional row for ivgts[[5]] if there is a 5th alternative,.... 
# (number of rows = number of alternatives) Number of columns = Number of alternatives; 
# Note that you can also add individual-specific variables below, so that gamma varies across individuals; 
# However, you will then have to translate outputs to compute actual gamma parameters; 
# This code is written to provide you with the gamma parameters directly for the case when there is no variation in gamma across individuals 
ivgts <- list();
# ivgts[[1]] <- c("uno");
# ivgts[[2]] <- c("uno");
# ivgts[[3]] <- c("uno");
# ivgts[[4]] <- c("uno");
# ivgts[[5]] <- c("uno");
# ivgts[[6]] <- c("uno");

for (i in 1:nc){
  ivgts[[i]] <- c("uno");
}


# Add variable names for translation and satiation variables
# The number of names for both translation and satiation should be equal to the number of alternatives
alpha_name_list = c()
for (i in 1:nc){
  variable_name = paste('D', i, sep = "")
  alpha_name_list = c(alpha_name_list, variable_name)
}
alpha_names <- alpha_name_list

gamma_name_list = c()
for (i in 1:nc){
  variable_name = paste('G', i, sep = "")
  gamma_name_list = c(gamma_name_list, variable_name)
}
gamma_names <- gamma_name_list

########################################################################################################
#  Do Not Modify Next Three Lines
########################################################################################################
arg_inds <- list(config, alp0to1, price, nc, po); 
arg_vars <- list(ivuno, ivsero, wtind, maxlikmethod1, maxlikmethod2);           


result <- mdcev_nooutgood(Data, arg_inds, arg_vars, def, fp, ivmt, ivdts, ivgts, alpha_names, gamma_names);
########################################################################################################
sink(output_results_path)
summary(result); # Show results from the MDCEV model with no outside good
sink()
# write.table(result$estimate,file=output_results_path, sep=',')


