import json, requests, re
from pathlib import Path

file = Path.cwd()/"csv_reports"/"summary_report.txt"
file.touch()
# Create the text file summary_report

def api_function():
# Create a function
    with file.open(mode = "w" , encoding = 'UTF-8' , newline = '') as text:
    # Open the summmary_report text file

        api_key = "6B4S1U6RBFT3Q19Q"
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
        api = requests.get(url)
        api = api.json()
        # Get the api url

        api = json.dumps(api, indent=4)
        # Make the output neater
        pattern = 'Exchange Rate": ".+'
        api = re.search(pattern, api)
        ER = api.group(0).strip('Exchange Rate":"').strip('",')
        # Extract the exchange rate


        ER = float(ER)
        # Make ER a float instead of a string
        text.writelines(f"[REAL TIME CURRENCY RATE]: USD1 = SGD{ER}\n")
        # Print [REAL TIME CURRENCY RATE]: USD1 = SGD" for summary_report.txt
        return ER
        # Return ER for forex in main.py