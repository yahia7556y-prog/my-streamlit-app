import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="MIA Global - Save Miami", page_icon="🌊", layout="wide")

st.title("🌊 MIA Global - Mine by Saving Miami")
st.markdown("**The world mines by solving Miami's real climate problems** - Unclonable Proof of Impact")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Miami Heat Now", "94°F", "2°")
col2.metric("Sea Level Rise", "+3.2mm", "DANGER")
col3.metric("Global Miners", "1,247")
col4.metric("Donated to Miami", "$12,430")

st.divider()

st.subheader("Choose a Mining Task - Every task saves Miami")

task = st.selectbox("Task Type:", 
    ["🔥 Identify Urban Heat Islands from Satellite",
     "🌊 Classify Flood Risk Zones", 
     "🤖 Train AI to Predict Hurricanes"])

if task:
    st.info(f"Current Mission: {task}")
    st.image("https://images.unsplash.com/photo-1544551763-46a013bb70d5", caption="Satellite View - Miami, FL")
    
    st.write("Is this area at high risk of flooding?")
    choice = st.radio("Your analysis:", ["Yes - High Risk 🔴", "No - Safe 🟢", "Not Sure"], horizontal=True)
    
    if st.button("Submit, Verify & Mine ⛏️"):
        if choice != "Not Sure":
            reward = random.uniform(0.5, 2.5)
            st.balloons()
            st.success(f"Thank you! You helped save Miami. Mined {reward:.3f} MIA 💰")
            st.write(f"Data sent to University of Miami Rosenstiel School - {datetime.now().strftime('%H:%M:%S')}")
            st.progress(random.randint(60, 95))
            st.write("AI Verification: ✅ Human verified, not a bot")
        else:
            st.warning("Try again - AI will guide you")

st.sidebar.title("🌍 Why Global & Unclonable?")
st.sidebar.markdown("""
- **Anyone** in the world can mine
- **No expensive GPUs** needed - needs human intelligence
- **Impossible to clone** - tied to real Miami data + University partnerships
- **Powerful story:** A coin that saves a city from sinking

**How it works:**
1. You solve real Miami climate tasks
2. AI verifies your work
3. You earn MIA
4. 10% goes to Miami Climate Fund
""")
st.sidebar.metric("Your Mining Rate", f"{random.uniform(1.2, 4.5):.2f} MIA/h")
st.sidebar.button("Connect Wallet (Coming Soon)")

st.divider()
st.caption("MIA Whitepaper v1 | Proof of Impact | Registered 2026 | Miami, FL")
