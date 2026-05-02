import streamlit as st
from PIL import Image

st.set_page_config(page_title="About Growise", page_icon="🌿", layout="wide")

logo = Image.open("assets/logo.png")
founder = Image.open("assets/founder.png")
mentor = Image.open("assets/mentor.png")

st.image(logo, width=120)

st.title("🌿 About Growise")

st.write("""
Growise is an AI-powered smart grocery companion built to transform the way households purchase, identify, and manage vegetables.

From identifying vegetables through a single scan to helping users track freshness and reduce kitchen wastage, Growise combines convenience with sustainability.

Our goal is simple: make everyday grocery shopping smarter, faster, and more efficient.
""")

st.markdown("## 👩‍💼 Our Team")

col1, col2 = st.columns(2)

with col1:
    st.image(founder, width=250)
    st.subheader("Sarah Kazi")
    st.write("Founder")
    st.write("Building innovative practical solutions using technology for everyday household challenges.")

with col2:
    st.image(mentor, width=250)
    st.subheader("Project Mentor")
    st.write("Technical & Strategic Mentor")
    st.write("Providing product guidance, development support, and startup mentoring for Growise.")

st.markdown("## 🎯 Our Mission")

m1, m2, m3 = st.columns(3)

with m1:
    st.subheader("🛒 Smarter Shopping")
    st.write("Helping users identify and choose vegetables correctly.")

with m2:
    st.subheader("♻ Less Waste")
    st.write("Reducing spoilage through freshness reminders.")

with m3:
    st.subheader("⚡ Everyday Ease")
    st.write("Making grocery management simple for all households.")