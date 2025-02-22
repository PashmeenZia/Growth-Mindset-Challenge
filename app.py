# streamlit
import streamlit as st

# Page Config
st.set_page_config(page_title="Growth Mindset Project", page_icon="⭐")

# Custom CSS for Colors
st.markdown("""
    <style>
        .main-title { color: #FF5733; font-size: 30px; font-weight: bold; }
        .header { color: #4CAF50; font-size: 24px; font-weight: bold; }
        .quote { color: #008CBA; font-size: 20px; font-style: italic; }
        .footer { color: #DAA520; font-size: 18px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-title">Growth Mindset Challenge: Web App with Streamlit</h1>', unsafe_allow_html=True)

# Welcome Section
st.markdown('<h2 class="header">🚀 Welcome to Your Growth Journey!</h2>', unsafe_allow_html=True)
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟")

# Quote Section
st.markdown('<h2 class="header">✨ Inspiring Thought for Today</h2>', unsafe_allow_html=True)
st.markdown('<p class="quote">“It is not in the stars to hold our destiny, but in ourselves.” — William Shakespeare</p>', unsafe_allow_html=True)

# Challenge Section
st.markdown('<h2 class="header">🔥 Face Your Challenge Head-On!</h2>', unsafe_allow_html=True)
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 You are facing: {user_input}. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection Section
st.markdown('<h2 class="header">🧠 Reflect & Grow!</h2>', unsafe_allow_html=True)
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experience helps you grow! Share your difficulties.")

# Achievements Section
st.markdown('<h2 class="header">🎯 Your Success Matters!</h2>', unsafe_allow_html=True)
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🎉 Amazing! You achieved: {achievement}")
else:
    st.info("Success comes in all sizes! What’s something you’re proud of? 🎉")

# Footer
st.write(" - - - ")
st.markdown('<p class="footer">🚀 Believe in yourself — every step counts! ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="credit">✨ Created by PashmeenZia ✨</p>', unsafe_allow_html=True)