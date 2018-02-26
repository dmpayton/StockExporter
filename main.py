# imports everthing I need
from alpha_vantage.timeseries import TimeSeries
from openpyxl import Workbook
import datetime
import json
# sets a couple variables for libraries I'll need in a sec.
wb = Workbook
ws = wb.active
ts = TimeSeries('N1RDW0MA9WZPJGCK')
now = datetime.datetime.now()
stringnow = str(now)
todaysdate = (stringnow[:10])
#Prints an intro message
intromessage = """Stock Exporter V1.0
This app takes data for securities with tickers, accepts input in the form of a
ticker, and then creates an Excel document and writes the values for Open,
Close, High, Low, and Volume into the appropriate cells.
Type the Ticker for your desired security in now."""
print(intromessage)
data, meta_data = ts.get_daily(input(str()))
openvalue = data[todaysdate]['1. open']
highvalue = data[todaysdate]['2. high']
lowvalue = data[todaysdate]['3. low']
closevalue = data[todaysdate]['4. close']
print("Open Price:" + openvalue)
print("High Price:" + highvalue)
print("Low Price:" + lowvalue)
print("Close Price:" + closevalue)
