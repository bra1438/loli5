import streamlit as st
from gtts import gTTS
from PIL import Image

#st.title("تعليم اللغة العربية")
st.title("Apprendre la langue arabe")

# Add a text input field
#text_input = st.text_input("مرحبا اكتب اسمك هنا")
text_input = st.text_input("Prenom : Zayneb / Soumaya / Abdallah")

# Set the background color of the app
st.markdown("""
<style>
body {
  background-color: #0000FF;
}
</style>
""", unsafe_allow_html=True)




# Add a button
button = st.button("ابدا")

# If the button is clicked, print the user's name
if button:
    #st.write(f"مرحبا بك {text_input}, سوف تتعلم معنا اساسيات اللغة العربية على القاعدة النورانية")
    st.write(f"مرحبا بك {text_input}, Tu va apprendre la langue Arabe et t'auras des surprises a chaque fois")


image = 'ar.jpg'

# Load the image
image = Image.open("ar.jpg")

# Display the image
st.image(image)

#st.subheader('تقسيم حروف الكلمة')  
st.subheader('Diviser les lettres du mot') 
#word = st.text_input("اكتب الكلمة المراد تقسيمها الى احرف")
word = st.text_input("Ecris le mot que tu veux diviser en lettre")

if word:
          for char in word:
                  tts = gTTS(text=char, lang='ar')
                  tts.save(f"file_{char}.mp3")
                  st.audio(f"file_{char}.mp3")

          #st.write("نطق الكلمة كاملة")
          st.write("Prononciation du mot en entier")
          tts = gTTS(text=word, lang='ar')
          tts.save("word.mp3")
          st.audio("word.mp3")

#st.subheader('نطق الأحرف')  
st.subheader('Prononciation des lettres') 
# Create a dropdownlist of Arabic letters
arabic_letters = st.multiselect("Select an Arabic letter:", ["أ", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "ه", "و", "ي"])

# If a letter is selected, print its code
if arabic_letters:
    for letter in arabic_letters:
        tts = gTTS(text=letter, lang='ar')
        tts.save("letter.mp3")
        st.audio("letter.mp3")            
            
#st.subheader("نطق الاحرف بالحركات / الفتحة - الضمة - الكسرة")
st.subheader("Prononciation des lettres avec voyelles")
vowels = ["ا", "و", "ي"]

def pronounce_arabic_letter_with_vowel(letter, vowel):
        tts = gTTS(text=letter + vowel, lang='ar')
        tts.save(f"file_{vowel}.mp3")
        st.audio(f"file_{vowel}.mp3")



# Create a list of Arabic letters
arabic_letters = ["أ", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر", "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ك", "ل", "م", "ن", "ه", "و", "ي"]

# Create a dropdown list with the Arabic letters
#letter_dropdown = st.selectbox("اختر احد الحروف", arabic_letters)
letter_dropdown = st.selectbox("Choisir une lettre pour ecouter comment la prononcer", arabic_letters)

# If a letter is selected, pronounce it with all three vowels
if letter_dropdown:
        st.write(f"لقد اخترت الحرف: {letter_dropdown}")
        st.write(f"Tu as choisi la lettre: {letter_dropdown}")
        for vowel in vowels:
            pronounce_arabic_letter_with_vowel(letter_dropdown, vowel)


