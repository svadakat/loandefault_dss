library(dataiku)

# Recipe inputs
loandefaulteval1_joined_prepared <- dkuReadDataset("loandefaulteval1_joined_prepared", samplingMethod="head", nbRows=100000)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a R dataframe or data table
testR <- loandefaulteval1_joined_prepared # For this sample code, simply copy input to output

##testing
# Recipe outputs
dkuWriteDataset(testR,"testR")
