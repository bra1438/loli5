import streamlit as st
from gtts import gTTS

def pronounce_arabic_letters(letters):
    for letter in letters:
        tts = gTTS(text=letter, lang='ar')
        tts.save("output.mp3")
        st.audio("output.mp3")

st.title("تعليم نطق الخروف العربية ")

letter = st.text_input("ادخل الحرف:")

if letter:
    pronounce_arabic_letters(letter)
