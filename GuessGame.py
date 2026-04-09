import streamlit as st
import random

# ===== Background Mario Style =====
page_bg = """
<style>
.stApp {
    background-color: #ffd6e7;
}

h1 {
    color: #ffcc00;
    text-align: center;
    text-shadow: 2px 2px #000;
}

.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    font-size: 18px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ===== Tajuk =====
st.title("🍄 Mario Guess The Number 🎯")

# Input nama player
name = st.text_input("Masukkan nama anda:")

# Simpan dalam session
if name:
    st.session_state.player_name = name

# ===== Init Game =====
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 25)
    st.session_state.attempts = 0

# ===== Input =====
guess = st.number_input("Pilih nombor (1 - 25):", 1, 25)

# ===== Check Button =====
if st.button("🎮 Teka!"):
    st.session_state.attempts += 1

    if guess < st.session_state.number:
        st.error("⬇️ Terlalu kecil!")
        st.snow()  # animation salah (snow effect)
        
    elif guess > st.session_state.number:
        st.error("⬆️ Terlalu besar!")
        st.snow()

    else:
        st.success(f"🎉 Betul! Anda menang dalam {st.session_state.attempts} cubaan!")
        st.balloons()  # animation menang 🎈

# ===== Reset =====
if st.button("🔄 Main semula"):
    st.session_state.number = random.randint(1, 25)
    st.session_state.attempts = 0
    st.rerun()