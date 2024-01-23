<h1 align="center">ALGOIND: A Technical Indicators collection in Python.</h1>

<div align="center">
<img src="https://komarev.com/ghpvc/?username=matteoincremona&label=Profile%20views&color=blueviolet&style=flat" /> </a>
<img src ="https://img.shields.io/badge/pipy-%3E%20v3.7-blue" /> </a>
<img src ="https://img.shields.io/badge/version-0.0.3-green" /> </a>
<img src= "https://raw.githubusercontent.com/matteoincremona/algoind/main/logo.svg">

<div align="left">

# 🔎 What is it

- **algoind** is a python3 package that contains technical indicators for backtesting and for implementing trading strategies.

- ### 😃 Who I am
  - My name is Matteo, a 21-year-old FinTech student.
  - I created this library for personal usage and I decided to publish it because it can be useful for someone.
  - 👋 You can find my [contacts here].

- The source code is currently hosted on GitHub at: https://github.com/matteoincremona/algoind/

- Thanks to [Investopedia.com] which provided me a vast amount of knowledge to be able to create this library.

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
  - Exponential Moving Average (**EMA**)
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
from algoind import indicators as ind

# Let's try SMA: what should we know about it?
help(ind.SMA)

# Let's try SMA that takes, for example:
# - The close prices of a df: "df.Close"
# - The period for the calculation of the SMA: "20"
SMA20 = ind.SMA(df.Close, 20)

# To see the values of the indicator:
print(SMA20)
```
# ⚙️ Discussion and Development
I would be very enthusiastic if somebody would like to help me with this project.

[Contact me] if you have any **problem** or if you want me to add **new indicators**.

Thank you.

[contacts here]: https://github.com/matteoincremona/matteoincremona/
[Investopedia.com]: https://www.investopedia.com
[Contact me]: https://github.com/matteoincremona/matteoincremona/
