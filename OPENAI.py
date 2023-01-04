# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import openai
import pandas as pd
import streamlit as st
import os
#openai.api_key = os.getenv("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")
#os.environ["OPENAI_API_KEY"] = "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"
#openai.api_key = os.environ["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"]
openai.api_key = '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'
model_engine = "text-davinci-003"
prompt = st.text_input('inserisci la richiesta:')
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.9,
)

message = completions.choices[0].text
st.write(message)
