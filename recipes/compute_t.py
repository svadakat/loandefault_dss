# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
lendingclub_training = dataiku.Dataset("Lendingclub_training")
lendingclub_training_df = lendingclub_training.get_dataframe()
evalTestRemainingCols = dataiku.Dataset("EvalTestRemainingCols")
evalTestRemainingCols_df = evalTestRemainingCols.get_dataframe()
dataload_TEMP1_loandefaulteval1 = dataiku.Dataset("DATALOAD_TEMP1_loandefaulteval1")
dataload_TEMP1_loandefaulteval1_df = dataload_TEMP1_loandefaulteval1.get_dataframe()


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

t_df = ... # Compute a Pandas dataframe to write into t


# Write recipe outputs
t = dataiku.Dataset("t")
t.write_with_schema(t_df)
