import streamlit as st
import plotly.graph_objects as go

# ======= Page Config =======
st.set_page_config(page_title="Dom's Unit Converter", layout="centered")

# ======= Header Section =======
st.markdown(
    """
    <div style="text-align:center; padding:20px; 
                background: linear-gradient(90deg, #4facfe 0%, #6a11cb 100%);
                border-radius: 12px; color: white;">
        <h2>🌟 Social Eagle GenAI Architect 🌟</h2>
        <h3>🚀 15 Days Python Challenge</h3>
        <h4>📅 Day 5 Assignment</h4>
        <h3>👨‍🏫 Coach Dom</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ======= Converter Section =======
st.title("🔄 Unit Converter")
converter_type = st.selectbox(
    "Choose what you want to convert:",
    ["Currency 💵", "Temperature 🌡️", "Length 📏", "Weight ⚖️"]
)

# --- Helper: Create Gauge Chart ---
def gauge_chart(value, title, max_value):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={"text": title},
        gauge={
            "axis": {"range": [None, max_value]},
            "bar": {"color": "limegreen"},
            "bgcolor": "white",
            "borderwidth": 2,
            "bordercolor": "gray"
        }
    ))
    fig.update_layout(height=250, margin=dict(t=20, b=20, l=20, r=20))
    return fig

# ======= Currency =======
if converter_type == "Currency 💵":
    st.subheader("💵 Currency Converter (RM → Other Currencies)")
    col1, col2 = st.columns(2)

    with col1:
        amount = st.number_input("Amount in RM", min_value=0.0, value=10.0, key="rm")

    with col2:
        currency = st.selectbox("Convert to:", ["USD", "GBP", "EUR", "INR"])

        rates = {"USD": 0.21, "GBP": 0.17, "EUR": 0.19, "INR": 17.4}
        converted = round(amount * rates[currency], 1)

        st.metric(label=f"Converted to {currency}", value=f"{converted:.1f} {currency}")
        st.plotly_chart(gauge_chart(converted, f"{currency} Value", converted * 2 if converted > 0 else 1))

# ======= Temperature =======
elif converter_type == "Temperature 🌡️":
    st.subheader("🌡️ Temperature Converter")
    col1, col2 = st.columns(2)

    with col1:
        temp_c = st.number_input("Temperature in °C", value=25.0, key="temp_c")

    with col2:
        scale = st.selectbox("Convert to:", ["°F", "K"])
        if scale == "°F":
            result = round(temp_c * 9/5 + 32, 1)
            max_val = 120
        else:
            result = round(temp_c + 273.15, 1)
            max_val = 400

        st.metric(label=f"Converted to {scale}", value=f"{result:.1f} {scale}")
        st.plotly_chart(gauge_chart(result, f"{scale} Scale", max_val))

# ======= Length =======
elif converter_type == "Length 📏":
    st.subheader("📏 Length Converter (cm → Other Units)")
    col1, col2 = st.columns(2)

    with col1:
        length_cm = st.number_input("Length in cm", value=100.0, key="len_cm")

    with col2:
        unit = st.selectbox("Convert to:", ["Meters (m)", "Inches (in)", "Feet (ft)"])
        if unit == "Meters (m)":
            result = round(length_cm / 100, 1)
            symbol, max_val = "m", 10
        elif unit == "Inches (in)":
            result = round(length_cm / 2.54, 1)
            symbol, max_val = "in", 100
        else:
            result = round(length_cm / 30.48, 1)
            symbol, max_val = "ft", 50

        st.metric(label=f"Converted to {unit}", value=f"{result:.1f} {symbol}")
        st.plotly_chart(gauge_chart(result, f"{unit}", max_val))

# ======= Weight =======
elif converter_type == "Weight ⚖️":
    st.subheader("⚖️ Weight Converter (kg → Other Units)")
    col1, col2 = st.columns(2)

    with col1:
        weight_kg = st.number_input("Weight in kg", value=50.0, key="weight_kg")

    with col2:
        unit = st.selectbox("Convert to:", ["Grams (g)", "Pounds (lbs)", "Ounces (oz)"])
        if unit == "Grams (g)":
            result = round(weight_kg * 1000, 1)
            symbol, max_val = "g", 100000
        elif unit == "Pounds (lbs)":
            result = round(weight_kg * 2.20462, 1)
            symbol, max_val = "lbs", 500
        else:
            result = round(weight_kg * 35.274, 1)
            symbol, max_val = "oz", 1000

        st.metric(label=f"Converted to {unit}", value=f"{result:.1f} {symbol}")
        st.plotly_chart(gauge_chart(result, f"{unit}", max_val))



