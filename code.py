#Imports streamlit to make website
import streamlit as st 

#Import translator
from deep_translator import GoogleTranslator

#List of supported languages
langList = ('english','hindi','afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'ukrainian', 'urdu', 'uzbek', 'vietnamese', 'welsh', 'xhosa','yiddish', 'yoruba', 'zulu')
lang = "english"
page = "Home"

#Translator methods
def trans_title(text):
  translate = GoogleTranslator(source="english",target=lang).translate(text=text)
  st.title(str(translate))

def trans_sub(text):
  translate = GoogleTranslator(source="english",target=lang).translate(text=text)
  st.subheader(str(translate))

def trans_write(text):
  translate = GoogleTranslator(source="english",target=lang).translate(text=text)
  st.write(str(translate))

#Logo, should be on every page of the website
def logo_header():
  st.image('med3.png', width = 160)

#Home Page
def home_page(lang):
  logo_header()

  #Title
  text = "Welcome to MedlingoHealth!"
  trans_title(text)

  #Subheader
  text = "Your personal healthcare companion"
  trans_sub(text)
  #Welcome Statement
  text = "Welcome to MedlingoHealth! Our goal is to develop a real-time translation tool specifically for medical terminology. This could help healthcare workers communicate more effectively with patients who speak different languages. The tool could be integrated into existing healthcare systems to facilitate seamless communication. Please proceed to the chatbot for assistance with your symptoms." 
  trans_write(text)
  st.text("")
  st.image("Doctor-and-patient.jpg", width = 700)
 
#About Page and FAQs
def about_faqs(lang):

  #Logo at the top
  logo_header()

  #Title
  text = "About Us"
  trans_title(text)
  
  #Splits our mission and our vision into two columns
  col1, col2 = st.columns(2) 
  with col1:
    text = "Our Mission: To create a chatbot capable of diagnosing common illnesses without language barriers."
    trans_sub(text)
  with col2:
    text = "Our Vision: To break down the communication barrier between health care professionals and patients with a technology oriented solution, promoting health for people around the globe. "
    trans_sub(text)
  
  #Final paragraph
  text = "Our team is composed of a diverse group of healthcare professionals and patients who share a passion to help YOU improve your healthcare experience. We are committed to providing the best possible experience for our users. We believe in the best for YOU."
  trans_write(text)

  


#Chatbot
def chatbot(lang):
  
  #Logo
  logo_header()

  #Title
  text = "Welcome to the Medlingo Health Chatbot!"
  trans_title(text)
  
  #List of possible symptoms
  sym = ["Runny nose", "Red, swollen eyes", "Itchy eyes or nose", "Cough", "Sore throat", "Sneezing", "Aches and pains", "Pain when swallowing", "Fever", "Swollen lymph nodes", "Headache", "Fatigue", "Chills", "Shortness of breath", "Loss of taste or smell", "Wheezing", "Mild to moderate chest discomfort", "Rash", "Nausea/vomiting"] 
  
  #Loop that translates each symptom
  for i in sym:
    text = sym[sym.index(i)]
    translate = GoogleTranslator(source="english", target=lang).translate(text = text)
    sym[sym.index(i)] = translate
  
  #List of different onset times
  ons = ["Abrupt (the same day)", "Quick (1-2 days)", "Gradual (2-14 days)"] 
  
  #Translates each onset time
  for i in ons:
    text = ons[ons.index(i)]
    translate = GoogleTranslator(source="english", target=lang).translate(text = text)
    ons[ons.index(i)] = translate 
  
  #Splits symptoms and onset into two columns
  col1, col2 = st.columns(2) 
  with col1:
    with st.chat_message("assistant"):
      text = "What are your symptoms? For best results, please select all of your symptoms."
      trans_write(text)

    #Checkboxes for each symptom
    runny_nose = st.checkbox(sym[0])
    eyes = st.checkbox(sym[1])
    eyes_itch = st.checkbox(sym[2])
    cough =  st.checkbox(sym[3])
    throat =  st.checkbox(sym[4])
    sneezing =  st.checkbox(sym[5])
    aches =  st.checkbox(sym[6])
    swallow =  st.checkbox(sym[7])
    fever =  st.checkbox(sym[8])
    lymph =  st.checkbox(sym[9])
    headache =  st.checkbox(sym[10])
    fatigue =  st.checkbox(sym[11])
    chills =  st.checkbox(sym[12])
    breath =  st.checkbox(sym[13])
    loss =  st.checkbox(sym[14])
    wheezing =  st.checkbox(sym[15])
    chest =  st.checkbox(sym[16])
    rash =  st.checkbox(sym[17])
    nausea =  st.checkbox(sym[18])
  
  #Checkboxes for each onset times
  with col2:
    with st.chat_message("assistant"):
      text = "How quick was the onset of your symptoms?"
      trans_write(text)
    abrupt = st.checkbox(ons[0])
    quick = st.checkbox(ons[1])
    gradual = st.checkbox(ons[2]) 

  #Ensures that diagnosis does not appear until user is done inputting symptoms
  if st.button("Done"): 

    #Symptoms for seasonal allergies
    if sum([int(abrupt), int(throat), int(runny_nose)]) == 3:
      with st.chat_message("assistant"):
        text = "Seems like you have seasonal allergies"
        trans_write(text)

    #Symptoms for cold
    elif sum([int(gradual), int(runny_nose), int(sneezing), int(throat)]) == 4:
      with st.chat_message("assistant"):
        text = "Seems like you have a cold"
        trans_write(text)

    #Symptoms for strep throat
    elif sum([int(abrupt), int(throat), int(swallow), int(fever), int(lymph)]) == 5:
      with st.chat_message("assistant"):
        text = "Seems like you have strep throat"
        trans_write(text)

    #Symptoms for the flu
    elif sum([int(quick), int(fever), int(headache), int(cough), int(aches)]) == 5:
      with st.chat_message("assistant"):
        text = "Seems like you have the flu"
        trans_write(text)

    #Symptoms for COVID-19
    elif sum([int(gradual), int(fever), int(cough), int(loss)]) == 4:
      with st.chat_message("assistant"):
        text = "Seems like you have COVID-19"
        translate = GoogleTranslator(source="english", target=lang).translate(text = text)
        trans_write(text)

    #Message if none of the symptoms match with a diagnosis
    else:
      with st.chat_message("assistant"):
        text = "Hmmmmm, we could't find an exact diagnosis. Please try again or contact your primary physician."
        trans_write(text)
    
    #Liability message
    with st.chat_message("assistant"):
      text = "Remember that Medlingo Health may not be 100% accurate with your diagnosis. Please confirm all diagnoses with a secondary qualified medical professional."
      trans_write(text)

#Sidebar for user navigation
def sidebar():
  
    #Defines lang as a global variable
    global lang

    page_list = ["Home", "About Us", "Chat"]
    lang = st.sidebar.selectbox('Language', langList)
    for i in page_list:
      text = page_list[page_list.index(i)]
      translate = GoogleTranslator(source="english", target=lang).translate(text = text)
      page_list[page_list.index(i)] = translate

    if 'index' not in st.session_state:
      st.session_state['index'] = 0

    page = st.sidebar.selectbox("Go to", page_list, index = st.session_state['index'])

    #Translates each page name

    if page == page_list[0]:
      index = 0
      home_page(lang)
    if page == page_list[1]:
      index = 1
      about_faqs(lang)
    if page == page_list[2]:
      index = 2
      chatbot(lang)

    st.session_state['index'] = index
  
sidebar() 
