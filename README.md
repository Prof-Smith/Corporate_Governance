
# Corporate Governance Simulation

This Streamlit app simulates decision-making in corporate governance. Students act as board members and make choices on:
- Executive compensation
- Audit policy
- Sustainability strategy

## Scoring Mechanism
Each decision contributes to a total score out of 6:
- **Executive Compensation**
  - Fixed salary: 0 points
  - Performance-based bonuses: 1 point
  - Stock options with long-term vesting: 2 points
- **Audit Policy**
  - Internal audit only: 0 points
  - Annual external audit: 1 point
  - Real-time external audit with board oversight: 2 points
- **Sustainability Strategy**
  - Profit-only focus: 0 points
  - Profit + environmental goals: 1 point
  - Profit + environment + social development: 2 points

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   streamlit run governance_simulation.py
   ```

## Educational Use
Use this app to facilitate classroom discussions on corporate governance and evaluate students' understanding of best practices.
