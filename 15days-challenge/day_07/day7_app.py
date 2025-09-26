# day7_app.py
import random
import sqlite3
from datetime import datetime

import pandas as pd
import streamlit as st

# Optional plotting import (graceful fallback)
try:
    import plotly.express as px

    PLOTLY_AVAILABLE = True
except Exception:
    px = None
    PLOTLY_AVAILABLE = False

# -------------------
# Database Setup
# -------------------
DB_FILE = "workouts.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            exercise_name TEXT,
            sets INTEGER,
            reps INTEGER,
            weight REAL
        )
    """
    )
    conn.commit()
    conn.close()


def log_workout(exercise: str, sets: int, reps: int, weight: float):
    ts = datetime.utcnow().isoformat(sep=" ", timespec="seconds")
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "INSERT INTO workouts (timestamp, exercise_name, sets, reps, weight) VALUES (?,?,?,?,?)",
        (ts, exercise, sets, reps, weight),
    )
    conn.commit()
    conn.close()


def fetch_history_df() -> pd.DataFrame:
    conn = sqlite3.connect(DB_FILE)
    try:
        df = pd.read_sql_query("SELECT * FROM workouts ORDER BY timestamp DESC", conn)
    finally:
        conn.close()
    if df.empty:
        return pd.DataFrame(
            columns=["id", "timestamp", "exercise_name", "sets", "reps", "weight", "date", "volume"]
        )
    # Handle mixed timestamp formats safely
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce", format="mixed")
    df["date"] = df["timestamp"].dt.date
    df["volume"] = df["sets"] * df["reps"] * df["weight"]
    return df


# ✅ Initialize DB after functions are defined
init_db()

# -------------------
# Page Config & CSS
# -------------------
st.set_page_config(page_title="Gym Workout Logger", page_icon="🏋️", layout="centered")

st.markdown(
    """
    <style>
      .block-container { max-width: 820px; margin: auto; }
      .big-title { font-size: 34px !important; text-align:center; color:#FF4B4B; font-weight:700; margin-bottom:0.1rem; }
      .sub-title { text-align:center; font-size:15px; color:#4B9EFF; margin-top:0.2rem; margin-bottom:12px; }
      .badge { display:inline-block; padding:6px 12px; border-radius:999px; font-weight:600; margin-top:8px; transition: all 0.5s ease-in-out; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------
# Header
# -------------------
st.markdown('<div class="big-title">🏋️ Gym Workout Logger</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">🚀 Social Eagle GenAI Architect | 15 Days Python Challenge | Coach Dom</div>',
    unsafe_allow_html=True,
)

# -------------------
# Motivational Badge (cycles every rerun)
# -------------------
badges = [
    ("🔥 Great Gym Enthusiast", "#FF5733"),
    ("⚡ Strength Builder", "#4B9EFF"),
    ("🏆 Consistency Champ", "#28A745"),
    ("💪 Never Skip a Rep", "#FFC107"),
    ("🚀 Progress Over Perfection", "#9B59B6"),
]
text, color = random.choice(badges)
st.markdown(
    f'<div class="badge" style="background-color:{color}; color:white;">{text}</div>',
    unsafe_allow_html=True,
)

# -------------------
# Tabs
# -------------------
tab1, tab2, tab3, tab4 = st.tabs(["📝 Log Workout", "📜 History", "📈 Progress", "💡 Coach Dom"])

# --- Tab 1: Log Workout ---
with tab1:
    st.subheader("Log a New Workout")
    exercises = [
        "Bench Press",
        "Squat",
        "Deadlift",
        "Pull-ups",
        "Push-ups",
        "Overhead Press",
        "Bicep Curls",
        "Tricep Dips",
        "Plank",
    ]
    with st.form("log_form", clear_on_submit=False):
        colA, colB, colC = st.columns([3, 1, 1])
        with colA:
            selected = st.selectbox("Exercise", exercises + ["Other (type below)"])
            if selected == "Other (type below)":
                exercise = st.text_input("Custom exercise name")
            else:
                exercise = selected
        with colB:
            sets = st.number_input("Sets", min_value=1, value=3)
        with colC:
            reps = st.number_input("Reps", min_value=1, value=8)
        weight = st.number_input("Weight (kg)", min_value=0.0, value=20.0, step=0.5)
        submitted = st.form_submit_button("Log Workout ✅")

        if submitted:
            if not exercise or str(exercise).strip() == "":
                st.error("Please enter an exercise name.")
            else:
                log_workout(str(exercise).strip(), int(sets), int(reps), float(weight))
                st.success(f"Logged: **{exercise}** — {sets} sets × {reps} reps × {weight} kg")
                st.experimental_rerun()

# --- Tab 2: History ---
with tab2:
    st.subheader("Workout History")
    df_hist = fetch_history_df()
    if df_hist.empty:
        st.info("No workouts logged yet — use the Log tab to add your first entry.")
    else:
        display = df_hist[["date", "exercise_name", "volume"]].rename(
            columns={"date": "Date", "exercise_name": "Exercise", "volume": "Volume"}
        )
        st.dataframe(display.reset_index(drop=True), use_container_width=True)

# --- Tab 3: Progress ---
with tab3:
    st.subheader("Weekly Progress")
    df_progress = fetch_history_df()
    if df_progress.empty:
        st.info("No data yet. Log workouts to see progress here.")
    else:
        df_progress["week"] = df_progress["timestamp"].dt.strftime("%Y-%U")
        weekly = df_progress.groupby("week", as_index=False)["volume"].sum().sort_values("week")
        if PLOTLY_AVAILABLE:
            try:
                fig = px.bar(
                    weekly,
                    x="week",
                    y="volume",
                    title="Total Training Volume per Week",
                    labels={"week": "Week", "volume": "Volume (sets×reps×weight)"},
                    color="volume",
                    color_continuous_scale="Blues",
                )
                st.plotly_chart(fig, use_container_width=True)
            except Exception:
                st.warning("Plotly failed to render; showing fallback chart.")
                st.bar_chart(weekly.set_index("week")["volume"])
        else:
            st.warning(
                "Plotly not installed — showing fallback chart. Install with `pip install plotly`"
            )
            st.bar_chart(weekly.set_index("week")["volume"])

# --- Tab 4: Coach Dom ---
with tab4:
    st.subheader("Coach Dom — Your training partner")
    st.markdown(
        """
        👋 Hi, I'm **Coach Dom** — I craft simple, effective training plans and keep you accountable.
        
        **Services**
        - Personalized programs
        - Weekly check-ins & progress review
        - Technique feedback & motivation

        If you'd like to try a one-off consult, press the button below.
        """
    )
    if st.button("Contact Coach Dom 📩"):
        st.info("Thanks — Coach Dom (demo) will reach out! (This is a placeholder CTA.)")

# --- Diagnostics ---
with st.expander("Diagnostics / Quick checks (open if something is missing)"):
    import sys

    st.write("Python:", sys.version.splitlines()[0])
    st.write("Streamlit version:", st.__version__)
    st.write("Plotly available:", PLOTLY_AVAILABLE)
    st.write("Database file:", DB_FILE)
    try:
        df_diag = fetch_history_df()
        st.write("DB rows:", len(df_diag))
    except Exception as e:
        st.error("Error reading DB — see terminal for full traceback.")
        st.exception(e)
