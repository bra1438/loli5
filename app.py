import streamlit as st
from gtts import gTTS

vowels = ["ا", "و", "ي"]

def pronounce_arabic_letter_with_vowel(letter, vowel):
    tts = gTTS(text=letter + vowel, lang='ar')
    tts.save(f"file_{vowel}.mp3")
    st.audio(f"file_{vowel}.mp3")

st.title("Arabic Letter Pronunciation")

letter = st.text_input("Enter an Arabic letter:")

if letter:
    for vowel in vowels:
        pronounce_arabic_letter_with_vowel(letter, vowel)

