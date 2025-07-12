# Stock_Price_Analysis_and_Forecast_Dashbaord
Stock Price Prediction & Analysis WebApp
This project is a full-featured Stock Market WebApp built using Streamlit, designed to:

📊 Analyze historical stock data

Predict future stock prices using the ARIMA model

Visualize technical indicators such as Moving Averages, RSI, and MACD

Display interactive tables using Plotly

Features
- Feature	Description
- Forecasting	Predicts next 30 days' close prices using the ARIMA model
- Moving Averages	Visualizes Open, Close, High, Low and 50-day SMA
- RSI & MACD	Detect overbought/oversold conditions & trend strength
- Forecast Table	Interactive forecast table using Plotly
- Streamlit UI	Easy-to-use sliders, inputs, and buttons

📦 Folder Structure
bash
Edit
├── app.py                        # Homepage (Streamlit)
├── pages/
│   ├── Stock_analysis.py        # Technical indicators page
│   └── Stock_prediction.py      # Price prediction page
├── utils/
│   ├── model_train.py           # ARIMA model, scaler, forecasting utils
│   └── plotly_figure.py         # Plotly chart helper functions
├── requirements.txt             # Python dependencies
└── README.md                    # You're reading it!


🚀 How to Run
Clone the repository:

bash
git clone https://github.com/yourusername/stock-price-webapp.git
cd stock-price-webapp
Install dependencies:

bash
pip install -r requirements.txt
Run the app:

bash
streamlit run app.py
