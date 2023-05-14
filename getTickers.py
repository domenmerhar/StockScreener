from polygon import RESTClient
import pandas

txtFileLocation = "USTickers.txt"

# Get API key
polygonIoApiKey = open("API Keys\polygonIoApiKey.txt", "r").read()

polygonClient = RESTClient(polygonIoApiKey)
exchanges = list(polygonClient.get_exchanges(
    asset_class="stocks", locale="us"))
USTickers = []

# Wipes List
with open(txtFileLocation, "w") as file:
    file.write("")

with open(txtFileLocation, "a") as file:
    # Goes Through Every Company In Every Exchange
    for company in polygonClient.list_tickers(market="stocks", active=False, limit=1000):
        if company != None:
            file.write(f"{company.ticker}\n")
