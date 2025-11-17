import streamlit as st

st.set_page_config(page_title="Revelion 2025-2026", layout="centered")

# Pink background
st.markdown("""
<style>
.stApp {
    background-color: #f7c1d9 !important;
    padding-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    "<h1 style='text-align:center; color:white;'>🎉 Revelion 2025 - 2026 🎉</h1>",
    unsafe_allow_html=True
)

# FUN GIF (functional)
st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
st.image("https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif", width=250)
st.markdown("</div>", unsafe_allow_html=True)

# Two images side-by-side
col1, col2 = st.columns(2)

with col1:
    st.image("https://raw.githubusercontent.com/ApostolAdinaDenisa/ANNOUNCEHAPPYNEWYEAR/main/photos/photos/weed1.png", width=250)

with col2:
    st.image("https://raw.githubusercontent.com/ApostolAdinaDenisa/ANNOUNCEHAPPYNEWYEAR/main/photos/photos/weed2.png", width=250)

# SPACE BEFORE BUTTON
st.markdown("<br><br>", unsafe_allow_html=True)

# Funny button section
st.markdown(
    "<h2 style='text-align:center; color:white;'>👇 Tap aici dacă ai curaj 😂👇</h2>",
    unsafe_allow_html=True
)

# Button
if st.button("🎊 REVELION 2025-2026 TAP HERE 🎊"):
    st.markdown(
        "<h2 style='text-align:center; color:white; font-weight:bold;'>"
        "😢❌ SORRY GUYS, DAR ANUL ACESTA NU VOM FI ÎMPREUNĂ ❌😢"
        "</h2>",
        unsafe_allow_html=True
    )
    st.image("https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif", width=250)
