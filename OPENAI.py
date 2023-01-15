# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import openai
import pandas as pd
import streamlit as st
import os
import numpy as np
from PIL import Image
st.header('.....................My name is Ambrose..................')
st.subheader('.............................I^m here to serve you...........................')
st.subheader('I am an advanced neural network specialized in responding in natural language')
image=Image.open('concierge.JPG')#('sfera.JPG')
image = image.resize((1000, 400))
st.image(image)
st.subheader('To keep the service active and pay OPENAI.com make a small donation with PayPal.. Thank you')
st.success('gianfranco.fa@gmail.com')
#openai.api_key = os.getenv("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")
#os.environ["OPENAI_API_KEY"] = "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"
#openai.api_key = os.environ["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"]
#openai.api_key=st.secrets['OPEN_APY_KEY']
#openai.api_key = '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'#
#model_engine ="text-davinci-003"#text-curie-001"# "text-davinci-003"
model_engine = st.radio(
    "scegli il modello AI",
    ('text-davinci-002', 'text-davinci-003', 'code-davinci-002','code-cushman-001','text-curie-001'))
openai.api_key=st.secrets['OPEN_APY_KEY']


    
prompt =st.text_area('inserisci la richiesta')
#if prompt is not None:
completions = openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens=512,n=1, stop=None,
                                      frequency_penalty=0.0,temperature=0.5,)#top_p=1
#message =(completions.choices[0].text)#
#st.write(message)
if st.button('RUN'):
    message =(completions.choices[0].text)#
    st.write(message)
#else:
    #st.write('inserisci la richiesta')
#text_contents = (message)
st.download_button('download the result on your PC.. After first sloping Run....',(completions.choices[0].text))



#from audio_recorder_streamlit import audio_recorder#####
#import speech_recognition as sr
#audio_bytes = audio_recorder()####
#if audio_bytes:######
    #st.audio(audio_bytes, format="audio/wav")######
    
#import whisper############################################################################

#model = whisper.load_model('base')
#st.text('language recognition model loaded')
#if st.button('TRANSCRIBE FILE'):
    #if audio_file is not None:
        #st.success('TRANSCRIBENG FILE')
        #audio_bytes = audio_file.read()#####
        #transcription=model.transcribe((audio_file.name))####
        #st.success('TRANSCRIPTION COMPLETE')
        #st.markdown(transcription['text'])
    #else:
        #st.error('PLEASE UPLOAD FILE')
#st.header('Play Original File')
#st.audio(audio_file)
