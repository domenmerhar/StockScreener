import requests
import matplotlib

apiKey = open("apiKey.txt", "r").read()

ticker = "META"
years = 1


def WipeTxt(ticker: str):
    with open(f"Output\{ticker}.txt", "w") as file:
        file.write("")


def WriteRatios(financialStatement: dict, years: int, cutList: bool, ticker: str, typeOfStatement: str):
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
    WriteRatios(marketCap, years, False, ticker, "Market Cap")
    WriteRatios(incomeStatement, years, True, ticker, "Income Statement")
    WriteRatios(balanceSheet, years, True, ticker, "Balance Sheet")
    WriteRatios(cashFlowStatement, years, True, ticker, "Cash Flow Statement")
    WriteRatios(financialRatios, years, True, ticker, "Financial Ratios")

    """
    with open(f"Output\{ticker}.txt", "w") as f:  # Makes new file if it doesn't exist

        f.write("****Market Cap****\n")
        for ratio in marketCap[0]:
            if (marketCap[0][ratio] != 0):
                f.write(f"{ratio}: {marketCap[0][ratio]}\n")

        f.write("\n****Income Statement****")
        for year in range(years):
            f.write("\n")
            # Gets rid of the first 8 items and the last 2
            ratios = list(incomeStatement[year].keys())[8:-2]
            for ratio in ratios:
                if (incomeStatement[0][ratio] != 0):
                    f.write(f"{ratio}: {incomeStatement[year][ratio]}\n")

        f.write("\n****Balance Sheet****")
        for year in range(years):
            f.write("\n")
            ratios = list(balanceSheet[year].keys())[8:-2]
            for ratio in ratios:
                if (balanceSheet[0][ratio] != 0):
                    f.write(f"{ratio}: {balanceSheet[year][ratio]}\n")

        f.write("\n****Cash Flow Statement****")
        for year in range(years):
            f.write("\n")
            ratios = list(cashFlowStatement[year].keys())[8:-2]
            for ratio in ratios:
                if (cashFlowStatement[0][ratio] != 0):
                    f.write(f"{ratio}: {cashFlowStatement[year][ratio]}\n")

        f.write("\n****Financial Ratios****\n")
        for ratio in financialRatios[0]:
            if (financialRatios[0][ratio] != 0):
                f.write(f"{ratio}: {financialRatios[0][ratio]}\n")
    """


GetInfo(1, "CROX")
