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
st.subheader('To keep the service active make a small donation with PayPal.. Thank you')
st.success('gianfranco.fa@gmail.com')
#openai.api_key = os.getenv("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")
#os.environ["OPENAI_API_KEY"] = "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"
#openai.api_key = os.environ["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"]
#openai.api_key=st.secrets['OPEN_APY_KEY']
#openai.api_key = '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'#
#model_engine ="text-davinci-003"#text-curie-001"# "text-davinci-003"

st.subheader('For use and explanation models read this:')
st.success('https://beta.openai.com/docs/models/overview')
st.subheader('text-davinci-003.......IS THE ENGINE OF CHATGPT')


model_engine = st.radio(
    "CHOOSE THE MODEL OF A.I.",
    ('None','text-ada-001','text-davinci-002', 'text-davinci-003', 'code-cushman-001','text-curie-001'))
##########################################################
#name = st.text_input('Name')
if model_engine=='None' :
  st.warning('CHOSE A MODEL')
  st.stop()
st.success('Thank you for chose a Model')
###########################################################

openai.api_key=st.secrets['OPEN_APY_KEY']


    
prompt =st.text_area('YOUR REQUEST:')
#if prompt is not None:
completions = openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens=1024,n=1, stop=None,
                                      frequency_penalty=0.0,temperature=0.0,)#top_p=1
#message =(completions.choices[0].text)#
#st.write(message)
if st.button('RUN'):
    message =(completions.choices[0].text)#
    st.write(message)
#else:
    #st.write('inserisci la richiesta')
#text_contents = (message)
st.download_button('download the result on your PC.. After first sloping Run....',(completions.choices[0].text))





