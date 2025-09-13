import streamlit as st

# ------------------------------
# HEADER
# ------------------------------
st.markdown(
    """
    <h1 style="text-align:center; color:#1E88E5;">
        🔢 Simple & Fun Calculator
    </h1>
    <h3 style="text-align:center; color:#43A047;">
        Social Eagle GenAI Architect - 15 Days Python Challenge
    </h3>
    <h4 style="text-align:center; color:#E65100;">
        Day 3 Assignment - 👨‍🏫 Coach Dom
    </h4>
    <hr style="border: 1px solid #1E88E5;">
    """,
    unsafe_allow_html=True,
)

st.write("🎉 Welcome to the **Colorful Calculator**! Enter two numbers and pick an operation ➕➖✖️➗")

# ------------------------------
# CALCULATOR INPUTS
# ------------------------------
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", min_value=0, max_value=99999, step=1, format="%d")
with col2:
    num2 = st.number_input("Enter second number", min_value=0, max_value=99999, step=1, format="%d")

operation = st.radio(
    "Choose operation",
    ("➕ Addition", "➖ Subtraction", "✖️ Multiplication", "➗ Division"),
    horizontal=True
)

# ------------------------------
# CALCULATION
# ------------------------------
result = None
if st.button("✅ Calculate"):
    if operation.startswith("➕"):
        result = num1 + num2
    elif operation.startswith("➖"):
        result = num1 - num2
    elif operation.startswith("✖️"):
        result = num1 * num2
    elif operation.startswith("➗"):
        if num2 != 0:
            result = round(num1 / num2, 2)  # 2 decimals
        else:
            st.error("❌ Cannot divide by zero!")

# ------------------------------
# OUTPUT
# ------------------------------
if result is not None:
    st.markdown(
        f"""
        <h2 style="color:#D32F2F; text-align:center;">
            🎉 Result: {result}
        </h2>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------
# FOOTER
# ------------------------------
st.markdown(
    """
    <hr style="border: 1px solid #43A047;">
    <p style="text-align:center; color:#666;">
    🌟 Built with ❤️ using Streamlit <br>
    A fun assignment in the <b>15 Days Python Challenge</b>
    </p>
    """,
    unsafe_allow_html=True,
)
