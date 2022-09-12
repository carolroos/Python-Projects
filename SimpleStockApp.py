import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
#Simple Stock price App

Shown are the stock closing price and volume

""")


tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2012-09-01', end = '2022-09-01')

st.line_chart(tickerDf.Close)

st.line_chart(tickerDf.Volume)
