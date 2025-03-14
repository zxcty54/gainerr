import yfinance as yf
import pandas as pd

# List of stocks (Add all 2000 symbols)
stocks = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFC.NS', 'ICICIBANK.NS']  # Add all stocks

# Fetch live OHLC data
data = yf.download(stocks, period='1d', interval='1m')

# Extract OHLC values
ohlc = data[['Open', 'High', 'Low', 'Close']].ffill().iloc[-1]

# Calculate percentage change from previous close
prev_close = data['Close'].ffill().iloc[-2]
percentage_change = ((ohlc['Close'] - prev_close) / prev_close) * 100

# Create DataFrame
df = pd.DataFrame({
    'Stock': stocks,
    'Open': ohlc['Open'],
    'High': ohlc['High'],
    'Low': ohlc['Low'],
    'Close': ohlc['Close'],
    'Change (%)': percentage_change
})

# Save as an HTML table (Only table rows for AJAX)
table_html = df.to_html(index=False, classes="stock-table", border=1)

with open("stocks_data.html", "w", encoding="utf-8") as f:
    f.write(table_html)

print("Stock data updated successfully!")
