import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
from openai import OpenAI

st.set_page_config(page_title="Bitcoin AI Alpha Terminal v5.0", layout="wide", page_icon="🟠")

st.title("🟠 Bitcoin AI Alpha Terminal v5.0")
st.markdown("**Bloomberg for Bitcoin Treasuries** • Strategy’s Preferred Stock “Bitcoin Bond Market” • Real-time alpha")
st.caption("Built solo in the United States 🇺🇸 • 100% FREE forever")

DONATION_ADDRESS = "bc1qfstxeju0mknz0q2vu8uldvkvxdltrhf6aqggkf"

# ==================== SIDEBAR ====================
xai_key = st.sidebar.text_input("🔑 xAI Grok API Key (makes AI agent real)", type="password")
st.sidebar.caption("Get free key at console.x.ai")
st.sidebar.subheader("💰 Donate BTC")
st.sidebar.code(DONATION_ADDRESS)
st.sidebar.caption("🇺🇸 Any amount keeps this growing from the United States")

# ==================== LIVE DATA & PRICES ====================
data = [
    {"Company": "Strategy", "Ticker": "MSTR", "Country": "US", "BTC": 738731, "Value (B)": 50.66, "mNAV": 0.97, "Strategy": "Preferred + ATM"},
    {"Company": "MARA Holdings, Inc.", "Ticker": "MARA", "Country": "US", "BTC": 53822, "Value (B)": 3.69, "mNAV": 1.04, "Strategy": "Miner treasury"},
    {"Company": "Twenty One Capital", "Ticker": "XXI", "Country": "US", "BTC": 43514, "Value (B)": 2.98, "mNAV": 0.71, "Strategy": "Pure treasury"},
    {"Company": "Metaplanet Inc.", "Ticker": "MPJPY", "Country": "JP", "BTC": 35102, "Value (B)": 2.41, "mNAV": 1.26, "Strategy": "Pure treasury"},
    {"Company": "Bitcoin Standard Treasury Company", "Ticker": "CEPO", "Country": "US", "BTC": 30021, "Value (B)": 2.06, "mNAV": 0.13, "Strategy": "Pure treasury"},
    {"Company": "Bullish", "Ticker": "BLSH", "Country": "US", "BTC": 24300, "Value (B)": 1.67, "mNAV": 2.68, "Strategy": "Pure treasury"},
    {"Company": "Riot Platforms, Inc.", "Ticker": "RIOT", "Country": "US", "BTC": 18005, "Value (B)": 1.24, "mNAV": 4.84, "Strategy": "Miner treasury"},
    {"Company": "Coinbase Global, Inc.", "Ticker": "COIN", "Country": "US", "BTC": 15389, "Value (B)": 1.06, "mNAV": 52.11, "Strategy": "Pure treasury"},
    {"Company": "Hut 8 Mining Corp", "Ticker": "HUT", "Country": "US", "BTC": 13696, "Value (B)": 0.94, "mNAV": 5.91, "Strategy": "Miner treasury"},
    {"Company": "CleanSpark, Inc.", "Ticker": "CLSK", "Country": "US", "BTC": 13363, "Value (B)": 0.92, "mNAV": 3.26, "Strategy": "Miner treasury"},
    {"Company": "Strive", "Ticker": "ASST", "Country": "US", "BTC": 13132, "Value (B)": 0.90, "mNAV": 0.61, "Strategy": "Pure treasury"},
    # Add the rest of your 50+ companies here from v2.0 if you want the full list
    {"Company": "Nano Labs", "Ticker": "NA", "Country": "CN", "BTC": 1000, "Value (B)": 0.07, "mNAV": 0.00, "Strategy": "Pure treasury"}
]

df = pd.DataFrame(data)

@st.cache_data(ttl=60)
def get_live_prices(tickers):
    prices = {}
    for t in tickers:
        try:
            ticker = yf.Ticker(t)
            price = ticker.info.get('currentPrice') or ticker.history(period="1d")['Close'].iloc[-1]
            prices[t] = round(price, 2) if price else None
        except:
            prices[t] = None
    return prices

all_tickers = df['Ticker'].tolist() + ['BTC-USD']
prices = get_live_prices(all_tickers)
btc_price = prices.get('BTC-USD', 68000)

df['Stock Price ($)'] = df['Ticker'].map(prices)
df['BTC Value (B)'] = (df['BTC'] * btc_price / 1_000_000_000).round(2)

# ==================== CLEAN LANDING PAGE ====================
st.metric("🚀 Current Bitcoin Price", f"${btc_price:,}", "Live — updates on refresh")

st.divider()

# ==================== TABS (exactly like your working v2.0) ====================
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Holdings Table", "📈 Charts", "💎 Preferred Offerings", "🤖 Grok AI Agent", "💰 Donations"])

# Paste your existing tab code here (the same Holdings Table, Charts, Preferred Offerings, Grok Agent, and Donations tabs from v2.0).
# Everything works exactly the same — just copy from your current file if needed.

st.divider()
st.caption("v5.0 • Clean landing page • Live BTC price • Built in the United States 🇺🇸")
