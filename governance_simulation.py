
import streamlit as st

st.title("Corporate Governance Simulation")

st.write("Welcome to the Governance Simulation! You are a board member making key decisions for a multinational firm. Your choices will impact shareholder satisfaction and firm performance.")

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

def evaluate_choices(comp, audit, sustain):
    score = 0
    feedback = []

    if comp == "Stock options with long-term vesting":
        score += 2
        feedback.append("Long-term incentives align management with shareholder interests.")
    elif comp == "Performance-based bonuses tied to financial metrics":
        score += 1
        feedback.append("Performance-based bonuses encourage results but may focus on short-term gains.")
    else:
        feedback.append("Fixed salaries may not motivate executives to maximize shareholder value.")

    if audit == "Real-time external audit with board oversight":
        score += 2
        feedback.append("Strong audit practices enhance transparency and investor confidence.")
    elif audit == "Annual external audit":
        score += 1
        feedback.append("Annual audits are standard but may miss real-time issues.")
    else:
        feedback.append("Internal audits alone may lack independence and credibility.")

    if sustain == "Integrate profit, environment, and social development":
        score += 2
        feedback.append("Comprehensive sustainability strategy improves reputation and long-term viability.")
    elif sustain == "Balance profit with environmental goals":
        score += 1
        feedback.append("Balancing profit and environment is a step toward responsible governance.")
    else:
        feedback.append("Ignoring sustainability may harm reputation and long-term performance.")

    return score, feedback

if st.button("Submit Choices"):
    total_score, feedback_messages = evaluate_choices(comp_choice, audit_choice, sustain_choice)
    st.subheader("Simulation Results")
    st.write(f"Shareholder Satisfaction Score: {total_score} / 6")
    for msg in feedback_messages:
        st.write(f"- {msg}")
