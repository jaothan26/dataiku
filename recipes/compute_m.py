# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
clean_pos = dataiku.Dataset("clean_pos")
clean_pos_df = clean_pos.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

m_df = clean_pos_df # For this sample code, simply copy input to output


# Write recipe outputs
m = dataiku.Dataset("m")
m.write_with_schema(m_df)
