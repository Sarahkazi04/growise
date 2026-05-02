import streamlit as st
from PIL import Image

st.set_page_config(page_title="Expiry Tips", page_icon="⏳", layout="wide")

logo = Image.open("assets/logo.png")
st.image(logo, width=120)

st.title("⏳ Smart Expiry Management")

st.write("Growise helps users consume vegetables before spoilage by giving estimated freshness reminders.")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    img1 = Image.open("assets/tomato_card.png")
    st.image(img1, width=180)
    st.subheader("Tomato 🍅")
    st.write("Best consumed within 4 days")

with col2:
    img2 = Image.open("assets/potato_card.png")
    st.image(img2, width=180)
    st.subheader("Potato 🥔")
    st.write("Best consumed within 10 days")

with col3:
    img3 = Image.open("assets/lauki_card.png")
    st.image(img3, width=180)
    st.subheader("Lauki 🥒")
    st.write("Best consumed within 5 days")

with col4:
    img4 = Image.open("assets/bhindi_card.png")
    st.image(img4, width=180)
    st.subheader("Bhindi 🌶")
    st.write("Best consumed within 3 days")

st.success("This feature promotes smarter kitchen consumption and helps reduce everyday household food wastage.")