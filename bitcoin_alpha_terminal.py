import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf
from openai import OpenAI
from datetime import datetime

st.set_page_config(page_title="Bitcoin Alpha Terminal", layout="wide", page_icon="🟠")

st.title("🟠 BITCOIN ALPHA TERMINAL")
st.caption("Built solo in the United States 🇺🇸 • 100% FREE forever")

DONATION_ADDRESS = "bc1qfstxeju0mknz0q2vu8uldvkvxdltrhf6aqggkf"

# ==================== SIDEBAR ====================
xai_key = st.sidebar.text_input("🔑 xAI Grok API Key (makes AI agent real)", type="password")
st.sidebar.caption("Get free key at console.x.ai")
st.sidebar.subheader("💰 Donate BTC")
st.sidebar.code(DONATION_ADDRESS)
st.sidebar.caption("🇺🇸 Any amount keeps this growing from the United States")

# ==================== FULL CLEAN DATA ====================
data = [
    {"Company": "Strategy", "Ticker": "MSTR", "BTC": 738731, "Value (B)": 50.66, "mNAV": 0.97, "Strategy": "Preferred + ATM"},
    {"Company": "MARA Holdings, Inc.", "Ticker": "MARA", "BTC": 53822, "Value (B)": 3.69, "mNAV": 1.04, "Strategy": "Miner treasury"},
    {"Company": "Twenty One Capital", "Ticker": "XXI", "BTC": 43514, "Value (B)": 2.98, "mNAV": 0.71, "Strategy": "Pure treasury"},
    {"Company": "Metaplanet Inc.", "Ticker": "MPJPY", "BTC": 35102, "Value (B)": 2.41, "mNAV": 1.26, "Strategy": "Pure treasury"},
    {"Company": "Bitcoin Standard Treasury Company", "Ticker": "CEPO", "BTC": 30021, "Value (B)": 2.06, "mNAV": 0.13, "Strategy": "Pure treasury"},
    {"Company": "Bullish", "Ticker": "BLSH", "BTC": 24300, "Value (B)": 1.67, "mNAV": 2.68, "Strategy": "Pure treasury"},
    {"Company": "Riot Platforms, Inc.", "Ticker": "RIOT", "BTC": 18005, "Value (B)": 1.24, "mNAV": 4.84, "Strategy": "Miner treasury"},
    {"Company": "Coinbase Global, Inc.", "Ticker": "COIN", "BTC": 15389, "Value (B)": 1.06, "mNAV": 52.11, "Strategy": "Pure treasury"},
    {"Company": "Hut 8 Mining Corp", "Ticker": "HUT", "BTC": 13696, "Value (B)": 0.94, "mNAV": 5.91, "Strategy": "Miner treasury"},
    {"Company": "CleanSpark, Inc.", "Ticker": "CLSK", "BTC": 13363, "Value (B)": 0.92, "mNAV": 3.26, "Strategy": "Miner treasury"},
    {"Company": "Strive", "Ticker": "ASST", "BTC": 13132, "Value (B)": 0.90, "mNAV": 0.61, "Strategy": "Pure treasury"},
    {"Company": "Tesla, Inc.", "Ticker": "TSLA", "BTC": 11509, "Value (B)": 0.79, "mNAV": 0.00, "Strategy": "Pure treasury"},
    {"Company": "Trump Media & Technology Group Corp.", "Ticker": "DJT", "BTC": 9542, "Value (B)": 0.65, "mNAV": 3.70, "Strategy": "Pure treasury"},
    {"Company": "Block, Inc.", "Ticker": "XYZ", "BTC": 8883, "Value (B)": 0.61, "mNAV": 65.84, "Strategy": "Pure treasury"},
    {"Company": "GD Culture Group", "Ticker": "GDC", "BTC": 7500, "Value (B)": 0.51, "mNAV": 0.47, "Strategy": "Pure treasury"},
    {"Company": "Galaxy Digital Holdings Ltd", "Ticker": "GLXY", "BTC": 6894, "Value (B)": 0.47, "mNAV": 16.90, "Strategy": "Pure treasury"},
    {"Company": "American Bitcoin Corp", "Ticker": "ABTC", "BTC": 6500, "Value (B)": 0.45, "mNAV": 2.26, "Strategy": "Pure treasury"},
    {"Company": "Next Technology Holding Inc.", "Ticker": "NXTT", "BTC": 5833, "Value (B)": 0.40, "mNAV": 0.02, "Strategy": "Pure treasury"},
    {"Company": "ProCap Financial", "Ticker": "BRR", "BTC": 5457, "Value (B)": 0.37, "mNAV": 0.00, "Strategy": "Pure treasury"},
    {"Company": "Nakamoto Inc", "Ticker": "NAKA", "BTC": 5398, "Value (B)": 0.37, "mNAV": 0.36, "Strategy": "Pure treasury"},
    {"Company": "GameStop Corp.", "Ticker": "GME", "BTC": 4710, "Value (B)": 0.32, "mNAV": 40.77, "Strategy": "Pure treasury"},
    {"Company": "Boyaa Interactive International Limited", "Ticker": "0434", "BTC": 4091, "Value (B)": 0.28, "mNAV": 0.96, "Strategy": "Pure treasury"},
    {"Company": "Empery Digital", "Ticker": "EMPD", "BTC": 4081, "Value (B)": 0.28, "mNAV": 0.62, "Strategy": "Pure treasury"},
    {"Company": "Gemini Space Station Inc", "Ticker": "GEMI", "BTC": 4002, "Value (B)": 0.27, "mNAV": 3.79, "Strategy": "Pure treasury"},
    {"Company": "OranjeBTC", "Ticker": "OBTC3", "BTC": 3723, "Value (B)": 0.26, "mNAV": 0.86, "Strategy": "Pure treasury"},
    {"Company": "Bitcoin Group SE", "Ticker": "ADE", "BTC": 3605, "Value (B)": 0.25, "mNAV": 0.72, "Strategy": "Pure treasury"},
    {"Company": "Cango Inc", "Ticker": "CANG", "BTC": 3313, "Value (B)": 0.23, "mNAV": 0.51, "Strategy": "Pure treasury"},
    {"Company": "Capital B", "Ticker": "ALCPB", "BTC": 2836, "Value (B)": 0.19, "mNAV": 1.89, "Strategy": "Pure treasury"},
    {"Company": "The Smarter Web Company PLC", "Ticker": "SWC", "BTC": 2692, "Value (B)": 0.19, "mNAV": 0.85, "Strategy": "Pure treasury"},
    {"Company": "Core Scientific", "Ticker": "CORZ", "BTC": 2537, "Value (B)": 0.17, "mNAV": 26.81, "Strategy": "Miner treasury"},
    {"Company": "DeFi Technologies", "Ticker": "DEFI", "BTC": 2452, "Value (B)": 0.17, "mNAV": 1.55, "Strategy": "Pure treasury"},
    {"Company": "Microcloud Hologram", "Ticker": "HOLO", "BTC": 2353, "Value (B)": 0.16, "mNAV": 0.19, "Strategy": "Pure treasury"},
    {"Company": "HIVE Digital Technologies", "Ticker": "HIVE", "BTC": 2201, "Value (B)": 0.15, "mNAV": 3.08, "Strategy": "Miner treasury"},
    {"Company": "DDC Enterprise Limited", "Ticker": "DDC", "BTC": 2183, "Value (B)": 0.15, "mNAV": 0.52, "Strategy": "Pure treasury"},
    {"Company": "Sequans Communications S.A.", "Ticker": "SQNS", "BTC": 2139, "Value (B)": 0.15, "mNAV": 0.54, "Strategy": "Pure treasury"},
    {"Company": "BitFuFu Inc.", "Ticker": "FUFU", "BTC": 1830, "Value (B)": 0.13, "mNAV": 3.53, "Strategy": "Miner treasury"},
    {"Company": "Bitfarms Ltd.", "Ticker": "BITF", "BTC": 1827, "Value (B)": 0.13, "mNAV": 8.98, "Strategy": "Miner treasury"},
    {"Company": "Canaan Inc.", "Ticker": "CAN", "BTC": 1778, "Value (B)": 0.12, "mNAV": 21.94, "Strategy": "Miner treasury"},
    {"Company": "NEXON Co., Ltd.", "Ticker": "3659", "BTC": 1717, "Value (B)": 0.12, "mNAV": 0.00, "Strategy": "Pure treasury"},
    {"Company": "Exodus Movement, Inc", "Ticker": "EXOD", "BTC": 1694, "Value (B)": 0.12, "mNAV": 3.16, "Strategy": "Pure treasury"},
    {"Company": "Cipher Mining", "Ticker": "CIFR", "BTC": 1500, "Value (B)": 0.10, "mNAV": 49.33, "Strategy": "Miner treasury"},
    {"Company": "Anap Holdings Inc.", "Ticker": "3189", "BTC": 1417, "Value (B)": 0.10, "mNAV": 0.62, "Strategy": "Pure treasury"},
    {"Company": "Remixpoint", "Ticker": "3825", "BTC": 1411, "Value (B)": 0.10, "mNAV": 2.05, "Strategy": "Pure treasury"},
    {"Company": "Treasury", "Ticker": "TRSR", "BTC": 1111, "Value (B)": 0.08, "mNAV": 0.00, "Strategy": "Pure treasury"},
    {"Company": "H100 Group", "Ticker": "H100", "BTC": 1051, "Value (B)": 0.07, "mNAV": 0.00, "Strategy": "Pure treasury"},
    {"Company": "ZOOZ Power", "Ticker": "ZOOZ", "BTC": 1036, "Value (B)": 0.07, "mNAV": 0.06, "Strategy": "Pure treasury"},
    {"Company": "KULR Technology Group", "Ticker": "KULR", "BTC": 1021, "Value (B)": 0.07, "mNAV": 1.49, "Strategy": "Pure treasury"},
    {"Company": "Fold Holdings Inc.", "Ticker": "FLD", "BTC": 1005, "Value (B)": 0.07, "mNAV": 0.92, "Strategy": "Pure treasury"},
    {"Company": "Nano Labs", "Ticker": "NA", "BTC": 1000, "Value (B)": 0.07, "mNAV": 0.00, "Strategy": "Pure treasury"}
]

