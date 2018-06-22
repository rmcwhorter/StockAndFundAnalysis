import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas_datareader import data, wb

def getHistoricalData(ticker, start, end=datetime.now(), source='iex'):
    return data.DataReader(ticker,source,start,end)

def getIEXTopsData(ticker):
    return data.DataReader(ticker, 'iex-tops')