import numpy as np
import pandas as pd
import json
import requests
import os
from datetime  import datetime

def top_protocols(top=10, bottom=0):
    """the below funtion uses the defilama api to pull a list of the top protocols 
    by total value locked as reported on defilama. It also gives a break out of the TVL by chain.
    By default the funtion returns the top 10 protocols."""
    assert top > bottom, "your 'top' variable must be greater than your 'bottom' variable"
    
    r = requests.get('https://api.llama.fi/protocols') #Make request for all protocols
    json = r.json() # Extract json
    lst = np.arange(0,len(json)).tolist() #make a list to itterate though all protocols for values

    # Get a list of all of the protocol names
    protocol_names = []
    for i in lst:
        protocol_names.append(json[i]['name'])
    protocol_names = pd.DataFrame(protocol_names)

    #get a list of all protocol tvls
    chainstvl = []
    for i in lst:
        chainstvl.append(json[i]['chainTvls'])
    chainstvl = pd.DataFrame(chainstvl)

    #make a dataframe for all protocols and their tvls
    platform_tvl = pd.concat([protocol_names,chainstvl], axis=1)
    platform_tvl = platform_tvl.rename(columns={platform_tvl.columns[0]:'protocol_name'})
    platform_tvl['total'] = platform_tvl.sum(axis=1)
    platform_tvl = platform_tvl.sort_values(by='total',ascending=False)

    top_protocols = platform_tvl[bottom:top]
    top_protocols = top_protocols.replace(np.nan,0)
    return(top_protocols)

#exclude: 'Binance CEX','Polygon Bridge & Staking,
#I need to add an exception for aave v1,v2,v3 and convert it to just aave.

