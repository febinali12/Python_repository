import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="InvestBot", page_icon="💼", layout="wide")

# ---- FUND DATA ----
funds = {
    "alpha growth fund": {
        "type": "Equity",
        "return": "12% annual",
        "risk": "High",
        "min_investment": "$10,000",
        "description": "Focuses on high-growth tech and emerging companies."
    },
    "beta income fund": {
        "type": "Debt",
        "return": "6% annual",
        "risk": "Low",
        "min_investment": "$5,000",
        "description": "Stable income through government and corporate bonds."
    },
    "gamma balanced fund": {
        "type": "Hybrid",
        "return": "8% annual",
        "risk": "Medium",
        "min_investment": "$7,500",
        "description": "Mix of equity and debt for balanced growth."
    },
    "delta global fund": {
        "type": "International Equity",
        "return": "10% annual",
        "risk": "High",
        "min_investment": "$15,000",
        "description": "Invests in global markets including US and Europe."
    },
    "epsilon esg fund": {
        "type": "ESG",
        "return": "9% annual",
        "risk": "Medium",
        "min_investment": "$8,000",
        "description": "Focuses on environmentally and socially responsible companies."
    }
}

# ---- CHATBOT LOGIC ----


def get_response(user_input):
    user_input = user_input.lower()

    if "list" in user_input or "funds" in user_input:
        return "📊 Available Funds:\n\n" + "\n".join([f"- {f.title()}" for f in funds])

    for fund_name, details in funds.items():
        if fund_name in user_input:
            return f"""
### 📊 {fund_name.title()}

- **Type:** {details['type']}
- **Returns:** {details['return']}
- **Risk:** {details['risk']}
- **Minimum Investment:** {details['min_investment']}
- **About:** {details['description']}
"""

    return "🤖 I didn’t understand. Try typing **'list'** or ask about a specific fund."


# ---- SESSION STATE ----
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- TITLE ----
st.title("💼 InvestBot")
st.caption("Your AI Investment Assistant")

# ---- DISPLAY CHAT ----
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---- USER INPUT ----
if prompt := st.chat_input("Ask about funds..."):
    # user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # bot response
    response = get_response(prompt)
    st.session_state.messages.append(
        {"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
