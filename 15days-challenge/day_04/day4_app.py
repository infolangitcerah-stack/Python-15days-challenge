import plotly.graph_objects as go
import streamlit as st

# -------------------------------------------------
# Contexts
# Social Eagle GenAI Architect
# 15 Days Python Challenge
# Day 4 Assignment
# Coach Dom
# -------------------------------------------------

st.set_page_config(page_title="BMI Calculator 🏋️", page_icon="🏋️")

# ------------------------------
# App Title
# ------------------------------
st.title("🏋️ BMI Calculator")
st.markdown("**15 Days Python Challenge | Day 4 Assignment | Coach Dom**")
st.write("Welcome! Enter your details to calculate your BMI.")

# ------------------------------
# Input Section
# ------------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("🎂 Age (years):", min_value=5, max_value=120, step=1)
    sex = st.radio("⚧ Sex:", ["Male", "Female"], horizontal=True)

with col2:
    height = st.number_input("📏 Height (cm):", min_value=50.0, max_value=250.0, step=0.1)
    weight = st.number_input("⚖️ Weight (kg):", min_value=10.0, max_value=300.0, step=0.1)

# ------------------------------
# Button Action
# ------------------------------
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        # BMI formula
        bmi = weight / ((height / 100) ** 2)
        bmi_value = round(bmi, 1)

        # Determine category & recommendation
        if bmi < 18.5:
            category = "Underweight 😟"
            color = "orange"
            recommendation = "🍲 Eat more nutrient-rich foods and consult a doctor if necessary."
        elif 18.5 <= bmi < 25:
            category = "Normal ✅"
            color = "green"
            recommendation = (
                "💪 Keep up your healthy lifestyle with balanced diet and regular exercise."
            )
        else:
            category = "Overweight ⚠️"
            color = "red"
            recommendation = "🏃 Consider healthier eating habits and more physical activity."

        # -------------------------
        # Results Section
        # -------------------------
        st.subheader("📋 Your Results")
        st.markdown(f"**Age:** {age} | **Sex:** {sex}")
        st.markdown(f"**BMI Value:** `{bmi_value}`")
        st.markdown(
            f"<div style='color:{color}; font-size:26px; font-weight:bold;'>Category: {category}</div>",
            unsafe_allow_html=True,
        )

        # -------------------------
        # Compact Speedometer Gauge with Plotly
        # -------------------------
        st.subheader("📊 BMI Speedometer")

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=bmi_value,
                title={"text": "BMI", "font": {"size": 20}},
                gauge={
                    "axis": {"range": [0, 40], "tickwidth": 1, "tickcolor": "darkgray"},
                    "bar": {"color": "black", "thickness": 0.25},
                    "steps": [
                        {"range": [0, 18.5], "color": "orange"},
                        {"range": [18.5, 25], "color": "green"},
                        {"range": [25, 40], "color": "red"},
                    ],
                    "threshold": {
                        "line": {"color": "black", "width": 4},
                        "thickness": 0.75,
                        "value": bmi_value,
                    },
                },
            )
        )

        # Compact layout
        fig.update_layout(
            autosize=False, width=400, height=250, margin=dict(l=30, r=30, t=50, b=30)
        )

        st.plotly_chart(fig, use_container_width=False)

        # -------------------------
        # Interpretation
        # -------------------------
        st.subheader("📑 BMI Categories")
        st.markdown(
            """
        - 🟠 **Underweight:** BMI < 18.5  
        - 🟢 **Normal:** 18.5 – 24.9  
        - 🔴 **Overweight:** BMI ≥ 25  
        """
        )

        # -------------------------
        # Health Recommendation
        # -------------------------
        st.subheader("💡 Health Recommendation")
        st.info(recommendation)

    else:
        st.error("⚠️ Please enter valid height and weight values.")
