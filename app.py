# streamlit
import streamlit as st

# Page Config
st.set_page_config(page_title="Growth Mindset Project", page_icon="⭐")

# Custom CSS for Better Colors & Break Lines
st.markdown("""
    <style>
        .main-title { color: #6A5ACD; font-size: 30px; font-weight: bold; }
        .header { color: #5D3FD3; font-size: 24px; font-weight: bold; margin-top: 20px; }
        .quote { color: #4682B4; font-size: 20px; font-style: italic; font-weight: bold; }
        .footer { color: #DAA520; font-size: 18px; font-weight: bold; }
        .credit { color: #A0522D; font-size: 16px; font-weight: bold; text-align: center; margin-top: 20px; }
        .break-line { margin-top: 10px; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="main-title">🚀 Growth Mindset Challenge: Web App with Streamlit</div>', unsafe_allow_html=True)
st.markdown('<hr class="break-line">', unsafe_allow_html=True)

# Welcome Section
st.markdown('<div class="header">🌟 Welcome to Your Growth Journey!</div>', unsafe_allow_html=True)
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟")
st.markdown('<hr class="break-line">', unsafe_allow_html=True)

# Quote Section
st.markdown('<div class="header">✨ Inspiring Thought for Today</div>', unsafe_allow_html=True)
st.markdown('<div class="quote">“It is not in the stars to hold our destiny, but in ourselves.” — William Shakespeare</div>', unsafe_allow_html=True)
st.markdown('<hr class="break-line">', unsafe_allow_html=True)

# Challenge Section
st.markdown('<div class="header">🔥 Face Your Challenge Head-On!</div>', unsafe_allow_html=True)
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 You are facing: {user_input}. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")
st.markdown('<hr class="break-line">', unsafe_allow_html=True)

# Reflection Section
st.markdown('<div class="header">🧠 Reflect & Grow!</div>', unsafe_allow_html=True)
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experience helps you grow! Share your difficulties.")
st.markdown('<hr class="break-line">', unsafe_allow_html=True)

# Achievements Section
st.markdown('<div class="header">🎯 Your Success Matters!</div>', unsafe_allow_html=True)
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🎉 Amazing! You achieved: {achievement}")
else:
    st.info("Success comes in all sizes! What’s something you’re proud of? 🎉")
st.markdown('<hr class="break-line">', unsafe_allow_html=True)

# Footer
st.write(" - - - ")
st.markdown('<div class="footer">🚀 Believe in yourself — every step counts! ✨</div>', unsafe_allow_html=True)
st.markdown('<hr class="break-line">', unsafe_allow_html=True)

# Created by PashmeenZia
st.markdown('<div class="credit">✨ Created by PashmeenZia ✨</div>', unsafe_allow_html=True)
