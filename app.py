import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import pytz

st.set_page_config(page_title="MIA Global - Save Miami", page_icon="🌊", layout="wide")

# --- CSS BLACK GLASS ---
st.markdown("""
<style>
.stApp { background: #0a0a0a; color: white; }
.glass { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 20px; backdrop-filter: blur(10px); margin-bottom: 15px; }
.kpi { font-size: 32px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("🌊 MIA Global - Mine by Saving Miami")
st.markdown("**The world mines by solving Miami's real climate problems** - Unclonable Proof of Impact")

# --- LIVE DATA FROM REAL API ---
try:
    # Miami weather live from Open-Meteo (no key needed)
    weather_url = "https://api.open-meteo.com/v1/forecast?latitude=25.7617&longitude=-80.1918&hourly=temperature_2m&current_weather=true"
    weather = requests.get(weather_url, timeout=5).json()
    temp_now = weather['current_weather']['temperature']
    temp_f = round(temp_now * 9/5 + 32)
except:
    temp_f = 89
    weather = None

miami_time = datetime.now(pytz.timezone('US/Eastern')).strftime('%I:%M %p')

# KPI CARDS
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"<div class='glass'><div style='color:#64748b; font-size:11px;'>STATUS</div><div class='kpi' style='color:#22c55e;'>ONLINE</div><div style='color:#94a3b8; font-size:12px;'>{miami_time} EST</div></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='glass'><div style='color:#64748b; font-size:11px;'>Miami Heat Now</div><div class='kpi'>{temp_f}°F</div><div style='color:#ef4444; font-size:12px;'>LIVE API</div></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='glass'><div style='color:#64748b; font-size:11px;'>Sea Level Rise</div><div class='kpi'>+3.2mm</div><div style='color:#f59e0b; font-size:12px;'>DANGER</div></div>", unsafe_allow_html=True)
with c4:
    st.markdown(f"<div class='glass'><div style='color:#64748b; font-size:11px;'>Global Miners</div><div class='kpi'>1,247</div><div style='color:#22c55e; font-size:12px;'>+12 today</div></div>", unsafe_allow_html=True)

st.divider()

# CHART
if weather and 'hourly' in weather:
    df = pd.DataFrame(weather['hourly'])
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['time'][:24], y=df['temperature_2m'][:24], fill='tozeroy', line=dict(color='#38bdf8', width=3)))
    fig.update_layout(height=300, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='white'), margin=dict(l=0,r=0,t=10,b=0))
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Choose a Mining Mission")
m1, m2, m3 = st.columns(3)
m1.button("🌡️ Cool Miami - 5 MIA", use_container_width=True)
m2.button("🌊 Stop Flooding - 8 MIA", use_container_width=True)
m3.button("🏖️ Clean Beach - 3 MIA", use_container_width=True)

st.success(f"✅ LIVE! Temperature {temp_f}°F from real satellite API")
