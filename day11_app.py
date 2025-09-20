import streamlit as st
import pandas as pd

# ------------------------------
# HEADER
# ------------------------------
st.markdown(
    """
    <h1 style="text-align:center; color:#00e6e6;">🎉 Event Registration System</h1>
    <h3 style="text-align:center; color:#888;">Social Eagle GenAI Architect</h3>
    <h4 style="text-align:center; color:#888;">15 Days Python Challenge - Day 10 Assignment</h4>
    <h4 style="text-align:center; color:#ff66cc;">👨‍🏫 Coach Dom</h4>
    <hr>
    """,
    unsafe_allow_html=True,
)

st.write("Welcome to the **futuristic event registration system** 🚀. "
         "Fill out the form below to register and track participation live!")

# ------------------------------
# SESSION STATE STORAGE
# ------------------------------
if "registrations" not in st.session_state:
    st.session_state.registrations = []

# ------------------------------
# FORM
# ------------------------------
with st.form("registration_form"):
    name = st.text_input("👤 Name")
    email = st.text_input("📧 Email")
    event_choice = st.selectbox("🎯 Select Event", ["Hackathon", "Workshop", "Webinar", "AI Bootcamp"])
    submitted = st.form_submit_button("✅ Register")

    if submitted:
        if name and email:
            st.session_state.registrations.append(
                {"Name": name, "Email": email, "Event": event_choice}
            )
            st.success(f"🎉 {name}, you have successfully registered for {event_choice}!")
        else:
            st.error("⚠️ Please fill in both name and email.")

# ------------------------------
# RESULTS
# ------------------------------
st.subheader("📊 Live Registration Count")
st.info(f"Total Registrations: **{len(st.session_state.registrations)}**")

if st.session_state.registrations:
    df = pd.DataFrame(st.session_state.registrations)
    st.dataframe(df)

    # CSV Export
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "📥 Download Registrations (CSV)",
        csv,
        "registrations.csv",
        "text/csv",
        key="download-csv"
    )

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

