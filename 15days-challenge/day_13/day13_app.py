# ---------------------------------------------------------
# Title: "Rock, Paper, Scissors Game"
# Context 1: "Social Eagle GenAI Architect"
# Context 2: "15 Days Python Challenge"
# Context 3: "Day 13 Assignment"
# Context 4: "Coach Dom"
# ---------------------------------------------------------

import random
import time

import streamlit as st

# ------------------------------- Page Setup -------------------------------
st.set_page_config(page_title="Rock, Paper, Scissors Game", page_icon="🪨", layout="centered")

# ------------------------------- Styles (Neo-Cyberpunk + Larger Fonts) -------------------------------
st.markdown(
    """
<style>
:root{
  --bg:#0a0f1c;
  --panel:#0e1526;
  --neon-blue:#3ea3ff;
  --neon-magenta:#ff42e7;
  --neon-green:#39ffb6;
  --neon-orange:#ff9f3e;
  --text:#e6f1ff;
  --muted:#9bb3d1;
}

[data-testid="stAppViewContainer"]{
  background:
    radial-gradient(900px 500px at 10% 10%, rgba(62,163,255,.08), transparent 60%),
    radial-gradient(900px 500px at 90% 80%, rgba(255,66,231,.08), transparent 60%),
    linear-gradient(180deg, #0b1120 0%, #0a0f1c 60%, #080d18 100%);
  color: var(--text);
  font-family: ui-sans-serif, system-ui, "Segoe UI", "SF Pro Text", Roboto, Helvetica, Arial;
  font-size: 18px;
}

.block-container{max-width: 900px; padding-top: 1rem}

h1{ font-size: 2.4rem; text-shadow: 0 0 12px rgba(62,163,255,.35); }
h2{ font-size: 1.8rem; text-shadow: 0 0 12px rgba(62,163,255,.35); }
h3{ font-size: 1.5rem; text-shadow: 0 0 12px rgba(62,163,255,.35); }

.card{
  background: linear-gradient(145deg, var(--panel), #0b1324);
  border: 1px solid rgba(62,163,255,.25);
  border-radius: 18px;
  padding: 1rem 1.2rem;
  box-shadow: 0 12px 30px rgba(0,0,0,.35), inset 0 0 18px rgba(62,163,255,.06);
  font-size: 18px;
}

.choice-btn{
  display:inline-flex; align-items:center; justify-content:center;
  width:100%; height:90px;
  border-radius:18px;
  border:1px solid rgba(62,163,255,.35);
  background: linear-gradient(145deg, #0b142a, #0a1122);
  color: var(--text); font-size: 34px; font-weight:800;
  box-shadow: inset 0 0 14px rgba(62,163,255,.12);
  cursor:pointer; user-select:none;
  transition: transform .08s ease, box-shadow .12s ease, border-color .12s ease;
}
.choice-btn:hover{
  transform: translateY(-2px);
  border-color: var(--neon-blue);
  box-shadow: 0 10px 26px rgba(62,163,255,.18), inset 0 0 18px rgba(62,163,255,.18);
}

.outcome{
  display:flex; align-items:center; justify-content:center;
  min-height:60px; border-radius:16px; font-weight:800; font-size:22px;
  border:1px solid rgba(255,255,255,.08);
  background: linear-gradient(145deg, #0c152a, #0a1222);
  color: var(--text);
}
.outcome.win{ border-color: rgba(57,255,182,.6); }
.outcome.lose{ border-color: rgba(255,66,231,.6); }
.outcome.draw{ border-color: rgba(255,159,62,.6); }

.badge{
  display:inline-block; padding:.4rem .8rem; border-radius:999px; font-weight:700;
  border:1px solid rgba(62,163,255,.35); color:var(--text); background:rgba(62,163,255,.08);
  font-size: 18px;
}

.bar-wrap{ display:grid; gap:.4rem; font-size:16px; }
.bar-row{ display:flex; align-items:center; gap:.6rem; }
.bar-label{ width:90px; color:var(--muted); font-weight:700; }
.bar{ height:18px; border-radius:999px; border:1px solid rgba(62,163,255,.25); background:rgba(62,163,255,.08); }
.bar > span{ display:block; height:100%; width:0%; transition:width .4s ease; }
.bar.win > span{ background: linear-gradient(90deg, var(--neon-green), var(--neon-blue)); }
.bar.lose > span{ background: linear-gradient(90deg, var(--neon-magenta), var(--neon-orange)); }
.bar.draw > span{ background: linear-gradient(90deg, var(--neon-orange), var(--neon-blue)); }
</style>
""",
    unsafe_allow_html=True,
)


# ------------------------------- State -------------------------------
def _init_state():
    st.session_state.setdefault("user_score", 0)
    st.session_state.setdefault("cpu_score", 0)
    st.session_state.setdefault("draws", 0)
    st.session_state.setdefault("history", [])


_init_state()

# ------------------------------- Helpers -------------------------------
CHOICES = ["🪨 Rock", "📜 Paper", "✂️ Scissors"]


def parse_choice(label: str) -> str:
    return "rock" if "Rock" in label else "paper" if "Paper" in label else "scissors"


