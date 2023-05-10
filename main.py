import requests
import matplotlib

apiKey = open("apiKey.txt", "r").read()

ticker = "META"
years = 1


def GetInfo(years: int, ticker: str):  # Hints help document the parameters
    # Get stock info
    marketCap = requests.get(
        f"https://financialmodelingprep.com/api/v3/market-capitalization/{ticker}?apikey={apiKey}")
    incomeStatement = requests.get(
        f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit={years}&apikey={apiKey}")
    balanceSheet = requests.get(
        f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?limit={years}&apikey={apiKey}")
    cashFlowStatement = requests.get(
        f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?limit={years}&apikey={apiKey}")
    financialRatios = requests.get(
        f"https://financialmodelingprep.com/api/v3/ratios-ttm/{ticker}?apikey={apiKey}")

    # Convert to .json file
    marketCap = marketCap.json()
    incomeStatement = incomeStatement.json()
    balanceSheet = balanceSheet.json()
    cashFlowStatement = cashFlowStatement.json()
    financialRatios = financialRatios.json()

    with open(f"Output\{ticker}.txt", "w") as f:  # Makes new file if it doesn't exist

        f.write("****Market Cap****")
        # Cycle through every item in the 2nd dimension
        for ratio in marketCap[0]:
            f.write(f"{ratio}: {marketCap[0][ratio]}\n")

        f.write("\n****Income Statement****\n")
        for ratio in incomeStatement[0]:
            f.write(f"{ratio}: {incomeStatement[0][ratio]}\n")

        f.write("\n****Balance Sheet****\n")
        for ratio in balanceSheet[0]:
            f.write(f"{ratio}: {balanceSheet[0][ratio]}\n")

        f.write("\n****Cash Flow Statement****\n")
        for ratio in cashFlowStatement[0]:
            f.write(f"{ratio}: {cashFlowStatement[0][ratio]}\n")

        f.write("\n****Financial Ratios****\n")
        for ratio in financialRatios[0]:
            f.write(f"{ratio}: {financialRatios[0][ratio]}\n")


GetInfo(1, "CROX")
