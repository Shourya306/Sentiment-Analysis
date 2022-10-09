from tkinter import Button
import streamlit as st
from textblob import TextBlob

st.title('Sentiment Analysis')

res = st.text_area('How was your day?')

if st.button('Submit'):
    blob = TextBlob(res)
    sent = blob.sentiment.polarity
    st.write(f'Sentiment score: {sent}')
    if sent >= 0.5:
        st.success('Positive')
    elif sent <= -0.5:
        st.error('Negetive')
    else:
        st.warning('Netural')