import json
from binance.client import Client
api_key = "3Po2NaBCl6XvLuApEqK745gfFsZd9JMfafE11pHt3CqJNa2BuXP9vMdl9Wa3ZcEv"
api_secret = "vqoukQTxRWUj9cXdUvy1yisiouzrN51jY07xOQOtAEM9CyNTvfpd998LPzCbuqgl"
userid="1122321"

def save_balance_to_json(api_key, api_secret, filename):
    # Get account data
    balances = Client(api_key, api_secret).get_account()


    # Save balances to JSON file
    with open(filename, "w") as f:
        json.dump(balances, f)

    print(f"Balance saved to {filename}")

save_balance_to_json(api_key, api_secret,userid)
