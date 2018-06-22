import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas_datareader import data, wb
import lib

'''
# NYSE
url_nyse = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download"
# Nasdaq
url_nasdaq = "http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download"

nyse = pd.DataFrame.from_csv(url_nyse)
nasdaq = pd.DataFrame.from_csv(url_nasdaq)
validTickers = nyse.index.tolist() + nasdaq.index.tolist()
'''

start = datetime(2018, 1, 1)
end = datetime(2018, 6, 21)

t = "TSLA"

print(lib.getHistoricalData(t,start))
print(lib.getIEXTopsData(t))