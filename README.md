<h1 align="center">ALGOIND: A Technical Indicators collection in Python.</h1>

<div align="center">
<img src="https://komarev.com/ghpvc/?username=matteoincremona&label=Profile%20views&color=blueviolet&style=flat" /> </a>
<img src ="https://img.shields.io/badge/pipy-%3E%20v3.7-blue" /> </a>
<img src ="https://img.shields.io/badge/version-0.0.1-green" /> </a>

![images](https://github.com/matteoincremona/algoind/blob/main/imga.jpg)

<div align="left">

# 🔎 What is it

- **algoind** is small python3 package that contains technical indicators for backtesting and for implementing trading strategies in Python3.

- ### 😃 Who I am
  My name is Matteo Incremona, an italian 21 years old FinTech student, and I created this library for my personal usage. I decided publish it because it can be useful for some people. You can find my [contact] at the aned of this page.

- The source code is currently hosted on GitHub at: https://github.com/...

- Thanks to https://www.investopedia.com that provided me a vast amount of knowledge to be able to create this library.

# 💻 How to Install it
```sh
# conda
conda install -c conda-forge algoind
```

```sh
# PyPI
pip install algoind
```

# 📈 Features 
This is the list of all the indicators **algoind** contains:

  - Single Moving Average (**SMA**)
  - Esponential Moving Average (**EMA**)
  - Average True Range (**ATR**)
  - Relative Strenght Index (**RSI**)
  - Upper Bollinger Bands (**BBU**)
  - Lower Bollinger Bands (**BBL**)
  - Mid Bollinger Bands (**BBM**)
  - Moving Average Convergence Divergence (**MACD**)
  - Moving Average Convergence Divergence Signal (**MACDsignal**)

# ✅ Example: How to use it

```sh
# After the installation of the package:
import algoind
from algoind import xxx

# Let's try SMA: what should we know about it?
help(SMA)

# Let's try SMA that takes, for example:
# - The close prices of a df called data: "data.Close"
# - The period for the calculation of the SMA: "20"
SMA20 = SMA(pandas.Close, 20)

# To see the values of the indicator:
SMA20
```

# 😃 Who I am

[contact]: https://github.com/matteoincremona/TESTLIIB/tree/main#-who-i-am-1
