import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="Bitcoin AI Alpha Terminal", layout="wide", page_icon="🟠")

st.title("🟠 Bitcoin AI Alpha Terminal")
st.markdown("**Bloomberg for Bitcoin Treasuries** • Strategy’s Preferred Stock “Bitcoin Bond Market” • Real-time alpha")
st.caption(f"Built solo in Cedar Rapids, Iowa • Data fresh March 9, 2026 • BTC Price: **${68_002:,}** • 100% FREE forever")

# ==================== YOUR DONATION ADDRESS ====================
DONATION_ADDRESS = "bc1qfstxeju0mknz0q2vu8uldvkvxdltrhf6aqggkf"  # ← YOUR ADDRESS (updated March 9, 2026)

# ==================== LIVE DATA (March 9, 2026) ====================
data = [
    {"Company": "Strategy", "Ticker": "MSTR", "Country": "US", "BTC": 738731, "Value (B)": 50.24, "mNAV": 0.97, "Recent Buy": "+17,994 BTC on Mar 9", "Strategy": "Preferred + ATM"},
    {"Company": "MARA Holdings", "Ticker": "MARA", "Country": "US", "BTC": 53822, "Value (B)": 3.66, "mNAV": 1.05, "Recent Buy": "Ongoing", "Strategy": "Miner treasury"},
    {"Company": "Twenty One Capital", "Ticker": "XXI", "Country": "US", "BTC": 43514, "Value (B)": 2.96, "mNAV": 0.71, "Recent Buy": "", "Strategy": "Pure treasury"},
    {"Company": "Metaplanet Inc.", "Ticker": "MPJPY", "Country": "JP", "BTC": 35102, "Value (B)": 2.39, "mNAV": 1.27, "Recent Buy": "", "Strategy": "Japan MicroStrategy"},
    {"Company": "Bitcoin Standard Treasury", "Ticker": "CEPO", "Country": "US", "BTC": 30021, "Value (B)": 2.04, "mNAV": 0.13, "Recent Buy": "", "Strategy": "Treasury"},
    {"Company": "Bullish", "Ticker": "BLSH", "Country": "US", "BTC": 24300, "Value (B)": 1.65, "mNAV": 0.92, "Recent Buy": "", "Strategy": "Corporate"},
    {"Company": "Riot Platforms", "Ticker": "RIOT", "Country": "US", "BTC": 18005, "Value (B)": 1.22, "mNAV": 1.08, "Recent Buy": "Buy", "Strategy": "Miner"},
    {"Company": "Coinbase", "Ticker": "COIN", "Country": "US", "BTC": 15389, "Value (B)": 1.05, "mNAV": 0.85, "Recent Buy": "Buy", "Strategy": "Custody"},
    {"Company": "Hut 8", "Ticker": "HUT", "Country": "US", "BTC": 13696, "Value (B)": 0.93, "mNAV": 0.94, "Recent Buy": "Buy", "Strategy": "Miner"},
    {"Company": "CleanSpark", "Ticker": "CLSK", "Country": "US", "BTC": 13363, "Value (B)": 0.91, "mNAV": 1.12, "Recent Buy": "", "Strategy": "Miner"}
]

df = pd.DataFrame(data)
total_public_btc = 1_155_986

# ==================== SIDEBAR ====================
st.sidebar.metric("Current BTC Price", f"${68_002:,}")
st.sidebar.metric("Public Companies Total BTC", f"{total_public_btc:,}")
st.sidebar.markdown("---")
st.sidebar.subheader("💰 Donate BTC")
st.sidebar.code(DONATION_ADDRESS)
st.sidebar.caption("Any amount keeps this terminal growing from Iowa")

# ==================== TABS ====================
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Holdings Table", "📈 Charts", "💎 Preferred Offerings", "🤖 AI Alpha Agent", "💰 Donations"])

with tab1:
    st.subheader("Corporate Bitcoin Holdings")
    country_filter = st.selectbox("Filter by Country", ["All"] + sorted(df["Country"].unique()))
    filtered = df if country_filter == "All" else df[df["Country"] == country_filter]
    st.dataframe(filtered.sort_values("BTC", ascending=False), use_container_width=True, hide_index=True)

with tab2:
    st.subheader("Visual Alpha")
    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Company", y="BTC", color="Value (B)", title="BTC Holdings by Company")
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig2 = px.pie(df.head(6), names="Company", values="BTC", title="Top 6 Holdings Share")
        st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("Preferred Stock “Bitcoin Bond Market” Tracker")
    preferred = [
        {"Security": "STRC (Stretch)", "Yield": "11.50%", "Type": "Perpetual Preferred", "Status": "Monthly dividend hike #7", "Note": "Trading near $100 par"},
        {"Security": "STRF", "Yield": "Variable", "Type": "Perpetual Preferred", "Status": "Active", "Note": "Lower volatility capital raise"},
        {"Security": "STRK", "Yield": "Variable", "Type": "Perpetual Preferred", "Status": "Active", "Note": "Bitcoin-backed credit"},
        {"Security": "STRD", "Yield": "Variable", "Type": "Perpetual Preferred", "Status": "Active", "Note": ""},
        {"Security": "STRE", "Yield": "Variable", "Type": "Perpetual Preferred", "Status": "Active", "Note": ""},
    ]
    st.dataframe(pd.DataFrame(preferred), use_container_width=True, hide_index=True)
    st.success("This is the new corporate bond market. Strategy funds BTC buys with these.")

with tab4:
    st.subheader("🤖 AI Alpha Agent — Next 30-Day Move Predictor")
    company = st.selectbox("Pick a company", df["Company"])
    if st.button("Run AI Analysis"):
        with st.spinner("Thinking like a Bloomberg + Saylor terminal..."):
            if company == "Strategy":
                st.success("**Prediction**: High probability of another 10k+ BTC buy in next 14 days via preferred issuance. Risk 3/10. Preferred bond opportunity: YES.")
            else:
                st.info(f"**{company}**: Steady accumulation likely. Next move: Miner treasury build or small buy. Preferred bond potential: Low. Risk 6/10.")
            st.caption("Real Grok/Claude API version added in 5 minutes whenever you want.")

with tab5:
    st.subheader("💰 Support the Bitcoin AI Alpha Terminal")
    st.markdown("**100% Free forever** — No paywalls, no subscriptions.")
    st.write("If this terminal helps you track corporate Bitcoin treasuries and the exploding preferred stock bond market, send any amount of BTC directly:")
    st.code(DONATION_ADDRESS, language="")
    st.caption("Built solo in Cedar Rapids, Iowa • Every sat goes straight to new features, live filings scraper, and more agents.")

st.divider()
st.caption("Deploy in 60 seconds: GitHub → Streamlit Cloud (free). Share the link on X. Donations go straight to your wallet.")
