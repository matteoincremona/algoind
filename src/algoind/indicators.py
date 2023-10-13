def SMA(array, period):
    """SINGLE MOVING AVERAGE
    ---
    
    Calculate the Single Moving Average (SMA) of given prices.

    Parameters:
    ---
    - `array` (pandas.Series): The list of the Close prices of the financial instrument.
    - `period` (int): The period to use for the SMA calculation.
    
    Return:
    ---
    - The values (pandas.Series) the values of the SMA calculated based on the prices and the period given.
    
    Source: https://www.investopedia.com/terms/m/movingaverage.asp
    """
    
    return array.rolling(period).mean()

def RSI(array, period):
    """RELATIVE STRENGHT INDEX
    ---
    
    Calculate the Relative Strenght Index (RSI).
    
    Parameters:
    ---
    - `array` (pandas.Series): The list of the Close prices of the financial instrument.
    - `period` (int): The period to use for the RSI (default = 14).
    
    Return:
    ---
    - The values (pandas.Series) the values of the RSI calculated based on the prices and the period given.
    
    Source: https://www.investopedia.com/terms/r/rsi.asp
    """
  
    var = array.diff()
    gain = var.where(var > 0, 0)
    loss = - var.where(var < 0, 0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
  
    return rsi

def MACD(array, slow_n, fast_n):
    """MOVING AVERAGE CONVERGENCE DIVERGENCE
    ---
  
    Calculate the Moving Average Convergence Divergence (MACD).

    Parameters:
    ---
    - `array` (pandas.Series): The list of the Close prices of the financial instrument.
    - `slow_n` (int): The value of the period for the calculation of the slow moving average (default = 26).
    - `fast_n` (int): The value of the period for the calculation of the fast moving average (default = 12).
    
    Return:
    ---
    - The values (pandas.Series) the values of the MACD calculated based on the prices and periods given.
    
    Source: https://www.investopedia.com/terms/m/macd.asp
    """
    slow = array.ewm(span = slow_n, adjust = False).mean()
    fast = array.ewm(span = fast_n, adjust = False).mean()
    macd = fast - slow
  
    return macd

# We can also calculate a signal for the MACD, that is a moving average based on the MACD values.

def MACDsignal(macd_values, period):
    """MOVING AVERAGE CONVERGENCE DIVERGENCE SIGNAL
    ---

    Calculate a moving average based on the MACD values and a given period.

    Parameters:
    ---
    - `macd_values` (pandas.Series): The values of the MACD of the financial instrument. (see function called "MACD").
    - `period` (int): The value of the period for the calculation of the moving average (default = 9).
    
    Return:
    ---
    - The values (pandas.Series) the values of the moving average based on the MACD values and the given period.
    
    Source: https://www.investopedia.com/terms/m/macd.asp
    """
    sig = macd_values.ewm(span = period, adjust = False).mean()

    return sig

def EMA(array, period):
    """ESPONENTIAL MOVING AVERAGE or ESPONENTIAL WEIGHTED MOVING AVERAGE
    ---
    
    Calculate the Esponential Moving Average (EMA), also called Esponential Weighted Moving Average (EWMA).

    Parameters:
    ---
    - `array` (pandas.Series): The list of the Close prices of the financial instrument.
    - `period` (int): The period to use for the EMA calculation.
    
    Return:
    ---
    - The values (pandas.Series) the values of the EMA calculated based on the prices and the period given.
    
    Source: https://www.investopedia.com/terms/e/ema.asp
    """
    res = array.ewm(span = period, adjust = False).mean()
    
    return res

# LOWER Bollinger Band

def BBL(array, period, k):
    """LOWER BOLLINGER BAND
    ---
    
    Calculate the Lower Bollinger Band of given prices.

    Parameters:
    ---
    - `array` (pandas.Series): The list of the Close prices of the financial instrument.
    - `period` (int): The period to use for the BB calculation (default = 20).
    - `k` (int): The standard deviation (default = 2).
    
    Return:
    ---
    - The values (pandas.Series) the values of the Lower BB calculated based on prices, period and sd given.
    
    Source: https://www.investopedia.com/terms/b/bollingerbands.asp
    """
    
    BBlow = array.rolling(period).mean() - k * array.rolling(period).std()
    
    return BBlow

# MID Bollinger Band

def BBM(array, period, k):
    """MID BOLLINGER BAND
    ---
    
    Calculate the Mid Bollinger Band (mean of the Upper and Lower BBs) of given prices.

    Parameters:
    ---
    - `array` (pandas.Series): The list of the Close prices of the financial instrument.
    - `period` (int): The period to use for the BB calculation (default = 20).
    - `k` (int): The standard deviation (default = 2).
    
    Return:
    ---
    - The values (pandas.Series) the values of the Mid BB calculated based on prices, period and sd given.
    
    Source: https://www.investopedia.com/terms/b/bollingerbands.asp
    """
    
    BBup = array.rolling(period).mean() + k * array.rolling(period).std()
    BBlow = array.rolling(period).mean() - k * array.rolling(period).std()
    BBmid = (BBup + BBlow) / 2
    
    return BBmid

# UPPER Bollinger Band

def BBU(array, period, k):
    """UPPER BOLLINGER BAND
    ---
    
    Calculate the Upper Bollinger Band of given prices.

    Parameters:
    ---
    - `array` (pandas.Series): The list of the Close prices of the financial instrument.
    - `period` (int): The period to use for the BB calculation (default = 20).
    - `k` (int): The standard deviation (default = 2).
    
    Return:
    ---
    - The values (pandas.Series) the values of the Upper BB calculated based on prices, period and sd given.
    
    Source: https://www.investopedia.com/terms/b/bollingerbands.asp
    """
    
    BBup = array.rolling(period).mean() + k * array.rolling(period).std()
    
    return BBup

def ATR(High, Low, Close, n):
    """AVERAGE TRUE RANGE
    ---
    
    Calculate the Average True Range (ATR).

    Parameters:
    ---
    - `High` (pandas.Series): The list of the High prices of the financial instrument.
    - `Low` (pandas.Series): The list of the Low prices of the financial instrument.
    - `Close` (pandas.Series): The list of the Close prices of the financial instrument.
    - `n` (int): The period to use for the ATR calculation (default = 14).
    
    Return:
    ---
    - The values (pandas.Series) the values of the ATR calculated based on the prices and the period given.
    
    Source: https://www.investopedia.com/terms/r/rsi.asp
    """
    tr0 = abs(High - Low)
    tr1 = abs(High - Close.shift())
    tr2 = abs(Low - Close.shift())
    db = pd.DataFrame({"tr0": tr0, "tr1": tr1, "tr2": tr2})
    tr = db.max(axis = 1)
    atr = tr.ewm(span = n, adjust = False).mean()
  
    return atr



