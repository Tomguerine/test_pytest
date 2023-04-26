import pandas as pd
import time
from binance.client import Client
from datetime import datetime
import json
import pandas as pd

# Fichier binanceAdapter
#api_key = "3Po2NaBCl6XvLuApEqK745gfFsZd9JMfafE11pHt3CqJNa2BuXP9vMdl9Wa3ZcEv"
#api_secret = "vqoukQTxRWUj9cXdUvy1yisiouzrN51jY07xOQOtAEM9CyNTvfpd998LPzCbuqgl"
class BinanceAdapter():
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret  

    def validate(api_key, api_secret):
        try:
            return Client(api_key, api_secret).get_account_status()["data"] == "Normal"
        except:
            return False
    def account(userid,api_key,api_secret):
        try:
            account_data = Client(api_key, api_secret).get_account()
            # Create DataFrame from account data
            df = pd.DataFrame.from_dict(account_data["balances"])
            df["amount"] = df["free"].astype(float) + df["locked"].astype(float)
            df = df.loc[df["amount"] > 1]
            df = df.drop(columns=["free", "locked"])
            df["userid"] = userid
            print(df)
            return True
        except:
             return False




        
api_key = "3Po2NaBCl6XvLuApEqK745gfFsZd9JMfafE11pHt3CqJNa2BuXP9vMdl9Wa3ZcEv"
api_secret = "vqoukQTxRWUj9cXdUvy1yisiouzrN51jY07xOQOtAEM9CyNTvfpd998LPzCbuqgl"
userid="1122321"






#fichier valide consumer

def validation(api_key,api_secret):     
    if BinanceAdapter.validate(api_key, api_secret):
        # produce event to queue "account_listing"
            return True
    else:
            return False

     

validation(api_key,api_secret)
print(BinanceAdapter.account(userid,api_key, api_secret))