df = pd.DataFrame(data)
df['BTC'] = pd.to_numeric(df['BTC'], errors='coerce').fillna(0)

@st.cache_data(ttl=15)
def get_live_prices(tickers):
    prices = {}
    changes = {}
    for t in tickers:
        try:
            ticker = yf.Ticker(t)
            price = ticker.info.get('currentPrice') or ticker.history(period="1d")['Close'].iloc[-1]
            change = ticker.info.get('regularMarketChangePercent') or 0
            prices[t] = round(price, 2) if price else None
            changes[t] = round(change, 2)
        except:
            prices[t] = None
            changes[t] = 0
    return prices, changes

all_tickers = df['Ticker'].tolist() + ['BTC-USD']
prices, changes = get_live_prices(all_tickers)
btc_price = prices.get('BTC-USD') or 68000

df['Stock Price ($)'] = df['Ticker'].map(prices)
df['Daily Change %'] = df['Ticker'].map(changes)
df['BTC Value (B)'] = (df['BTC'] * btc_price / 1_000_000_000).fillna(0).round(2)

# ==================== REFRESH BUTTON ====================
if st.button("🔄 Refresh Live Prices Now"):
    get_live_prices.clear()
    st.rerun()

last_updated = datetime.now().strftime("%I:%M:%S %p")
st.caption(f"Last updated: {last_updated} • Prices update every 15 seconds or click button")

