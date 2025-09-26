import streamlit as st
import random

# -------------------------------
# Setup
# -------------------------------
st.set_page_config(page_title="Snake Game", page_icon="🐍")

GRID_SIZE = 15

# Initialize session state
if "snake" not in st.session_state:
    st.session_state.snake = [(5, 5)]
if "food" not in st.session_state:
    st.session_state.food = (7, 7)
if "direction" not in st.session_state:
    st.session_state.direction = "RIGHT"
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False


# -------------------------------
# Game Logic
# -------------------------------
def move_snake():
    if st.session_state.game_over:
        return

    head_x, head_y = st.session_state.snake[0]

    if st.session_state.direction == "UP":
        head_y -= 1
    elif st.session_state.direction == "DOWN":
        head_y += 1
    elif st.session_state.direction == "LEFT":
        head_x -= 1
    elif st.session_state.direction == "RIGHT":
        head_x += 1

    new_head = (head_x, head_y)

    # Collision check
    if (
        new_head in st.session_state.snake
        or head_x < 0
        or head_x >= GRID_SIZE
        or head_y < 0
        or head_y >= GRID_SIZE
    ):
        st.session_state.game_over = True
        return

    st.session_state.snake.insert(0, new_head)

    # Food eaten
    if new_head == st.session_state.food:
        st.session_state.score += 1
        st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    else:
        st.session_state.snake.pop()


# -------------------------------
# Draw Board
# -------------------------------
def draw_board():
    board = [["⬛" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for x, y in st.session_state.snake:
        board[y][x] = "🟩"

    fx, fy = st.session_state.food
    board[fy][fx] = "🍒"

    board_str = "\n".join("".join(row) for row in board)
    st.text(board_str)


# -------------------------------
# UI
# -------------------------------
st.title("🐍 Simple Snake Game")
st.write(f"Score: {st.session_state.score}")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ Left"):
        if st.session_state.direction != "RIGHT":
            st.session_state.direction = "LEFT"
with col2:
    if st.button("⬆️ Up"):
        if st.session_state.direction != "DOWN":
            st.session_state.direction = "UP"
    if st.button("⬇️ Down"):
        if st.session_state.direction != "UP":
            st.session_state.direction = "DOWN"
with col3:
    if st.button("➡️ Right"):
        if st.session_state.direction != "LEFT":
            st.session_state.direction = "RIGHT"

if not st.session_state.game_over:
    move_snake()
    draw_board()
else:
    st.error("💀 Game Over!")
    if st.button("🔄 Restart"):
        st.session_state.snake = [(5, 5)]
        st.session_state.food = (7, 7)
        st.session_state.direction = "RIGHT"
        st.session_state.score = 0
        st.session_state.game_over = False
