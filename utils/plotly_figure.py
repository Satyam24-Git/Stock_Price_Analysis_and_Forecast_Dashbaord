import plotly.graph_objects as go
import pandas_ta as pta
import pandas as pd

# ----------- Table Function -----------
def plotly_table(dataframe):
    headerColor = '#0078ff'
    rowEvenColor = '#f8fafd'
    rowOddColor = '#e1f5fe'

    row_colors = [rowEvenColor if i % 2 == 0 else rowOddColor for i in range(len(dataframe))]

    fig = go.Figure(data=[go.Table(
        header=dict(
            values=["<b>Index</b>"] + ["<b>" + str(col) + "</b>" for col in dataframe.columns],
            fill_color=headerColor,
            align='center',
            font=dict(color='white', size=15),
            line_color='white',
            height=35
        ),
        cells=dict(
            values=[dataframe.index.astype(str).tolist()] + [
                dataframe[col].astype(str).tolist() for col in dataframe.columns
            ],
            fill_color=[row_colors for _ in range(len(dataframe.columns) + 1)],
            align='left',
            line_color='white',
            font=dict(color='black', size=14),
            height=30
        )
    )])

    fig.update_layout(height=400, margin=dict(l=0, r=0, t=0, b=0))
    return fig

# ----------- RSI Function -----------
def RSI(dataframe, num_period):
    dataframe['RSI'] = pta.rsi(dataframe['Close'])
    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['RSI'],
        name='RSI',
        marker_color='orange',
        line=dict(width=2, color='orange')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[70] * len(dataframe),
        name='Overbought',
        marker_color='red',
        line=dict(width=2, color='red', dash='dash')
    ))

    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=[30] * len(dataframe),
        fill='tonexty',
        name='Oversold',
        marker_color='#79da84',
        line=dict(width=2, color='#79da84', dash='dash')
    ))

    fig.update_layout(
        yaxis_range=[0, 100],
        height=200,
        plot_bgcolor='#elefff',
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation='h', yanchor='top', y=1.02, xanchor='right', x=1)
    )
    return fig

# ----------- Moving Average Function -----------
def Moving_average(dataframe, num_period):
    dataframe['SMA_50'] = pta.sma(dataframe['Close'], length=50)
    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Open'], mode='lines', name='Open', line=dict(width=2, color='#5ab7ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Close'], mode='lines', name='Close', line=dict(width=2, color='black')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['High'], mode='lines', name='High', line=dict(width=2, color='#0078ff')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['Low'], mode='lines', name='Low', line=dict(width=2, color='red')))
    fig.add_trace(go.Scatter(x=dataframe['Date'], y=dataframe['SMA_50'], mode='lines', name='SMA_50', line=dict(width=2, color='purple')))

    fig.update_xaxes(rangeslider_visible=True)
    fig.update_layout(
        yaxis_range=[0, 100],
        height=500,
        plot_bgcolor='#elefff',
        paper_bgcolor='#elefff',
        margin=dict(l=0, r=20, t=20, b=0),
        legend=dict(yanchor='top', xanchor='right')
    )
    return fig

# ----------- MACD Function -----------
def MACD(dataframe, num_period):
    macd_data = pta.macd(dataframe['Close'])
    dataframe['MACD'] = macd_data.iloc[:, 0]
    dataframe['MACD Signal'] = macd_data.iloc[:, 1]
    dataframe['MACD Hist'] = macd_data.iloc[:, 2]

    dataframe = filter_data(dataframe, num_period)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['MACD'],
        name='MACD',
        line=dict(width=2, color='blue')
    ))
    fig.add_trace(go.Scatter(
        x=dataframe['Date'],
        y=dataframe['MACD Signal'],
        name='MACD Signal',
        line=dict(width=2, color='red')
    ))
    fig.add_trace(go.Bar(
        x=dataframe['Date'],
        y=dataframe['MACD Hist'],
        name='MACD Histogram',
        marker_color=['green' if val > 0 else 'red' for val in dataframe['MACD Hist']]
    ))

    fig.update_layout(
        height=200,
        plot_bgcolor='white',
        paper_bgcolor='#elefff',
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation='h', yanchor='top', y=1.02, xanchor='right', x=1)
    )
    return fig

# ----------- Filter Function -----------
def filter_data(dataframe, num_period):
    return dataframe.tail(num_period).reset_index(drop=True)
