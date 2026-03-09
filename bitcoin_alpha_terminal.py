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

# ==================== LIVE DATA — ALL 50+ Companies ====================
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
    {"Company": "Tesla, Inc.", "Ticker": "TSLA", "Country": "US", "BTC": 11509, "Value (B)": 0.79, "mNAV": 0.00, "Strategy": "Pure treasury"},
    {"Company": "Trump Media & Technology Group Corp.", "Ticker": "DJT", "Country": "US", "BTC": 9542, "Value (B)": 0.65, "mNAV": 3.70, "Strategy": "Pure treasury"},
    {"Company": "Block, Inc.", "Ticker": "XYZ", "Country": "US", "BTC": 8883, "Value (B)": 0.61, "mNAV": 65.84, "Strategy": "Pure treasury"},
    {"Company": "GD Culture Group", "Ticker": "GDC", "Country": "US", "BTC": 7500, "Value (B)": 0.51, "mNAV": 0.47, "Strategy": "Pure treasury"},
    {"Company": "Galaxy Digital Holdings Ltd", "Ticker": "GLXY", "Country": "US", "BTC": 6894, "Value (B)": 0.47, "mNAV": 16.90, "Strategy": "Pure treasury"},
    {"Company": "American Bitcoin Corp", "Ticker": "ABTC", "Country": "US", "BTC": 6500, "Value (B)": 0.45, "mNAV": 2.26, "Strategy": "Pure treasury"},
    {"Company": "Next Technology Holding Inc.", "Ticker": "NXTT", "Country": "CN", "BTC": 5833, "Value (B)": 0.40, "mNAV": 0.02, "Strategy": "Pure treasury"},
    {"Company": "ProCap Financial", "Ticker": "BRR", "Country": "US", "BTC": 5457, "Value (B)": 0.37, "mNAV": 0.00, "Strategy": "Pure treasury"},
    {"Company": "Nakamoto Inc", "Ticker": "NAKA", "Country": "US", "BTC": 5398, "Value (B)": 0.37, "mNAV": 0.36, "Strategy": "Pure treasury"},
    {"Company": "GameStop Corp.", "Ticker": "GME", "Country": "US", "BTC": 4710, "Value (B)": 0.32, "mNAV": 40.77, "Strategy": "Pure treasury"},
    {"Company": "Boyaa Interactive International Limited", "Ticker": "0434", "Country": "HK", "BTC": 4091, "Value (B)": 0.28, "mNAV": 0.96, "Strategy": "Pure treasury"},
    {"Company": "Empery Digital", "Ticker": "EMPD", "Country": "US", "BTC": 4081, "Value (B)": 0.28, "mNAV": 0.62, "Strategy": "Pure treasury"},
    {"Company": "Gemini Space Station Inc", "Ticker": "GEMI", "Country": "US", "BTC": 4002, "Value (B)": 0.27, "mNAV": 3.79, "Strategy": "Pure treasury"},
    {"Company": "OranjeBTC", "Ticker": "OBTC3", "Country": "BR", "BTC": 3723, "Value (B)": 0.26, "mNAV": 0.86, "Strategy": "Pure treasury"},
    {"Company": "Bitcoin Group SE", "Ticker": "ADE", "Country": "DE", "BTC": 3605, "Value (B)": 0.25, "mNAV": 0.72, "Strategy": "Pure treasury"},
    {"Company": "Cango Inc", "Ticker": "CANG", "Country": "US", "BTC": 3313, "Value (B)": 0.23, "mNAV": 0.51, "Strategy": "Pure treasury"},
    {"Company": "Capital B", "Ticker": "ALCPB", "Country": "FR", "BTC": 2836, "Value (B)": 0.19, "mNAV": 1.89, "Strategy": "Pure treasury"},
    {"Company": "The Smarter Web Company PLC", "Ticker": "SWC", "Country": "GB", "BTC": 2692, "Value (B)": 0.19, "mNAV": 0.85, "Strategy": "Pure treasury"},
    {"Company": "Core Scientific", "Ticker": "CORZ", "Country": "US", "BTC": 2537, "Value (B)": 0.17, "mNAV": 26.81, "Strategy": "Miner treasury"},
    {"Company": "DeFi Technologies", "Ticker": "DEFI", "Country": "CA", "BTC": 2452, "Value (B)": 0.17, "mNAV": 1.55, "Strategy": "Pure treasury"},
    {"Company": "Microcloud Hologram", "Ticker": "HOLO", "Country": "KY", "BTC": 2353, "Value (B)": 0.16, "mNAV": 0.19, "Strategy": "Pure treasury"},
    {"Company": "HIVE Digital Technologies", "Ticker": "HIVE", "Country": "CA", "BTC": 2201, "Value (B)": 0.15, "mNAV": 3.08, "Strategy": "Miner treasury"},
    {"Company": "DDC Enterprise Limited", "Ticker": "DDC", "Country": "US", "BTC": 2183, "Value (B)": 0.15, "mNAV": 0.52, "Strategy": "Pure treasury"},
    {"Company": "Sequans Communications S.A.", "Ticker": "SQNS", "Country": "FR", "BTC": 2139, "Value (B)": 0.15, "mNAV": 0.54, "Strategy": "Pure treasury"},
    {"Company": "BitFuFu Inc.", "Ticker": "FUFU", "Country": "SG", "BTC": 1830, "Value (B)": 0.13, "mNAV": 3.53, "Strategy": "Miner treasury"},
    {"Company": "Bitfarms Ltd.", "Ticker": "BITF", "Country": "CA", "BTC": 1827, "Value (B)": 0.13, "mNAV": 8.98, "Strategy": "Miner treasury"},
    {"Company": "Canaan Inc.", "Ticker": "CAN", "Country": "SG", "BTC": 1778, "Value (B)": 0.12, "mNAV": 21.94, "Strategy": "Miner treasury"},
    {"Company": "NEXON Co., Ltd.", "Ticker": "3659", "Country": "JP", "BTC": 1717, "Value (B)": 0.12, "mNAV": 0.00, "Strategy": "Pure treasury"},
    {"Company": "Exodus Movement, Inc", "Ticker": "EXOD", "Country": "US", "BTC": 1694, "Value (B)": 0.12, "mNAV": 3.16, "Strategy": "Pure treasury"},
    {"Company": "Cipher Mining", "Ticker": "CIFR", "Country": "US", "BTC": 1500, "Value (B)": 0.10, "mNAV": 49.33, "Strategy": "Miner treasury"},
    {"Company": "Anap Holdings Inc.", "Ticker": "3189", "Country": "JP", "BTC": 1417, "Value (B)": 0.10, "mNAV": 0.62, "Strategy": "Pure treasury"},
    {"Company": "Remixpoint", "Ticker": "3825", "Country": "JP", "BTC": 1411, "Value (B)": 0.10, "mNAV": 2.05, "Strategy": "Pure treasury"},
    {"Company": "Treasury", "Ticker": "TRSR", "Country": "NL", "BTC": 1111, "Value (B)": 0.08, "mNAV": 0.00, "Strategy": "Pure treasury"},
    {"Company": "H100 Group", "Ticker": "H100", "Country": "SE", "BTC": 1051, "Value (B)": 0.07, "mNAV": 0.00, "Strategy": "Pure treasury"},
    {"Company": "ZOOZ Power", "Ticker": "ZOOZ", "Country": "IL", "BTC": 1036, "Value (B)": 0.07, "mNAV": 0.06, "Strategy": "Pure treasury"},
    {"Company": "KULR Technology Group", "Ticker": "KULR", "Country": "US", "BTC": 1021, "Value (B)": 0.07, "mNAV": 1.49, "Strategy": "Pure treasury"},
    {"Company": "Fold Holdings Inc.", "Ticker": "FLD", "Country": "US", "BTC": 1005, "Value (B)": 0.07, "mNAV": 0.92, "Strategy": "Pure treasury"},
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

