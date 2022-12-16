import numpy as np
import pandas as pd
import json
import requests
import os
from datetime  import datetime


def protocol_tvl_ts(protocol):
    """For a specific protocol names, this funtion will ouput a time series 
    dataset that provides the entire avalible the TVL from DefiLlama."""
    if (protocol == 'AAVE V2') or (protocol == 'AAVE V3'):
        print("AAVE V2 and V3 are aggregated in AAVE. Replace you protocol name with 'AAVE.'")
    elif(protocol == 'Binance CEX') or protocol == 'Binance':
        print("Binance is not avalible in the api endpoint 'https://api.llama.fi/protocol.'")
    else:
        url = 'https://api.llama.fi/protocol/{}'.format(protocol)
        r = requests.get(url)
        json = r.json()
        tvl = pd.DataFrame()
        chains = list(json['chainTvls'].keys())
        for i in chains:
            test = list(json['chainTvls'][i]['tvl'])
            test = pd.DataFrame(test)
            test['chains'] = str(i)
            tvl = pd.concat([test,tvl],ignore_index = True)

        tvl = tvl.pivot(index = 'date', columns = 'chains', values = 'totalLiquidityUSD')
        tvl = tvl.fillna(0)
        tvl = tvl.applymap(int)
        tvl = tvl.reset_index()
        tvl['date'] = tvl['date'].apply(lambda ts: datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d'))

        return(tvl)