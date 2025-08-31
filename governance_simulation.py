
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.express as px

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state.responses = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()

st.title("Corporate Governance Simulation")

# Countdown timer (15 minutes)
countdown = timedelta(minutes=15) - (datetime.now() - st.session_state.start_time)
if countdown.total_seconds() > 0:
    st.info(f"Time remaining: {str(countdown).split('.')[0]}")
else:
    st.warning("Time is up! Submissions are now closed.")

username = st.text_input("Enter your name:")

st.header("Scenario 1: Executive Compensation")
comp_choice = st.radio("Choose a compensation strategy:", [
    "Fixed salary with minimal bonuses",
    "Performance-based bonuses tied to financial metrics",
    "Stock options with long-term vesting"
])

st.header("Scenario 2: Audit Policy")
audit_choice = st.radio("Choose an audit approach:", [
    "Internal audit only",
    "Annual external audit",
    "Real-time external audit with board oversight"
])

st.header("Scenario 3: Sustainability Strategy")
sustain_choice = st.radio("Choose a sustainability strategy:", [
    "Focus solely on profit",
    "Balance profit with environmental goals",
    "Integrate profit, environment, and social development"
])

reflection = st.text_area("Reflect on your decisions and strategy:")

def evaluate_choices(comp, audit, sustain):
    score = 0
    if comp == "Stock options with long-term vesting":
        score += 2
    elif comp == "Performance-based bonuses tied to financial metrics":
        score += 1

    if audit == "Real-time external audit with board oversight":
        score += 2
    elif audit == "Annual external audit":
        score += 1

    if sustain == "Integrate profit, environment, and social development":
        score += 2
    elif sustain == "Balance profit with environmental goals":
        score += 1

    return score

if st.button("Submit Choices") and countdown.total_seconds() > 0:
    if username.strip() == "":
        st.warning("Please enter your name before submitting.")
    else:
        score = evaluate_choices(comp_choice, audit_choice, sustain_choice)
        st.session_state.responses.append({
            "Name": username,
            "Compensation": comp_choice,
            "Audit": audit_choice,
            "Sustainability": sustain_choice,
            "Score": score,
            "Reflection": reflection,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        st.success("Your responses have been saved.")
        st.write(f"Shareholder Satisfaction Score: {score} / 6")

# Display class summary and charts
if st.session_state.responses:
    st.subheader("Class Summary")
    df = pd.DataFrame(st.session_state.responses)

    comp_summary = df['Compensation'].value_counts().idxmax()
    audit_summary = df['Audit'].value_counts().idxmax()
    sustain_summary = df['Sustainability'].value_counts().idxmax()
    avg_score = df['Score'].mean()

    summary = (f"Most students chose '{comp_summary}' for compensation, "
               f"'{audit_summary}' for audit policy, and "
               f"'{sustain_summary}' for sustainability strategy. "
               f"The average score across the class is {avg_score:.2f}.")
    st.write(summary)

    # Visual charts
    st.plotly_chart(px.bar(df['Compensation'].value_counts().reset_index(), x='index', y='Compensation', title='Compensation Choices'))
    st.plotly_chart(px.bar(df['Audit'].value_counts().reset_index(), x='index', y='Audit', title='Audit Policy Choices'))
    st.plotly_chart(px.bar(df['Sustainability'].value_counts().reset_index(), x='index', y='Sustainability', title='Sustainability Strategy Choices'))

    # Download responses
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download All Responses as CSV", data=csv, file_name="class_responses.csv", mime="text/csv")

# Reset button
if st.button("Reset All Responses"):
    st.session_state.responses = []
    st.session_state.start_time = datetime.now()
    st.success("All responses have been cleared and timer reset.")
