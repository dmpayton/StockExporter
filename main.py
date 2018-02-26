import datetime
import json

from decimal import Decimal

from alpha_vantage.timeseries import TimeSeries
# from openpyxl import Workbook # (Will start importing once I need it)

# Setup a workbook/worksheet
# wb = Workbook
# ws = wb.active

ts = TimeSeries('N1RDW0MA9WZPJGCK')

# str(datetime.date.today()) would work, but
# explicit is better than implicit.
today = datetime.date.today().strftime('%Y-%m-%d')

# Print an intro message and get the ticker symbol
intro_message = """
Stock Exporter V1.0

This app takes data for securities with tickers, accepts input in the
form of a ticker, and then creates an Excel document and writes the
values for Open, Close, High, Low, and Volume into the appropriate cells.

Type the Ticker for your desired security in now.
"""

error_message = """
Sorry, "{0}" is not a valid ticker. Please enter a new ticker.
"""

print(intro_message)

# Ask the user for a ticker and try to fetch the data.
# If the user enters an invalid ticker, try again.
while True:
    ticker = input('> ')
    try:
        data, meta = ts.get_daily(ticker)
    except ValueError:
        # The API raises a ValueError when an invalid ticker
        # is passed in, so display an approproiate error message.
        print(error_message.format(ticker))
    else:
        # The API didn't raise an exception, which means
        # we got valid data back and can break the loop.
        break

# Get the values we need and convert them to Decimal
# (Monetary values should *always* be Decimal types
# because of how floating point math works.)
open_value = Decimal(data[today]['1. open'])
high_value = Decimal(data[today]['2. high'])
low_value = Decimal(data[today]['3. low'])
close_value = Decimal(data[today]['4. close'])

# Print the data, formating the values for
# better human readibility.
print("Open: ${0:,.2f}".format(open_value))
print("High: ${0:,.2f}".format(high_value))
print("Low: ${0:,.2f}".format(low_value))
print("Close: ${0:,.2f}".format(close_value))
