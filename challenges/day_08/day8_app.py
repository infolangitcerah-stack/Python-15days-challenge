import streamlit as st

# ----------------------------
# Social Eagle GenAI Architect | 15 Days Python Challenge
# Day 8 Assignment – Currency Converter 💱
# Coach Dom
# ----------------------------

st.set_page_config(page_title="Currency Converter 💱", page_icon="💱", layout="centered")

# Custom CSS for darker font
st.markdown(
    """
    <style>
        body, p, div, label, .stMarkdown, .stSelectbox, .stNumberInput {
            color: #111111 !important;  /* Darker black */
            font-weight: 500;
        }
        h1, h2, h3 {
            color: #00e6e6 !important;  /* Futuristic aqua for titles */
        }
        .stSuccess {
            font-size: 18px !important;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown(
    """
    <h1 style='text-align: center;'>
        💱 Dom's Currency Converter
    </h1>
    <p style='text-align: center; color:#444444;'>
        Convert between INR, USD, EUR, GBP with static rates <br>
        <b>Day 8 | Social Eagle GenAI Architect | 15 Days Python Challenge</b>
    </p>
    """,
    unsafe_allow_html=True
)

# Static conversion rates (example only)
rates = {
    "USD": 1.00,      # Base
    "INR": 83.00,     # 1 USD = 83 INR
    "EUR": 0.92,      # 1 USD = 0.92 EUR
    "GBP": 0.80       # 1 USD = 0.80 GBP
}

currencies = list(rates.keys())

# User input
col1, col2 = st.columns(2)
with col1:
    from_currency = st.selectbox("From Currency", currencies, index=0)
with col2:
    to_currency = st.selectbox("To Currency", currencies, index=1)

amount = st.number_input("Enter amount", min_value=0.0, format="%.2f")

# Conversion
if amount:
    usd_amount = amount / rates[from_currency]   # convert to USD first
    converted = usd_amount * rates[to_currency]
    st.success(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center; color:#666666;'>
        🚀 Built with Streamlit | Styled for a Futuristic Look ✨
    </p>
    """,
    unsafe_allow_html=True
)
