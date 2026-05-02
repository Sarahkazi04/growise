import streamlit as st
from PIL import Image

st.set_page_config(page_title="Future Vision", page_icon="🚀", layout="wide")

logo = Image.open("assets/logo.png")
st.image(logo, width=120)

st.title("🚀 Future Vision of Growise")

st.write("""
Growise is currently developed as a functional MVP prototype focused on vegetable recognition, weight estimation, and expiry tracking.

However, Growise is designed to evolve into a complete AI-powered household grocery management ecosystem.
""")

st.markdown("## 🔮 Upcoming Integrations")

c1, c2 = st.columns(2)

with c1:
    st.subheader("📲 WhatsApp Grocery Import")
    st.write("Users can directly import grocery lists received on WhatsApp.")

    st.subheader("🎤 Voice Grocery Notes")
    st.write("Speak your grocery list and Growise stores it automatically.")

    st.subheader("🥗 Nutrition Weekly Summary")
    st.write("Track vegetable consumption and receive healthy food suggestions.")

with c2:
    st.subheader("🚚 Vendor Home Delivery")
    st.write("Partnering with local vendors for smart doorstep vegetable delivery.")

    st.subheader("🔔 Smart Expiry Notifications")
    st.write("Automatic alerts before vegetables spoil.")

    st.subheader("💰 Price Comparison")
    st.write("AI-based estimated market price to avoid overpaying.")

st.markdown("## 💼 Business Potential")

st.write("""
Growise can generate revenue through:

• Vendor delivery commission  
• Premium household subscription  
• Sponsored grocery promotions  
• Data-driven smart shopping recommendations
""")

st.success("Growise Vision: Building India's Smartest AI Grocery Assistant for Every Home.")