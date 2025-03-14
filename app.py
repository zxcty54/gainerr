from flask import Flask, render_template
import yfinance as yf
import pandas as pd

app = Flask(__name__)  # Gunicorn needs this 'app' variable

@app.route('/')
def index():
    # List of stocks
    stocks = ['ABB.NS',
'ACC.NS',
'APLAPOLLO.NS',
'AUBANK.NS',
'ADANIENSOL.NS',
'ADANIENT.NS',
'ADANIGREEN.NS',
'ADANIPORTS.NS',
'ADANIPOWER.NS',
'ATGL.NS',
'ABCAPITAL.NS',
'ABFRL.NS',
'ALKEM.NS',
'AMBUJACEM.NS',
'APOLLOHOSP.NS',
'APOLLOTYRE.NS',
'ASHOKLEY.NS',
'ASIANPAINT.NS',
'ASTRAL.NS',
'AUROPHARMA.NS',
'DMART.NS',
'AXISBANK.NS',
'BSE.NS',
'BAJAJ-AUTO.NS',
'BAJFINANCE.NS',
'BAJAJFINSV.NS',
'BAJAJHLDNG.NS',
'BALKRISIND.NS',
'BANDHANBNK.NS',
'BANKBARODA.NS',
'BANKINDIA.NS',
'MAHABANK.NS',
'BDL.NS',
'BEL.NS',
'BHARATFORG.NS',
'BHEL.NS',
'BPCL.NS',
'BHARTIARTL.NS',
'BHARTIHEXA.NS',
'BIOCON.NS',
'BOSCHLTD.NS',
'BRITANNIA.NS',
'CGPOWER.NS',
'CANBK.NS',
'CHOLAFIN.NS',
'CIPLA.NS',
'COALINDIA.NS',
'COCHINSHIP.NS',
'COFORGE.NS',
'COLPAL.NS',
'CONCOR.NS',
'CUMMINSIND.NS',
'DLF.NS',
'DABUR.NS',
'DELHIVERY.NS',
'DIVISLAB.NS',
'DIXON.NS',
'DRREDDY.NS',
'EICHERMOT.NS',
'ESCORTS.NS',
'EXIDEIND.NS',
'NYKAA.NS',
'FEDERALBNK.NS',
'FACT.NS',
'GAIL.NS',
'GMRAIRPORT.NS',
'GODREJCP.NS',
'GODREJPROP.NS',
'GRASIM.NS',
'HCLTECH.NS',
'HDFCAMC.NS',
'HDFCBANK.NS',
'HDFCLIFE.NS',
'HAVELLS.NS',
'HEROMOTOCO.NS',
'HINDALCO.NS',
'HAL.NS',
'HINDPETRO.NS',
'HINDUNILVR.NS',
'HINDZINC.NS',
'HUDCO.NS',
'ICICIBANK.NS',
'ICICIGI.NS',
'ICICIPRULI.NS',
'IDBI.NS',
'IDFCFIRSTB.NS',
'IRB.NS',
'ITC.NS',
'INDIANB.NS',
'INDHOTEL.NS',
'IOC.NS',
'IOB.NS',
'IRCTC.NS',
'IRFC.NS',
'IREDA.NS',
'IGL.NS',
'INDUSTOWER.NS',
'INDUSINDBK.NS',
'NAUKRI.NS',
'INFY.NS',
'INDIGO.NS',
'JSWENERGY.NS',
'JSWINFRA.NS',
'JSWSTEEL.NS',
'JINDALSTEL.NS',
'JIOFIN.NS',
'JUBLFOOD.NS',
'KPITTECH.NS',
'KALYANKJIL.NS',
'KOTAKBANK.NS',
'LTF.NS',
'LICHSGFIN.NS',
'LTIM.NS',
'LT.NS',
'LICI.NS',
'LUPIN.NS',
'MRF.NS',
'LODHA.NS',
'M&MFIN.NS',
'M&M.NS',
'MRPL.NS',
'MANKIND.NS',
'MARICO.NS',
'MARUTI.NS',
'MFSL.NS',
'MAXHEALTH.NS',
'MAZDOCK.NS',
'MPHASIS.NS',
'MUTHOOTFIN.NS',
'NHPC.NS',
'NLCINDIA.NS',
'NMDC.NS',
'NTPC.NS',
'NESTLEIND.NS',
'OBEROIRLTY.NS',
'ONGC.NS',
'OIL.NS',
'PAYTM.NS',
'OFSS.NS',
'POLICYBZR.NS',
'PIIND.NS',
'PAGEIND.NS',
'PATANJALI.NS',
'PERSISTENT.NS',
'PETRONET.NS',
'PHOENIXLTD.NS',
'PIDILITIND.NS',
'POLYCAB.NS',
'POONAWALLA.NS',
'PFC.NS',
'POWERGRID.NS',
'PRESTIGE.NS',
'PNB.NS',
'RECLTD.NS',
'RVNL.NS',
'RELIANCE.NS',
'SBICARD.NS',
'SBILIFE.NS',
'SJVN.NS',
'SRF.NS',
'MOTHERSON.NS',
'SHREECEM.NS',
'SHRIRAMFIN.NS',
'SIEMENS.NS',
'SOLARINDS.NS',
'SONACOMS.NS',
'SBIN.NS',
'SAIL.NS',
'SUNPHARMA.NS',
'SUNDARMFIN.NS',
'SUPREMEIND.NS',
'SUZLON.NS',
'TVSMOTOR.NS',
'TATACHEM.NS',
'TATACOMM.NS',
'TCS.NS',
'TATACONSUM.NS',
'TATAELXSI.NS',
'TATAMOTORS.NS',
'TATAPOWER.NS',
'TATASTEEL.NS',
'TATATECH.NS',
'TECHM.NS',
'TITAN.NS',
'TORNTPHARM.NS',
'TORNTPOWER.NS',
'TRENT.NS',
'TIINDIA.NS',
'UPL.NS',
'ULTRACEMCO.NS',
'UNIONBANK.NS',
'UNITDSPR.NS',
'VBL.NS',
'VEDL.NS',
'IDEA.NS',
'VOLTAS.NS',
'WIPRO.NS',
'YESBANK.NS',
'ZOMATO.NS',
'ZYDUSLIFE.NS']

    # Fetch live OHLC data
    data = yf.download(stocks, period='1d', interval='1m')

    # Extract OHLC values
    ohlc = data[['Open', 'High', 'Low', 'Close']].ffill().iloc[-1]

    # Calculate % Change
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

    # Convert to HTML
    table_html = df.to_html(index=False, classes="stock-table", border=1)

    return table_html  # Render the table directly

if __name__ == '__main__':
    app.run(debug=True)