def get_computer_choice() -> str:
    return random.choice(["rock", "paper", "scissors"])


def decide_winner(user: str, cpu: str) -> str:
    if user == cpu:
        return "draw"
    wins = {("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")}
    return "win" if (user, cpu) in wins else "lose"


def record_round(user: str, cpu: str, outcome: str) -> None:
    st.session_state.history.append({"user": user, "cpu": cpu, "outcome": outcome})
    if outcome == "win":
        st.session_state.user_score += 1
    elif outcome == "lose":
        st.session_state.cpu_score += 1
    else:
        st.session_state.draws += 1


def reset_scores():
    st.session_state.user_score = 0
    st.session_state.cpu_score = 0
    st.session_state.draws = 0
    st.session_state.history = []


# ------------------------------- Header -------------------------------

# Spacer at very top
st.markdown("<div style='height:80px;'></div>", unsafe_allow_html=True)

# Title & Contexts (output on page)
st.markdown('# 🪨📜✂️ Title: "Rock, Paper, Scissors Game"')
st.markdown(
    """
    <div style="text-align:center">
        <h3>Social Eagle GenAI Architect</h3>
        <h3>15 Days Python Challenge</h3>
        <h3>Day 13 Assignment</h3>
        <h3>Coach Dom</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("## 🛰️ Greetings, Architect!")
st.markdown(
    "<div class='card'>Prepare to test your intuition against the <b>A.I. Protocol</b>. "
    "Select your move. Scores persist during your session. Good luck.</div>",
    unsafe_allow_html=True,
)

# ------------------------------- Scoreboard -------------------------------
c1, c2, c3, c4 = st.columns([1, 1, 1, 1])
with c1:
    st.markdown(
        f"**You** <span class='badge'>{st.session_state.user_score}</span>", unsafe_allow_html=True
    )
with c2:
    st.markdown(
        f"**A.I.** <span class='badge'>{st.session_state.cpu_score}</span>", unsafe_allow_html=True
    )
with c3:
    st.markdown(
        f"**Draws** <span class='badge'>{st.session_state.draws}</span>", unsafe_allow_html=True
    )
with c4:
    if st.button("🔄 Reset Score"):
        reset_scores()

# ------------------------------- Game Buttons -------------------------------
colA, colB, colC = st.columns(3)
user_pick = None
if colA.button(CHOICES[0]):
    user_pick = parse_choice(CHOICES[0])
if colB.button(CHOICES[1]):
    user_pick = parse_choice(CHOICES[1])
if colC.button(CHOICES[2]):
    user_pick = parse_choice(CHOICES[2])

# ------------------------------- Round Logic -------------------------------
outcome_text = ""
cpu_choice = None
if user_pick:
    time.sleep(0.05)
    cpu_choice = get_computer_choice()
    result = decide_winner(user_pick, cpu_choice)
    record_round(user_pick, cpu_choice, result)
    if result == "win":
        outcome_text = "🟢 A flawless victory, Architect!"
    elif result == "lose":
        outcome_text = "🟣 A minor setback. The A.I. adapts. Try again!"
    else:
        outcome_text = "🟠 A perfect stalemate. Awaiting your next command."

# ------------------------------- Outcome -------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
if user_pick:
    sym = {"rock": "🪨 Rock", "paper": "📜 Paper", "scissors": "✂️ Scissors"}
    st.markdown(f"**You:** {sym[user_pick]} | **A.I.:** {sym[cpu_choice]}")
st.markdown(
    f"<div class='outcome'>{outcome_text or 'Make your move above.'}</div>", unsafe_allow_html=True
)
st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------- History -------------------------------
with st.expander("Round History (latest first)"):
    if st.session_state.history:
        sym = {"rock": "🪨 Rock", "paper": "📜 Paper", "scissors": "✂️ Scissors"}
        for rec in reversed(st.session_state.history[-10:]):
            st.markdown(
                f"- You: **{sym[rec['user']]}** | A.I.: **{sym[rec['cpu']]}** → **{rec['outcome'].upper()}**"
            )
    else:
        st.caption("No rounds yet. Engage when ready, Architect.")

# ------------------------------- Chart -------------------------------
total = len(st.session_state.history)
if total >= 5:
    wins, losses, draws = (
        st.session_state.user_score,
        st.session_state.cpu_score,
        st.session_state.draws,
    )

    def pct(x):
        return 0 if total == 0 else int(100 * x / total)

    st.markdown("#### Session Summary")
    st.markdown(
        f"""
<div class='bar-wrap'>
  <div class='bar-row'><div class='bar-label'>Wins</div>
    <div class='bar win'><span style='width:{pct(wins)}%'></span></div>
    <div class='bar-label'>{wins}/{total}</div></div>
  <div class='bar-row'><div class='bar-label'>Losses</div>
    <div class='bar lose'><span style='width:{pct(losses)}%'></span></div>
    <div class='bar-label'>{losses}/{total}</div></div>
  <div class='bar-row'><div class='bar-label'>Draws</div>
    <div class='bar draw'><span style='width:{pct(draws)}%'></span></div>
    <div class='bar-label'>{draws}/{total}</div></div>
</div>
""",
        unsafe_allow_html=True,
    )
