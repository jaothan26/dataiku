# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
from dataiku import Dataset, Folder
import pandas as pd
import json
import requests
import base64
from pandas.io.json import json_normalize

# Read recipe inputs
#data15_17_joined_author_data = dataiku.Dataset("data15_17_joined_author_data")
#data15_17_joined_author_data_df = data15_17_joined_author_data.get_dataframe()

# Create Pandas dataframe
counter = 1
freshdesk_companies_final = pd.DataFrame()
tmp = True
# Pull data using Freshdesk API using companies endpoint
while tmp:
    FRESHDESK_ENDPOINT = "https://newaccount160716329665.freshdesk.com" # check if you have configured https, modify accordingly
    FRESHDESK_KEY = "OgEeDb5wzXsh9Ryt8DMM"
    r = requests.get(FRESHDESK_ENDPOINT + '/api/v2/companies?page=' + str(counter) + '&per_page=100',auth=(FRESHDESK_KEY, "X"))
    if r.content == '[]':
        break
    freshdesk_companies = pd.DataFrame(json_normalize(json.loads(r.content)))
    freshdesk_companies_final = freshdesk_companies_final.append(freshdesk_companies)
    print (counter)
    counter += 1

# Write resulting dataframe into the output dataset
freshdesk_companies_list = dataiku.Dataset("Freshdesk_companies_list")
freshdesk_companies_list.write_with_schema(freshdesk_companies_final)