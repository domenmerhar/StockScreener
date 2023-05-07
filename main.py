import requests
import matplotlib

apiKey = open("apiKey.txt", "r").read()

ticker = "META"
years = 1

incomeStatement = requests.get(
    f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}?limit={years}&apikey={apiKey}")

incomeStatement = incomeStatement.json()

print(incomeStatement)