st.metric("🚀 Current Bitcoin Price", f"${btc_price:,}")

st.divider()

# ==================== TABS ====================
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Holdings Table", "📈 Charts", "💎 Preferred Offerings", "🤖 Grok AI Agent", "💰 Donations"])

with tab1:
    st.subheader("Corporate Bitcoin Holdings")
    filtered = df  # No country filter anymore
    # Reorder columns exactly as requested
    display_cols = ['Company', 'Ticker', 'Stock Price ($)', 'Daily Change %', 'BTC', 'BTC Value (B)', 'mNAV', 'Strategy']
    st.dataframe(
        filtered.sort_values("BTC", ascending=False)[display_cols],
        use_container_width=True, 
        hide_index=True,
        column_config={
            "Daily Change %": st.column_config.NumberColumn(
                format="%.2f%%",
                help="Daily % change (green = up, red = down)"
            )
        }
    )

with tab2:
    st.subheader("Full Interactive Charts")
    all_chart_tickers = ['BTC-USD'] + df['Ticker'].tolist()
    selected_ticker = st.selectbox("Choose ticker", all_chart_tickers, index=0)
    period = st.selectbox("Time period", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)
    if st.button("Load Full Chart with Indicators"):
        with st.spinner("Fetching real-time data..."):
            hist = yf.download(selected_ticker, period=period, progress=False)
            hist['SMA50'] = hist['Close'].rolling(50).mean()
            hist['SMA200'] = hist['Close'].rolling(200).mean()
            delta = hist['Close'].diff()
            gain = delta.where(delta > 0, 0).rolling(14).mean()
            loss = -delta.where(delta < 0, 0).rolling(14).mean()
            rs = gain / loss
            hist['RSI'] = 100 - 100 / (1 + rs)
            fig = make_subplots(rows=2, cols=1, shared_xaxes=True, row_heights=[0.7, 0.3])
            fig.add_trace(go.Candlestick(x=hist.index, open=hist['Open'], high=hist['High'], low=hist['Low'], close=hist['Close'], name="Price"), row=1, col=1)
            fig.add_trace(go.Scatter(x=hist.index, y=hist['SMA50'], name="SMA 50", line=dict(color='orange')), row=1, col=1)
            fig.add_trace(go.Scatter(x=hist.index, y=hist['SMA200'], name="SMA 200", line=dict(color='blue')), row=1, col=1)
            fig.add_trace(go.Scatter(x=hist.index, y=hist['RSI'], name="RSI", line=dict(color='purple')), row=2, col=1)
            fig.add_hline(y=30, row=2, col=1, line_dash="dash", line_color="green")
            fig.add_hline(y=70, row=2, col=1, line_dash="dash", line_color="red")
            fig.update_layout(height=700, xaxis_rangeslider_visible=False)
            st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Preferred Stock “Bitcoin Bond Market” Tracker")
    preferred = [
        {"Security": "STRC (Stretch)", "Yield": "11.50%", "Type": "Perpetual Preferred", "Status": "Monthly dividend hike #7", "Note": "Trading near $100 par"},
        {"Security": "STRF", "Yield": "Variable", "Type": "Perpetual Preferred", "Status": "Active", "Note": "Lower volatility capital raise"},
        {"Security": "STRK", "Yield": "Variable", "Type": "Perpetual Preferred", "Status": "Active", "Note": "Bitcoin-backed credit"},
        {"Security": "STRD", "Yield": "Variable", "Type": "Perpetual Preferred", "Status": "Active", "Note": ""},
        {"Security": "STRE", "Yield": "Variable", "Type": "Perpetual Preferred", "Status": "Active", "Note": ""},
        {"Security": "SATA (Strive)", "Yield": "12.5% variable", "Type": "Perpetual Preferred", "Status": "Active / Near par", "Note": "Second only to Strategy"},
    ]
    st.dataframe(pd.DataFrame(preferred), use_container_width=True, hide_index=True)

