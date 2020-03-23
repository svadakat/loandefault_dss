library(dataiku)

# Recipe inputs
lendingclub_training_prepared <- dkuReadDataset("Lendingclub_training_prepared", samplingMethod="head", nbRows=100000)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a R dataframe or data table
rtest <- lendingclub_training_prepared # For this sample code, simply copy input to output


# Recipe outputs
dkuWriteDataset(rtest,"Rtest")
