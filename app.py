import streamlit as st
from PIL import Image
import numpy as np
import cv2
from skimage.metrics import structural_similarity as ssim

st.set_page_config(page_title="Growise", page_icon="🌿", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}
.big-title {
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#2e7d32;
}
.tagline {
    text-align:center;
    font-size:20px;
    color:#4b4b4b;
    margin-bottom:20px;
}
.section-box {
    background-color:#f1fff1;
    padding:25px;
    border-radius:18px;
    margin-top:20px;
    margin-bottom:20px;
}
.scan-box {
    background-color:#ffffff;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 0px 15px rgba(0,0,0,0.08);
}
.feature {
    background-color:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 0px 10px rgba(0,0,0,0.06);
    text-align:center;
}
.centered {
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
veg_data = {
    "tomato": {"weight": "150g - 250g", "expiry": "Best consumed within 4 days"},
    "potato": {"weight": "100g - 300g", "expiry": "Best consumed within 10 days"},
    "lauki": {"weight": "400g - 700g", "expiry": "Best consumed within 5 days"},
    "bhindi": {"weight": "200g - 350g", "expiry": "Best consumed within 3 days"}
}

reference_images = {
    "tomato": cv2.imread("data/tomato.png"),
    "potato": cv2.imread("data/potato.png"),
    "lauki": cv2.imread("data/lauki.png"),
    "bhindi": cv2.imread("data/bhindi.png")
}

def compare_images(uploaded, reference):
    uploaded = cv2.resize(uploaded, (200, 200))
    reference = cv2.resize(reference, (200, 200))

    uploaded_gray = cv2.cvtColor(uploaded, cv2.COLOR_BGR2GRAY)
    reference_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
    shape_score, _ = ssim(uploaded_gray, reference_gray, full=True)

    hist_uploaded = cv2.calcHist([uploaded], [0,1,2], None, [8,8,8], [0,256,0,256,0,256])
    hist_reference = cv2.calcHist([reference], [0,1,2], None, [8,8,8], [0,256,0,256,0,256])

    cv2.normalize(hist_uploaded, hist_uploaded)
    cv2.normalize(hist_reference, hist_reference)

    color_score = cv2.compareHist(hist_uploaded, hist_reference, cv2.HISTCMP_CORREL)

    return (0.5 * shape_score) + (0.5 * color_score)

# ---------- LOGO + BANNER ----------
logo = Image.open("assets/logo.png")
st.image(logo, width=130)

banner = Image.open("assets/banner.jpg")
st.image(banner, use_container_width=True)

st.markdown("<div class='big-title'>Growise</div>", unsafe_allow_html=True)
st.markdown("<div class='tagline'>Your Smart Grocery Companion</div>", unsafe_allow_html=True)

st.markdown("""
<div class='centered'>
Growise is an AI-powered smart grocery companion designed to transform everyday vegetable shopping into a faster, smarter, and waste-free experience.
</div>
""", unsafe_allow_html=True)

# ---------- SCANNER ----------
st.markdown("<div class='section-box'>", unsafe_allow_html=True)
st.markdown("## 📸 AI Vegetable Scanner")
st.write("Choose your preferred scanning method below.")

scan_option = st.radio("Select Option", ["Upload Vegetable Image", "Scan with Live Camera"])

input_image = None

if scan_option == "Scan with Live Camera":
    camera_photo = st.camera_input("Open Camera and Capture Vegetable")
    if camera_photo is not None:
        input_image = Image.open(camera_photo).convert("RGB")

else:
    uploaded_file = st.file_uploader("Choose Vegetable Image", type=["jpg","jpeg","png"])
    if uploaded_file is not None:
        input_image = Image.open(uploaded_file).convert("RGB")

if input_image is not None:
    st.image(input_image, caption="Scanned Vegetable", width=280)

    uploaded_cv = np.array(input_image)
    uploaded_cv = cv2.cvtColor(uploaded_cv, cv2.COLOR_RGB2BGR)

    best_match = None
    best_score = -999

    for veg, ref_img in reference_images.items():
        score = compare_images(uploaded_cv, ref_img)
        if score > best_score:
            best_score = score
            best_match = veg

    st.success(f"✅ Vegetable Identified: {best_match.capitalize()}")
    st.success(f"⚖ Estimated Weight: {veg_data[best_match]['weight']}")
    st.success(f"⏳ Expiry Reminder: {veg_data[best_match]['expiry']}")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- WHY GROWISE ----------
st.markdown("## ✨ Why Growise?")

c1, c2, c3 = st.columns(3)

with c1:
    dimg = Image.open("assets/detect.jpg")
    st.image(dimg, use_container_width=True)
    st.subheader("🔍 Smart Detection")
    st.write("Instantly identify vegetables through one simple scan.")

with c2:
    fimg = Image.open("assets/fresh.jpg")
    st.image(fimg, use_container_width=True)
    st.subheader("⏳ Freshness Tracking")
    st.write("Know expiry timelines and reduce food waste.")

with c3:
    gimg = Image.open("assets/grocery.jpg")
    st.image(gimg, use_container_width=True)
    st.subheader("🛒 Better Grocery Decisions")
    st.write("Make smarter buying choices for your household.")

# ---------- TEAM ----------
st.markdown("## 👩‍💼 Meet the Minds Behind Growise")

f1, f2 = st.columns(2)

with f1:
    founder = Image.open("assets/founder.png")
    st.image(founder, width=220)
    st.subheader("Sarah Kazi")
    st.write("Founder of Growise")

with f2:
    mentor = Image.open("assets/mentor.png")
    st.image(mentor, width=220)
    st.subheader("Project Mentor")
    st.write("Technical & Strategic Guide")

# ---------- FUTURE ----------
st.markdown("## 🚀 Upcoming Future Integrations")

u1, u2, u3 = st.columns(3)

with u1:
    st.success("📲 WhatsApp Grocery List Import")

with u2:
    st.success("🎤 Voice Grocery Notes")

with u3:
    st.success("🚚 Vendor Home Delivery")

st.markdown("---")
st.markdown("<div class='centered'><b>Smart Shopping • Less Waste • Better Living</b></div>", unsafe_allow_html=True)