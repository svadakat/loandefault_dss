# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
loandefaulteval1_joined_prepared = dataiku.Dataset("loandefaulteval1_joined_prepared")
loandefaulteval1_joined_prepared_df = loandefaulteval1_joined_prepared.get_dataframe()
##test

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

evalRows_df = loandefaulteval1_joined_prepared_df # For this sample code, simply copy input to output

#test
# Write recipe outputs
evalRows = dataiku.Dataset("EvalRows")
evalRows.write_with_schema(evalRows_df)