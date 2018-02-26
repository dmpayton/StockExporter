from alpha_vantage.timeseries import TimeSeries
from openpyxl import Workbook
import json
# imports everthing I need
wb = Workbook
ws = wb.active
ts = TimeSeries('N1RDW0MA9WZPJGCK')
# sets a couple variables for libraries I'll need in a sec.
data, meta_data = ts.get_daily(input(str()))
close = data['2018-02-23']['4. close']
print(close)
