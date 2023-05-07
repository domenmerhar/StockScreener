import requests
import matplotlib

apiKey = open("apiKey.txt", "r").read()

ticker = "META"
years = 1

# Get stock info
marketCap = requests.get(
    f"https://financialmodelingprep.com/api/v3/market-capitalization/{ticker}?apikey={apiKey}")
incomeStatement = requests.get(
    f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit={years}&apikey={apiKey}")
balanceSheet = requests.get(
    f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?limit={years}&apikey={apiKey}")
cashFlowStatement = requests.get(
    f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?limit={years}&apikey={apiKey}")

# Convert to .json file
marketCap = marketCap.json()
incomeStatement = incomeStatement.json()
balanceSheet = balanceSheet.json()
cashFlowStatement = cashFlowStatement.json()

financialRatios = {
    "ticker": ticker,
    "Free Cash Flow yield": cashFlowStatement[0]["freeCashFlow"] / marketCap[0]["marketCap"]
}

print(financialRatios)
