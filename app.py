import streamlit as st
from gtts import gTTS

st.title("تعليم النطق للحروف العربية")

st.title("تقسيم حروف الكلمة")
      
word = st.text_input("اكتب الكلمة المراد تقسيمها الى احرف")

if word:
      for char in word:
              tts = gTTS(text=char, lang='ar')
              tts.save(f"file_{char}.mp3")
              st.audio(f"file_{char}.mp3")

      tts = gTTS(text=word, lang='ar')
      tts.save("word.mp3")
      st.audio("word.mp3")
      
st.title("نطق الاحرف")
      
vowels = ["ا", "و", "ي"]

def pronounce_arabic_letter_with_vowel(letter, vowel):
    tts = gTTS(text=letter + vowel, lang='ar')
    tts.save(f"file_{vowel}.mp3")
    st.audio(f"file_{vowel}.mp3")



# Create a list of Arabic letters
arabic_letters = ["ا", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "ه", "و", "ي"]

# Create a dropdown list with the Arabic letters
letter_dropdown = st.selectbox("اختر احد الحروف", arabic_letters)

# If a letter is selected, pronounce it with all three vowels
if letter_dropdown:
    st.write(f"لقد اخترت الحرف: {letter_dropdown}")
    for vowel in vowels:
        pronounce_arabic_letter_with_vowel(letter_dropdown, vowel)



