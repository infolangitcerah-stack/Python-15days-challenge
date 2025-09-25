# day12_tictactoe.py
# Context: Tic-Tac-Toe ❌⭕ | Social Eagle GenAI Architect | 15 Days Python Challenge
# Day 12 Assignment | Coach Dom

import streamlit as st
import random

st.set_page_config(page_title="Futuristic Tic-Tac-Toe ❌⭕", page_icon="✨", layout="centered")

# ----------------------- Styling (Futuristic) -----------------------
st.markdown("""
<style>
/* Neon gradient background */
[data-testid="stAppViewContainer"] {
  background: radial-gradient(1200px 600px at 10% 10%, #101426 0%, #0b0f1a 40%, #080d16 100%);
  color: #e6f1ff;
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}

/* Title glow */
h1, h2, h3 {
  text-shadow: 0 0 10px rgba(99, 179, 237, .45);
}

/* Card-like container */
.block-container { padding-top: 2rem; }

/* Primary buttons (game cells while playing) */
.stButton>button {
  background: linear-gradient(145deg, #111a2b, #0c1524);
  border: 1px solid #1f3b63;
  color: #d6e8ff;
  box-shadow: 0 0 0px rgba(0,0,0,0), inset 0 0 12px rgba(50, 120, 200, 0.25);
  transition: all .12s ease-in-out;
  border-radius: 18px;
  width: 100%;
  height: 90px;
  font-size: 32px;
  font-weight: 700;
}
.stButton>button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 22px rgba(30, 120, 255, .20), 0 0 16px rgba(30, 120, 255, .25) inset;
  border-color: #3e7ede;
}

/* Utility chips */
.badge {
  display:inline-block;padding:.35rem .6rem;border:1px solid #2d5aa6;
  border-radius:999px;background:rgba(30,120,255,.08);color:#beddff;
  font-size:.82rem;margin-left:.25rem
}

/* Static tiles when game is over (to highlight winning line) */
.tile {
  display:flex;align-items:center;justify-content:center;
  width:100%; height: 90px; border-radius:18px; font-size:32px; font-weight:800;
  border:1px solid #244a82; background:linear-gradient(145deg,#0e1626,#0a1322);
}
.tile.win {
  border:1px solid #37ffd2;
  background:linear-gradient(145deg,#0e2630,#0a1f24);
  box-shadow:0 0 22px rgba(55,255,210,.35), inset 0 0 18px rgba(55,255,210,.25);
  color:#d7fff5;
}
.tile.draw {
  opacity:.9;
}
.help {
  color:#a9c8ff; font-size:.92rem;
}
</style>
""", unsafe_allow_html=True)

# ----------------------- Helpers -----------------------
WIN_LINES = [
    (0,1,2),(3,4,5),(6,7,8),     # rows
    (0,3,6),(1,4,7),(2,5,8),     # cols
    (0,4,8),(2,4,6)              # diagonals
]

def check_winner(board):
    for a,b,c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a], (a,b,c)  # 'X' or 'O', winning combo
    if "" not in board:
        return "Draw", ()             # Draw
    return None, ()                   # No winner yet

def toggle(p): return "O" if p == "X" else "X"

def make_move(idx):
    if st.session_state.winner:  # game over
        return
    if st.session_state.board[idx] == "":
        st.session_state.board[idx] = st.session_state.player
        winner, combo = check_winner(st.session_state.board)
        st.session_state.winner, st.session_state.win_combo = winner, combo
        if not winner:
            st.session_state.player = toggle(st.session_state.player)

def computer_move_random():
    if st.session_state.winner: return
    empties = [i for i,v in enumerate(st.session_state.board) if v==""]
    if not empties: return
    idx = random.choice(empties)
    st.session_state.board[idx] = "O"
    winner, combo = check_winner(st.session_state.board)
    st.session_state.winner, st.session_state.win_combo = winner, combo
    if not winner:
        st.session_state.player = toggle(st.session_state.player)

def reset():
    st.session_state.board   = [""]*9
    st.session_state.player  = "X"
    st.session_state.winner  = None
    st.session_state.win_combo = ()

# ----------------------- State -----------------------
if "board" not in st.session_state:
    reset()
if "mode" not in st.session_state:
    st.session_state.mode = "Two Players"

# ----------------------- UI -----------------------
st.title("✨ Futuristic Tic-Tac-Toe ❌⭕")
st.caption("Social Eagle GenAI Architect • 15 Days Python Challenge • Day 12 • Coach Dom")

left, right = st.columns([1,1])
with left:
    st.session_state.mode = st.selectbox(
        "Game Mode",
        ["Two Players", "Vs Computer (random AI)"],
        index=0,
        help="Choose to play with a friend or versus a simple random-move computer."
    )
with right:
    if st.button("🔄 Reset Board", use_container_width=True):
        reset()

# Status line
if not st.session_state.winner:
    st.markdown(
        f"**Turn:** {'❌ X' if st.session_state.player=='X' else '⭕ O'} "
        f"<span class='badge'>{st.session_state.mode}</span>",
        unsafe_allow_html=True
    )
else:
    if st.session_state.winner == "Draw":
        st.markdown("**Result:** 🤝 Draw!", unsafe_allow_html=True)
    else:
        st.markdown(f"**Winner:** {'❌ X' if st.session_state.winner=='X' else '⭕ O'} 🏆", unsafe_allow_html=True)

# ----------------------- Board -----------------------
def render_board(interactive=True):
    for r in range(3):
        cols = st.columns(3, gap="small")
        for c in range(3):
            i = r*3 + c
            label = st.session_state.board[i] if st.session_state.board[i] else " "
            if interactive and not st.session_state.winner:
                if cols[c].button(label, key=f"cell_{i}"):
                    make_move(i)
                    # If vs computer and it's O's turn, let AI move immediately
                    if (st.session_state.mode.startswith("Vs Computer")
                        and st.session_state.player == "O"
                        and not st.session_state.winner):
                        computer_move_random()
            else:
                # Static tiles (after game ends)
                is_win = i in st.session_state.win_combo
                klass = "tile win" if is_win else "tile draw" if st.session_state.winner=="Draw" else "tile"
                cols[c].markdown(f"<div class='{klass}'>{label}</div>", unsafe_allow_html=True)

# During play, show interactive buttons; after end, show colored tiles
render_board(interactive=(st.session_state.winner is None))

# Friendly help text
st.markdown("""
<div class='help'>
• Click a square to place your mark. Winning line will glow cyan.<br>
• In <b>Vs Computer</b>, you are <b>X</b>. The computer plays random <b>O</b> moves.<br>
• Use <b>Reset Board</b> to start a new match. Have fun!
</div>
""", unsafe_allow_html=True)
