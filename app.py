import streamlit as st
from gtts import gTTS
import os

vowels = ["ا", "و", "ي"]
def pronounce_arabic_letter_with_vowel(letter, vowel):
    for vowel in vowels:
        tts = gTTS(text=letter + vowel, lang='ar')
        tts.save(f"file_{vowel}.mp3" )
        st.audio(f"file_{vowel}.mp3")

st.title("تعليم نطق الخروف العربية ")

letter = st.text_input("ادخل الحرف:")

if letter:
    pronounce_arabic_letter_with_vowel(letter, vowel)
