import streamlit as st
import pandas as pd
import yfinance as yf
from utils.plotly_figure import plotly_table, RSI, Moving_average, MACD, filter_data

st.title("📈 Stock Technical Analysis")

col1, col2, col3 = st.columns(3)

today = pd.to_datetime("today").date()

with col1:
    ticker = st.text_input("Enter Stock Ticker", value="AAPL")
with col2:
    start_date = st.date_input("Start Date", pd.to_datetime(today.replace(year=today.year - 1)))
with col3:
    end_date = st.date_input("End Date", today)

if st.button("Analyze"):
    data = yf.download(ticker, start=start_date, end=end_date)
    data.reset_index(inplace=True)
    data['Date'] = pd.to_datetime(data['Date'])

    st.subheader(f"Stock Info: {ticker}")
    info = yf.Ticker(ticker).info
    st.write("**Sector:**", info.get('sector', 'N/A'))
    st.write("**Employees:**", info.get('fullTimeEmployees', 'N/A'))
    st.write("**Website:**", info.get('website', 'N/A'))
    st.write("**Summary:**", info.get('longBusinessSummary', 'N/A'))

    st.plotly_chart(plotly_table(data.tail(10)), use_container_width=True)
    st.plotly_chart(Moving_average(data, 100), use_container_width=True)
    st.plotly_chart(RSI(data, 100), use_container_width=True)
    st.plotly_chart(MACD(data, 100), use_container_width=True)
