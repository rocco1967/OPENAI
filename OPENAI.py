# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import openai
import pandas as pd
import streamlit as st

openai.api_key = "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"
model_engine = "text-davinci-003"
prompt = 'consigli per la corsa'
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.9,
)
st.write( completions.choices[0].text)
#message = (completions.choices[0].text)
