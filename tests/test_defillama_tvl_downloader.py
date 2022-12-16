from defillama_tvl_downloader import defillama_tvl_downloader

import numpy as np
import pandas as pd
import json
import requests
import os
from datetime  import datetime

def test_protocol_tvl_ts():
    """Test to confirm that invalid protocol names are correctly processed 
    by the time-series funtion"""
    example = protocol_tvl_ts('AAVE V2')
    expected = protocol_tvl_ts('AAVE V2')
    actual = "AAVE V2 and V3 are aggregated in AAVE. Replace you protocol name with 'AAVE.'"
    assert actual == expected