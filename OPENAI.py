# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import openai
import pandas as pd
import streamlit as st
import os
from PIL import Image
st.header('.....................My name is Ambrose..................')
st.subheader('.............................I^m here to serve you...........................')
st.subheader('I am an advanced neural network specialized in responding in natural language')
image=Image.open('concierge.JPG')#('sfera.JPG')
image = image.resize((1000, 400))
st.image(image)
#openai.api_key = os.getenv("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")
#os.environ["OPENAI_API_KEY"] = "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"
#openai.api_key = os.environ["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"]
openai.api_key=st.secrets['OPEN_APY_KEY']
#openai.api_key = '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'
model_engine = "text-davinci-003"
prompt =st.text_input('inserisci la richiesta:','ciao come stai' )
#if prompt is not None:
completions = openai.Completion.create(engine=model_engine,prompt=prompt,max_tokens=512,n=10, stop=None,top_p=1.0,temperature=0.5,)
message =(completions.choices[0].text)
st.write(message)
#else:
    #st.write('inserisci la richiesta')

    