with tab4:
    st.subheader("🤖 Grok AI Alpha Agent")
    company = st.selectbox("Pick a company", df["Company"])
    if st.button("Run Grok Analysis"):
        row = df[df["Company"] == company].iloc[0]
        prompt = f"""You are Grok, the Bitcoin Alpha Terminal Agent.
Company: {row['Company']} ({row['Ticker']})
BTC Holdings: {row['BTC']:,}
Live BTC Value: ${row['BTC Value (B)']}B
Stock Price: ${row['Stock Price ($)']}
mNAV: {row['mNAV']}

Output in 4 bullets:
1. Next 30-day treasury move prediction
2. Risk level (1-10)
3. Preferred offering opportunity
4. Alert for user"""
        if xai_key:
            try:
                client = OpenAI(api_key=xai_key, base_url="https://api.x.ai/v1")
                response = client.chat.completions.create(model="grok-beta", messages=[{"role": "user", "content": prompt}])
                st.success(response.choices[0].message.content)
            except:
                st.info("**Demo**: High probability of continued accumulation. Risk 4/10.")
        else:
            st.warning("Enter xAI key in sidebar for real Grok analysis")

with tab5:
    st.subheader("💰 Support the Bitcoin Alpha Terminal")
    st.write("100% Free forever. Send any BTC directly:")
    st.code(DONATION_ADDRESS)
    st.caption("🇺🇸 Every sat helps keep this terminal growing from the United States")

st.divider()
st.caption("v6.0 • Live prices update every 15 seconds or click Refresh button • Built in the United States 🇺🇸")
