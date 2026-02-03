import streamlit as st
import random
import time
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

st.set_page_config(page_title="💌 For Ayoola", page_icon="❤️", layout="centered")

# ------------------ Styling ------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffe6eb, #fff5f7);
}
.big {
    font-size: 32px;
    font-weight: bold;
}
.soft {
    font-size: 20px;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #ffffffcc;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ------------------ Session State ------------------
if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "no_clicks" not in st.session_state:
    st.session_state.no_clicks = 0

if "button_shift" not in st.session_state:
    st.session_state.button_shift = random.randint(1, 3)

# ------------------ App ------------------
st.markdown("<div class='big'>💖 Hey Ayoola 😊</div>", unsafe_allow_html=True)

if not st.session_state.accepted:
    st.markdown("<div class='soft'>Will you be my Val? 🌹</div>", unsafe_allow_html=True)
    st.write("")

    cols = st.columns(5)

    # YES button (stable)
    with cols[1]:
        if st.button("💘 Yes"):
            st.session_state.accepted = True
            st.balloons()

    # NO button (moves)
    with cols[st.session_state.button_shift]:
        if st.button("No 😅"):
            st.session_state.no_clicks += 1
            st.session_state.button_shift = random.randint(0, 4)

            st.warning(random.choice([
                "Oops… that button moved 😄",
                "Nice try, Ayoola 😉",
                "The universe redirected that choice 💫",
                "Hmm… that didn’t land 😌",
                "Retry unlocked 😄"
            ]))

else:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## 🎉 IT’S A YES! 🎉")
    st.markdown("### Ayoola just unlocked Valentine mode 💕")

    # Countdown
    valentine_date = datetime(datetime.now().year, 2, 14)
    days_left = (valentine_date - datetime.now()).days

    if days_left >= 0:
        st.markdown(f"⏳ **{days_left} days to Valentine’s Day**")
    else:
        st.markdown("💖 Valentine’s Day is here!")

    # Venue picker
    venue = st.selectbox(
        "Pick the Valentine venue:",
        [
            "🍽️ A cozy restaurant",
            "🎬 Movie night",
            "🌅 Beach evening",
            "☕ Coffee & deep conversations",
            "🎶 Live music / concert"
        ]
    )

    st.success(f"✨ Venue selected: {venue}")
    st.markdown("</div>", unsafe_allow_html=True)

    # ------------------ Save-the-Date Card ------------------
    st.write("")
    st.markdown("### 📸 Save-the-Date Card")

    img = Image.new("RGB", (600, 400), "#ffe6eb")
    draw = ImageDraw.Draw(img)

    try:
        font_big = ImageFont.truetype("arial.ttf", 40)
        font_small = ImageFont.truetype("arial.ttf", 24)
    except:
        font_big = font_small = ImageFont.load_default()

    draw.text((150, 60), "SAVE THE DATE 💖", fill="#b3003b", font=font_big)
    draw.text((170, 140), "Ayoola’s Valentine", fill="#000000", font=font_small)
    draw.text((140, 190), f"Venue: {venue}", fill="#000000", font=font_small)
    draw.text((190, 240), "February 14", fill="#000000", font=font_small)

    st.image(img)
    st.caption("You can screenshot or download this card 📷")

    st.markdown("💝 Made with creativity, courage, and code.")