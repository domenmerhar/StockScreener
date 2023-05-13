import requests
import matplotlib

apiKey = open("apiKey.txt", "r").read()

ticker = "MSFT"
years = 5


def WipeTxt(ticker: str):
    with open(f"Output\{ticker}.txt", "w") as file:
        file.write("")


def AppendMarketCap(marketCap: dict, ticker: str):
    with open(f"Output\{ticker}.txt", "a") as file:
        file.write(f"Market Cap: {marketCap[0]['marketCap']}\n\n")


def AppendRatios(financialStatement: dict, cutList: bool, ticker: str, typeOfStatement: str, years: int = 1):
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


def FinancialRatioGrowth(incomeGrowthStatement: dict, financialRatios: str, years: int):
    periodGrowth = 1
    for year in range(years - 1):
        FYgrowth = int(incomeGrowthStatement[year][financialRatios])
        if (FYgrowth < 0):
            periodGrowth += FYgrowth * periodGrowth
        else:
            periodGrowth *= FYgrowth + 1
    return periodGrowth * 100


def GetInfo(years: int, ticker: str, apiKey: str):  # Hints help document the parameters
    # Get stock info
    marketCap = requests.get(
        f"https://financialmodelingprep.com/api/v3/market-capitalization/{ticker}?apikey={apiKey}").json()
    incomeStatement = requests.get(
        f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit={years}&apikey={apiKey}").json()
    balanceSheet = requests.get(
        f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?limit={years}&apikey={apiKey}").json()
    cashFlowStatement = requests.get(
        f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?limit={years}&apikey={apiKey}").json()
    financialRatios = requests.get(
        f"https://financialmodelingprep.com/api/v3/ratios-ttm/{ticker}?apikey={apiKey}").json()

    WipeTxt(ticker)
    # AppendMarketCap(marketCap, ticker)
    # AppendRatios(incomeStatement, True, ticker, "Income Statement", years)
    # AppendRatios(balanceSheet, True, ticker, "Balance Sheet", years)
    # AppendRatios(cashFlowStatement, True, ticker, "Cash Flow Statement", years)
    # AppendRatios(financialRatios, True, ticker, "Financial Ratios", years)

    incomeGrowth = requests.get(
        f"https://financialmodelingprep.com/api/v3/income-statement-growth/{ticker}?limit={years}&apikey={apiKey}").json()

    with open(f"Output\{ticker}.txt", "a") as file:
        file.write(
            f"{FinancialRatioGrowth(incomeGrowth, 'growthEPS', years)}%\n")


GetInfo(years, ticker, apiKey)
