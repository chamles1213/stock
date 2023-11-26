import yfinance as yf
import streamlit as st

st.write("""
# Stock and Crypto Price App
Shown are the stock **closing price** and **volume** of a stock or cryptocurrency!
""")

# Allow user to input a stock or crypto symbol
symbol = st.text_input("Enter a stock or crypto symbol (e.g. AAPL or BTC-USD)")

# Check if the symbol is for a stock or a cryptocurrency
if '-' in symbol:
    # Retrieve data for the cryptocurrency symbol
    data = yf.download(symbol, start='2020-01-01', end='2023-11-20')
else:
    # Retrieve data for the stock symbol
    data = yf.Ticker(symbol)
    data = data.history(period='id', start='2020-03-20', end='2023-11-20')

# Display line and area charts for the stock or crypto data
st.line_chart(data['Close'], color='#FF0000')
st.line_chart(data['Volume'], color='#00aaff')
st.area_chart(data['Volume'], color='#00ffaa')
st.line_chart(data['Low'], color='#aa00ff')
st.line_chart(data['High'], color='#00FFFF')

# Calculate the difference between high and low prices
difference = data['High'] - data['Low']

for i in difference:
    if i < 0:
        st.write('The asset is basically going down period!')
    else:
        st.write('The asset is up during this time!')
    break

# Display the difference between high and low prices
st.write(f"The difference between the high and low prices is {difference.mean()}")
