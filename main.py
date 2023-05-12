import requests
import matplotlib

apiKey = open("apiKey.txt", "r").read()

ticker = "META"
years = 1


def WipeTxt(ticker: str):
    with open(f"Output\{ticker}.txt", "w") as file:
        file.write("")


def AppendMarketCap(marketCap: dict, ticker: str):
    with open(f"Output\{ticker}.txt", "a") as file:
        file.write(f"Market Cap: {marketCap[0]['marketCap']}\n\n")


def AppendRatios(financialStatement: dict, years: int, cutList: bool, ticker: str, typeOfStatement: str):
    with open(f"Output\{ticker}.txt", "a") as file:
        file.write(f"****{typeOfStatement.capitalize()}****")

        for year in range(years):
            file.write("\n")

            if (cutList):
                ratios = list(financialStatement[year].keys())[
                    8:-2]  # Cuts the first 8 and last 2 elements

                for ratio in ratios:
                    if (financialStatement[year][ratio] != 0):
                        file.write(
                            f"{ratio}: {financialStatement[year][ratio]}\n")
            else:
                for ratio in financialStatement[year]:
                    if (financialStatement[year][ratio] != 0):
                        file.write(
                            f"{ratio}: {financialStatement[year][ratio]}\n")
            file.write("\n")


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

    WipeTxt(ticker)
    AppendMarketCap(marketCap, ticker)
    AppendRatios(incomeStatement, years, True, ticker, "Income Statement")
    AppendRatios(balanceSheet, years, True, ticker, "Balance Sheet")
    AppendRatios(cashFlowStatement, years, True, ticker, "Cash Flow Statement")
    AppendRatios(financialRatios, years, True, ticker, "Financial Ratios")


GetInfo(1, "CROX")
