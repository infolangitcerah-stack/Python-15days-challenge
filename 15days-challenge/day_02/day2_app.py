import pandas as pd
import streamlit as st

# ------------------------------
# HEADER
# ------------------------------
st.markdown(
    """
    <h1 style="text-align:center; color:#4CAF50;">💰 Fair Expense Splitter</h1>
    <h3 style="text-align:center; color:#555;">Social Eagle GenAI Architect</h3>
    <h4 style="text-align:center; color:#888;">15 Days Python Challenge - Day 2 Assignment</h4>
    <h4 style="text-align:center; color:#FF5722;">👨‍🏫 Coach Dom</h4>
    <hr>
    """,
    unsafe_allow_html=True,
)

st.write(
    "🎉 Welcome to the **dynamic expense splitter**. "
    "Easily calculate and visualize how expenses should be shared. "
    "Switch between tabs for **inputs, results, charts, and settlements** 🚀"
)

# ------------------------------
# MAIN APP WITH TABS
# ------------------------------
tab1, tab2, tab3, tab4 = st.tabs(["📝 Input", "📊 Results", "📈 Charts", "🤝 Settlement"])

# Shared state
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()
    st.session_state.total_expense = 0.0
    st.session_state.per_person = 0.0

# ------------------------------
# TAB 1: INPUT
# ------------------------------
with tab1:
    st.subheader("Step 1: Enter Participants and Expenses")

    num_people = st.number_input("How many participants?", min_value=2, max_value=10, value=3)

    participants = []
    expenses = []

    for i in range(num_people):
        col1, col2 = st.columns([2, 1])
        with col1:
            name = st.text_input(f"Name of participant {i+1}", key=f"name_{i}")
        with col2:
            expense = st.number_input(
                f"Expense by {name if name else 'Person ' + str(i+1)}",
                min_value=0.0,
                value=0.0,
                step=0.01,  # allow decimals
                format="%.2f",  # show only 2 decimals
                key=f"expense_{i}",
            )
        participants.append(name if name else f"Person {i+1}")
        expenses.append(expense)

    if st.button("✅ Save & Calculate"):
        df = pd.DataFrame({"Participant": participants, "Expense": expenses})
        total_expense = df["Expense"].sum()
        per_person = total_expense / num_people
        df["Balance"] = df["Expense"] - per_person

        st.session_state.df = df
        st.session_state.total_expense = total_expense
        st.session_state.per_person = per_person

        st.success("✅ Data saved! Switch tabs to see results 👉")

# ------------------------------
# TAB 2: RESULTS
# ------------------------------
with tab2:
    st.subheader("📊 Expense Summary")
    if not st.session_state.df.empty:
        st.success(
            f"🎉 Total Expense: **RM {st.session_state.total_expense:.2f}** "
            f"| Each person should pay: **RM {st.session_state.per_person:.2f}**"
        )

        # Format table with 2 decimals
        styled_df = st.session_state.df.style.format(
            {"Expense": "{:.2f}", "Balance": "{:.2f}"}
        ).background_gradient(cmap="YlGnBu")

        st.dataframe(styled_df, use_container_width=True)
    else:
        st.warning("⚠️ No data yet. Please enter details in the **Input** tab.")

# ------------------------------
# TAB 3: CHARTS
# ------------------------------
with tab3:
    st.subheader("📈 Visualize Expenses")
    if not st.session_state.df.empty:
        st.bar_chart(st.session_state.df.set_index("Participant")["Expense"])
        st.line_chart(st.session_state.df.set_index("Participant")["Expense"])
    else:
        st.info("ℹ️ No chart available yet. Please fill data in the **Input** tab.")

# ------------------------------
# TAB 4: SETTLEMENT
# ------------------------------
with tab4:
    st.subheader("🤝 Who Pays Whom")
    if not st.session_state.df.empty:
        creditors = st.session_state.df[st.session_state.df["Balance"] > 0].to_dict("records")
        debtors = st.session_state.df[st.session_state.df["Balance"] < 0].to_dict("records")

        if not creditors or not debtors:
            st.info("🎉 No settlements needed. Everyone paid equally!")
        else:
            for debtor in debtors:
                amount_owed = -debtor["Balance"]
                for creditor in creditors:
                    if creditor["Balance"] <= 0:
                        continue
                    payment = min(amount_owed, creditor["Balance"])
                    if payment > 0:
                        st.write(
                            f"👉 **{debtor['Participant']}** pays **RM {payment:.2f}** "
                            f"to **{creditor['Participant']}**"
                        )
                        amount_owed -= payment
                        creditor["Balance"] -= payment
                    if amount_owed <= 0:
                        break
    else:
        st.warning("⚠️ Please add data first in the **Input** tab.")

# ------------------------------
# FOOTER
# ------------------------------
st.markdown(
    """
    <hr>
    <p style="text-align:center; color:#888;">
    🌟 Built with ❤️ using Streamlit <br>
    Part of the <b>Social Eagle GenAI Architect - 15 Days Python Challenge</b>
    </p>
    """,
    unsafe_allow_html=True,
)
