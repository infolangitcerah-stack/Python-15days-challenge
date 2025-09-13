import streamlit as st

# Page Title
st.title("Social Eagle GenAI Architect")
st.title("15 Days Python Challenge")

# Subheading for the day
st.header("Day 1 Challenge")

# Intro / cheerful note
st.write("🎉 Selamat Datang to your first challenge in the 15 Days Python Challenge!")
st.write("Let's learn to build something simple but fun 🚀.")

# Create a small form
with st.form("assignment_form"):
    # Input fields
    name = st.text_input("Enter your name:", "Coach Dom")
    age = st.slider("Select your age:", min_value=1, max_value=100, value=27)

    # Submit button
    submit = st.form_submit_button("Submit")

# Display report after submission
if submit:
    st.success(f"✅ Selamat Datang, {name}! You are {age} years old.")
    st.info("This is your learner's challenge work — keep going with a cheerful spirit 🌟")
