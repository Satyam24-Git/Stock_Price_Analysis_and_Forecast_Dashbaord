import streamlit as st

# Set page config with title "Home"
st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

# App title and intro
st.title("🏠 STOCK PRICE ANALYSIS AND PREDICTION APP")

st.markdown("### 🧠 About the App")
st.markdown("""
This web application allows you to analyze and forecast stock prices using historical data and technical indicators.

✅ **Stock Information**  
Get detailed information about any publicly listed company, including its business summary, sector, and key financial statistics.

📊 **Technical Analysis**  
Visualize stock trends with Moving Averages, RSI, and MACD to better understand market behavior.

🔮 **Stock Price Forecasting**  
Predict future stock prices using machine learning models, helping you make informed investment decisions.

Whether you're a beginner or an experienced trader, this app provides essential tools to support your market analysis — all in one place.
""")


col1, col2 = st.columns(2)

with col1:
    st.markdown("#### :one: Stock Information")
    st.write("See all the stock info you need")
    if st.button("Go to Stock Info"):
        st.switch_page("pages/stock_analysis.py")

with col2:
    st.markdown("#### :two: Stock Prediction")
    st.write("See the forecast of the stock")
    if st.button("Go to Prediction"):
        st.switch_page("pages/stock_prediction.py")
