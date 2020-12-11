# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
tweet_data_joined_sql = dataiku.Dataset("sentiment_prepared_neo4j")
tweet_data_joined_sql_df = tweet_data_joined_sql.get_dataframe()
tweet_data_joined_sql_df.head()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
from textblob import TextBlob

example = "#!!"

print(TextBlob(example).sentiment)

print(TextBlob(example).sentiment.polarity)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df = tweet_data_joined_sql_df.head(5)

def sentiment(arg):
    try:
        return TextBlob(arg).sentiment.polarity
    except:
        return

df["sentiment"]= df["sent_bis"].apply(sentiment)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
tweet_data_joined_sql_df["sentiment"]=tweet_data_joined_sql_df["sent_bis].apply(sentiment)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

tweet_sentiment_df = tweet_data_joined_sql_df # For this sample code, simply copy input to output

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
tweet_sentiment = dataiku.Dataset("sent_bis")
tweet_sentiment.write_with_schema(tweet_sentiment_df)