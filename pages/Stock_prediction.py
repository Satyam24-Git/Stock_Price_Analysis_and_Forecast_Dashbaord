import streamlit as st
import pandas as pd
from utils.model_train import (
    get_data, get_rolling_mean, get_differencing_order, scaling,
    evaluate_model, fit_model, get_forcasting, inverse_scaling
)
from utils.plotly_figure import plotly_table, Moving_average

st.set_page_config(
    page_title='Stock Prediction',
    page_icon='📈',
    layout='wide'
)

st.title("📊 Stock Prediction Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    ticker = st.text_input('Stock Ticker', 'AAPL')

if ticker:
    st.subheader("Predicting next 30 days closing price - " + ticker)

    close_price = get_data(ticker)
    rolling_price = get_rolling_mean(close_price)

    differencing_order = get_differencing_order(rolling_price)
    scaled_data, scaler = scaling(rolling_price)
    rsme = evaluate_model(scaled_data, differencing_order)

    st.write("**Model RMSE SCORE:**", rsme)

    forecast = get_forcasting(scaled_data, differencing_order)
    forecast['Close'] = inverse_scaling(scaler, forecast['Close'])

    st.write('##### 📅 Forecast Data (Next 30 Days)')
    fig_tail = plotly_table(forecast.round(3))
    fig_tail.update_layout(height=220)
    st.plotly_chart(fig_tail, use_container_width=True)

    combined = pd.concat([rolling_price, forecast])
    combined.index.name = 'Date'
    st.plotly_chart(Moving_average(combined).update_layout(title='📈 Moving Average with Forecast'), use_container_width=True)