# ==================== TABS ====================
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Holdings Table", "📈 Charts", "💎 Preferred Offerings", "🤖 Grok AI Agent", "💰 Donations"])

with tab1:
    st.subheader("Corporate Bitcoin Holdings")
    country_filter = st.selectbox("Filter by Country", ["All"] + sorted(df["Country"].unique()))
    filtered = df if country_filter == "All" else df[df["Country"] == country_filter]
    st.dataframe(
        filtered.sort_values("BTC", ascending=False)[['Company', 'Ticker', 'Country', 'BTC', 'Stock Price ($)', 'BTC Value (B)', 'mNAV', 'Strategy']],
        use_container_width=True, hide_index=True
    )
    st.caption("Stock prices update live • Scroll for all 50+ companies")

with tab2:
    st.subheader("Full Interactive Charts")
    all_chart_tickers = ['BTC-USD'] + df['Ticker'].tolist()
    selected_ticker = st.selectbox("Choose ticker", all_chart_tickers, index=0)
    period = st.selectbox("Time period", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3)
    if st.button("Load Full Chart with Indicators"):
        with st.spinner("Fetching real-time data + technical indicators..."):
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
        {"Security": "SATA (Strive)", "Yield": "12.5% variable", "Type": "Perpetual Preferred", "Status": "Active / Near par", "Note": "Second only to Strategy – funds BTC buys + debt retirement"},
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
    st.subheader("💰 Support the Bitcoin AI Alpha Terminal")
    st.write("100% Free forever. Send any BTC directly:")
    st.code(DONATION_ADDRESS)
    st.caption("🇺🇸 Every sat helps keep this terminal growing from the United States")

st.divider()
st.caption("v5.0 • Clean landing page • Live BTC price • Full data restored • Built in the United States 🇺🇸")
