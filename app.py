import streamlit as st
from gtts import gTTS

def pronounce_arabic_letters(letters):
    for letter in letters:
        tts = gTTS(text=letter, lang='ar')
        tts.save("output.mp3")
        st.audio("output.mp3")

st.title("Arabic Letter Pronunciation")

letter = st.text_input("Enter an Arabic letter:")

if letter:
    pronounce_arabic_letters(letter)



def pronounce_arabic_letter_with_vowel(letter, vowel):
    for vowel in vowels:
        tts = gTTS(text=letter + vowel, lang='ar')
        tts.save(f"file_{vowel}.mp3")
        st.audio(f"file_{vowel}.mp3")
vowels = ["ا", "و", "ي"]
st.title("Arabic Letter Pronunciation")

letter = st.text_input("Enter an Arabic letter:")

if letter:
    pronounce_arabic_letter_with_vowel(letter)
