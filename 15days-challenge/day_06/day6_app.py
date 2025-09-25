import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# HEADER
# ------------------------------
st.markdown(
    """
    <h1 style="text-align:center; color:#00BFFF;">💧 Water Intake Tracker</h1>
    <h3 style="text-align:center; color:#555;">Social Eagle GenAI Architect</h3>
    <h4 style="text-align:center; color:#888;">15 Days Python Challenge - Day 6 Assignment</h4>
    <h4 style="text-align:center; color:#FF5722;">👨‍🏫 Coach Dom</h4>
    <hr>
    """,
    unsafe_allow_html=True,
)

# ------------------------------
# SETTINGS
# ------------------------------
DAILY_GOAL = 3.0  # liters/day
WEEKLY_GOAL = DAILY_GOAL * 7

days = [
    "Sunday 7.9.25",
    "Monday 8.9.25",
    "Tuesday 9.9.25",
    "Wednesday 10.9.25",
    "Thursday 11.9.25",
    "Friday 12.9.25",
    "Saturday 13.9.25",
]

# Initialize session state for intake values
if "intake" not in st.session_state:
    st.session_state.intake = [0.0] * len(days)

# ------------------------------
# TABS
# ------------------------------
tab1, tab2, tab3 = st.tabs(["📝 Input", "📊 Progress", "📈 Charts"])

# ------------------------------
# TAB 1: INPUT
# ------------------------------
with tab1:
    st.subheader("📝 Enter Daily Water Intake (L)")
    st.info("💡 Daily Goal: **3.00 Liters**")
    for i, day in enumerate(days):
        st.session_state.intake[i] = st.number_input(
            f"{day}",
            min_value=0.0,
            max_value=10.0,
            step=0.1,
            format="%.2f",
            value=st.session_state.intake[i],
            key=f"day_{i}"
        )

# ------------------------------
# TAB 2: PROGRESS
# ------------------------------
with tab2:
    st.subheader("📊 Daily Progress vs Goal")

    df = pd.DataFrame({
        "Day": days,
        "Intake": [round(x, 2) for x in st.session_state.intake],
    })
    df["Goal"] = DAILY_GOAL
    df["Progress %"] = (df["Intake"] / DAILY_GOAL * 100).clip(0, 100)

    # Hydration badge function
    def hydration_badge(intake):
        if intake >= DAILY_GOAL:
            return "🟢 Great"
        elif intake >= DAILY_GOAL * 0.7:
            return "🟡 Almost"
        else:
            return "🔴 Low"

    df["Badge"] = df["Intake"].apply(hydration_badge)

    # Display daily summary
    for idx, row in df.iterrows():
        st.write(f"**{row['Day']}** | Intake: {row['Intake']:.2f} L | {row['Badge']}")
        st.progress(int(row["Progress %"]))

    # Weekly total
    weekly_total = sum(df["Intake"])
    st.success(f"✅ Weekly Total: **{weekly_total:.2f} L** (Goal: {WEEKLY_GOAL:.2f} L)")

# ------------------------------
# TAB 3: CHARTS
# ------------------------------
with tab3:
    st.subheader("📈 Hydration Charts")

    # Daily intake vs goal
    st.markdown("#### 📌 Daily Intake vs Goal")
    fig, ax = plt.subplots()
    ax.bar(df["Day"], df["Intake"], color="#00BFFF", label="Intake")
    ax.axhline(y=DAILY_GOAL, color="red", linestyle="--", label=f"Goal {DAILY_GOAL} L")
    ax.set_ylabel("Liters")
    ax.set_xticklabels(df["Day"], rotation=30, ha="right")
    ax.legend()
    st.pyplot(fig)

    # Weekly total chart
    st.markdown("#### 📌 Weekly Total")
    fig, ax = plt.subplots()
    ax.bar(["This Week"], [weekly_total], color="#4CAF50")
    ax.axhline(y=WEEKLY_GOAL, color="red", linestyle="--", label=f"Goal {WEEKLY_GOAL} L")
    ax.set_ylabel("Liters")
    ax.set_title("Weekly Water Intake")
    ax.legend()
    st.pyplot(fig)

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
