import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
from openai import OpenAI
import streamlit.components.v1 as components

st.set_page_config(page_title="Bitcoin AI Alpha Terminal v4.0", layout="wide", page_icon="🟠")

st.title("🟠 Bitcoin AI Alpha Terminal v4.0")
st.markdown("**Bloomberg for Bitcoin Treasuries** • Strategy’s Preferred Stock “Bitcoin Bond Market” • Real-time alpha")
st.caption("Built solo in the United States 🇺🇸 • 100% FREE forever")

DONATION_ADDRESS = "bc1qfstxeju0mknz0q2vu8uldvkvxdltrhf6aqggkf"

# ==================== SIDEBAR ====================
xai_key = st.sidebar.text_input("🔑 xAI Grok API Key (makes AI agent real)", type="password")
st.sidebar.caption("Get free key at console.x.ai")
st.sidebar.subheader("💰 Donate BTC")
st.sidebar.code(DONATION_ADDRESS)
st.sidebar.caption("🇺🇸 Any amount keeps this growing from the United States")

# ==================== LIVE DATA & PRICES (v2.0 unchanged) ====================
data = [
    {"Company": "Strategy", "Ticker": "MSTR", "Country": "US", "BTC": 738731, "Value (B)": 50.66, "mNAV": 0.97, "Strategy": "Preferred + ATM"},
    {"Company": "MARA Holdings, Inc.", "Ticker": "MARA", "Country": "US", "BTC": 53822, "Value (B)": 3.69, "mNAV": 1.04, "Strategy": "Miner treasury"},
    # ... (your full 50+ company list from v2.0 is still here — paste your existing data block if you want, or keep the shortened one for now)
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

# ==================== LANDING PAGE — BIG BTC PRICE + LIVE WINDOWS ====================
st.metric("🚀 Current Bitcoin Price", f"${btc_price:,}", "Live — updates on refresh")

st.subheader("🌍 Live Bitcoin Ecosystem Feeds")
st.caption("Two independent creator tools that perfectly complement your terminal")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**strc.live** — Strategy & Strive Preferred Stock Live Tracker")
    try:
        components.iframe("https://strc.live", height=520, width=700)
    except:
        pass
    st.caption("Powered by strc.live • Support the creator with sats if you love it!")
    st.link_button("Open strc.live full screen →", "https://strc.live", use_container_width=True)

with col2:
    st.markdown("**bitfeed.live** — Live Bitcoin Transaction Fireworks Feed")
    try:
        components.iframe("https://bitfeed.live", height=520)
    except:
        pass
    st.caption("Powered by bitfeed.live • Support the creator with sats if you love it!")
    st.link_button("Open bitfeed.live full screen →", "https://bitfeed.live", use_container_width=True)

st.divider()

# ==================== REST OF THE APP (Tabs from v2.0 unchanged) ====================
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Holdings Table", "📈 Charts", "💎 Preferred Offerings", "🤖 Grok AI Agent", "💰 Donations"])

# (Copy-paste your existing tab1–tab5 code from v2.0 here — Holdings Table, Charts, Preferred Offerings, Grok Agent, Donations. 
# It’s the exact same as before so everything still works perfectly.)

st.divider()
st.caption("v4.0 • Live feeds + US flag added • Refresh for fresh prices • Built for you in the United States 🇺🇸")
