import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

# Initialize session state
if 'responses' not in st.session_state:
    st.session_state.responses = []
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()

st.title("Corporate Governance Simulation")

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
    feedback = []

    if comp == "Stock options with long-term vesting":
        score += 2
    elif comp == "Performance-based bonuses tied to financial metrics":
        score += 1
    else:
        feedback.append("Consider offering performance-based or equity-linked compensation to better align management incentives with shareholder interests.")

    if audit == "Real-time external audit with board oversight":
        score += 2
    elif audit == "Annual external audit":
        score += 1
    else:
        feedback.append("Internal audits alone may lack independence. External oversight improves transparency and credibility.")

    if sustain == "Integrate profit, environment, and social development":
        score += 2
    elif sustain == "Balance profit with environmental goals":
        score += 1
    else:
        feedback.append("A narrow focus on profit may overlook long-term sustainability and stakeholder trust.")

    return score, feedback

if st.button("Submit Choices"):
    if username.strip() == "":
        st.warning("Please enter your name before submitting.")
    else:
        score, feedback_msgs = evaluate_choices(comp_choice, audit_choice, sustain_choice)
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

        if score <= 2:
            st.info("Your decisions show room for improvement. Consider aligning more closely with governance best practices.")
        elif score <= 4:
            st.info("Your decisions reflect a balanced approach. There's potential to strengthen governance alignment.")
        else:
            st.success("Excellent choices! Your decisions strongly align with good governance principles.")

        if feedback_msgs:
            st.subheader("Suggestions for Improvement")
            for msg in feedback_msgs:
                st.write(f"- {msg}")

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

    comp_df = df['Compensation'].value_counts().reset_index()
    comp_df.columns = ['Compensation Type', 'Count']
    st.plotly_chart(px.bar(comp_df, x='Compensation Type', y='Count', title='Compensation Choices'))

    audit_df = df['Audit'].value_counts().reset_index()
    audit_df.columns = ['Audit Type', 'Count']
    st.plotly_chart(px.bar(audit_df, x='Audit Type', y='Count', title='Audit Policy Choices'))

    sustain_df = df['Sustainability'].value_counts().reset_index()
    sustain_df.columns = ['Sustainability Strategy', 'Count']
    st.plotly_chart(px.bar(sustain_df, x='Sustainability Strategy', y='Count', title='Sustainability Strategy Choices'))

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download All Responses as CSV", data=csv, file_name="class_responses.csv", mime="text/csv")

if st.button("Reset All Responses"):
    st.session_state.responses = []
    st.session_state.start_time = datetime.now()
    st.success("All responses have been cleared.")