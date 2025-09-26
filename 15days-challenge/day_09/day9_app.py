import streamlit as st

# ----------------------------
# Social Eagle GenAI Architect | 15 Days Python Challenge
# Day 9 Assignment – Quiz Game App ❓
# Coach Dom
# ----------------------------

st.set_page_config(page_title="Quiz Game ❓", page_icon="❓", layout="centered")

# ---------- Custom CSS (clean & white) ----------
st.markdown(
    """
    <style>
      /* Plain white background */
      .stApp {
        background-color: #ffffff;
        color: #111111;
      }

      /* Title styling */
      h1 {
        color: #1a1a1a !important;
      }

      /* Card-like container */
      .quiz-card {
        background: #f9f9f9;
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
      }

      /* Buttons */
      .stButton>button {
        border-radius: 10px;
        padding: 8px 14px;
        font-weight: 600;
        background: #0072ff;
        color: #ffffff;
        border: none;
      }
      .stButton>button:hover {
        background: #005bb5;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Quiz Questions (hardcoded) ----------
QUESTIONS = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi",
    },
    {
        "question": "Which language is primarily used for data analysis and ML?",
        "options": ["Java", "C++", "Python", "Ruby"],
        "answer": "Python",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "answer": "Mars",
    },
    {
        "question": "What does HTTP stand for?",
        "options": [
            "HyperText Transfer Protocol",
            "High Transfer Text Protocol",
            "Hyperlink Text Transfer Process",
            "Hyper Transfer Text Protocol",
        ],
        "answer": "HyperText Transfer Protocol",
    },
    {
        "question": "Which library is used for creating interactive web apps in Python?",
        "options": ["Flask", "Streamlit", "Django", "Tkinter"],
        "answer": "Streamlit",
    },
]

TOTAL = len(QUESTIONS)

# ---------- Session state initialization ----------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "selected" not in st.session_state:
    st.session_state.selected = None


# ---------- Helper functions ----------
def submit_answer():
    if st.session_state.selected is None:
        st.warning("Please select an option before submitting.")
        return

    if not st.session_state.answered:
        current_q = QUESTIONS[st.session_state.q_index]
        if st.session_state.selected == current_q["answer"]:
            st.session_state.score += 1
            st.session_state.feedback = ("Correct ✅", True)
        else:
            st.session_state.feedback = (
                f"Wrong ❌  — correct answer: {current_q['answer']}",
                False,
            )
        st.session_state.answered = True


def next_question():
    if st.session_state.q_index + 1 < TOTAL:
        st.session_state.q_index += 1
        st.session_state.answered = False
        st.session_state.selected = None
        st.session_state.feedback = ("", None)
    else:
        st.session_state.show_results = True


def restart_quiz():
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.show_results = False
    st.session_state.feedback = ("", None)


# ---------- UI ----------
st.markdown("<h1 style='text-align:center;'>❓ Quiz Game</h1>", unsafe_allow_html=True)
st.write("### Day 9 | Social Eagle GenAI Architect  — Coach Dom")
st.write("Test your knowledge! Choose the correct option and submit. Good luck 🚀")

# Card container
st.markdown('<div class="quiz-card">', unsafe_allow_html=True)

# Progress
progress_text = f"Question {st.session_state.q_index + 1} of {TOTAL}"
st.write(f"**{progress_text}**")
st.progress((st.session_state.q_index) / max(TOTAL - 1, 1))

# Current question
q = QUESTIONS[st.session_state.q_index]
st.write("### " + q["question"])

st.session_state.selected = st.radio(
    "Select an answer:",
    q["options"],
    index=0 if st.session_state.selected is None else q["options"].index(st.session_state.selected),
)

# Buttons
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("Submit"):
        submit_answer()

with col2:
    if st.button("Skip"):
        st.session_state.answered = True
        st.session_state.feedback = (f"Skipped — correct: {q['answer']}", False)

with col3:
    if st.session_state.answered:
        if st.button("Next"):
            next_question()

# Feedback
if "feedback" not in st.session_state:
    st.session_state.feedback = ("", None)

feedback_text, correct_flag = st.session_state.feedback
if st.session_state.answered and feedback_text:
    if correct_flag:
        st.success(feedback_text)
    else:
        st.error(feedback_text)

st.markdown("</div>", unsafe_allow_html=True)

# Results
if "show_results" in st.session_state and st.session_state.show_results:
    st.markdown("---")
    st.balloons()
    st.markdown(
        "<h2 style='text-align:center;color:#0072ff'>🎉 Quiz Complete!</h2>",
        unsafe_allow_html=True,
    )
    pct = (st.session_state.score / TOTAL) * 100
    st.metric(label="Score", value=f"{st.session_state.score} / {TOTAL}")
    st.write(f"**Percentage:** {pct:.2f}%")

    if pct == 100:
        st.success("Perfect score! You're a quiz master 👑")
    elif pct >= 70:
        st.success("Great job! Keep it up 👍")
    elif pct >= 40:
        st.info("Nice effort — a little more practice and you'll ace it 🚀")
    else:
        st.info("Good start — try again to improve your score 💪")

    st.button("Restart Quiz", on_click=restart_quiz)

# Current score
if not st.session_state.get("show_results", False):
    st.markdown("---")
    pct_now = (st.session_state.score / max(1, (st.session_state.q_index + 1))) * 100
    st.write(f"**Current Score:** {st.session_state.score} points | Progress: {pct_now:.2f}%")

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align:center;color:#555555'>
      Built for <b>Social Eagle GenAI Architect — Day 9</b> | Coach Dom
    </p>
    """,
    unsafe_allow_html=True,
)
