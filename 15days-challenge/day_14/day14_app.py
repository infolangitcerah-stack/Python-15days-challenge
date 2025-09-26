import streamlit as st
import time

# -------------------------------
# 🎨 App Setup
# -------------------------------
st.set_page_config(page_title="Futuristic Stopwatch", page_icon="⏱️", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #0D1117;
        color: #E6EDF3;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .header {
        text-align: center;
        padding: 20px;
        margin-bottom: 20px;
        border-radius: 15px;
        background: linear-gradient(90deg, #00f0ff, #ff00f7);
        color: white;
        font-size: 28px;
        font-weight: bold;
        box-shadow: 0 0 15px #00f0ff;
    }
    .sub-header {
        text-align: center;
        color: #111827;   /* 🔥 dark tone */
        font-size: 16px;
        margin-bottom: 30px;
        font-weight: 500;
    }
    .time-display {
        font-size: 72px;
        font-weight: bold;
        color: #00f0ff;
        text-shadow: 0px 0px 25px #00f0ff;
        text-align: center;
        margin: 20px 0;
    }
    .stButton button {
        background: linear-gradient(90deg, #00f0ff, #ff00f7);
        color: white;
        border: none;
        padding: 12px 28px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        transition: 0.3s;
        box-shadow: 0px 0px 10px #00f0ff;
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 20px #ff00f7;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# -------------------------------
# 📌 Header
# -------------------------------
st.markdown("<div class='header'>🚀 Day 14 - Stop Watch Challenge</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-header'>Social Eagle GenAI Architect | Built by Coach Dom | 15 Days Python Challenge</div>",
    unsafe_allow_html=True,
)

# -------------------------------
# ⏱️ Stopwatch State
# -------------------------------
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0.0
if "running" not in st.session_state:
    st.session_state.running = False

# -------------------------------
# 🎛️ Controls
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶️ Start"):
        if not st.session_state.running:
            st.session_state.start_time = time.time() - st.session_state.elapsed
            st.session_state.running = True

with col2:
    if st.button("⏸️ Pause"):
        if st.session_state.running:
            st.session_state.elapsed = time.time() - st.session_state.start_time
            st.session_state.running = False

with col3:
    if st.button("⏹️ Reset"):
        st.session_state.start_time = None
        st.session_state.elapsed = 0.0
        st.session_state.running = False

# -------------------------------
# ⏱️ Live Display
# -------------------------------
placeholder = st.empty()

if st.session_state.running:
    # Live update loop
    while st.session_state.running:
        elapsed_time = time.time() - st.session_state.start_time
        placeholder.markdown(
            f"<div class='time-display'>{elapsed_time:.2f} s</div>", unsafe_allow_html=True
        )
        time.sleep(0.1)
        st.rerun()  # use st.rerun if Streamlit >= 1.25, else st.experimental_rerun
else:
    placeholder.markdown(
        f"<div class='time-display'>{st.session_state.elapsed:.2f} s</div>", unsafe_allow_html=True
    )
