import streamlit as st
from textblob import TextBlob
from cleantext import clean


st.title('Sentiment Analysis')

def sentiment_analysis(text):
    cle = clean(text,no_punct=True, lower=False)
    blob = TextBlob(cle)
    sent = blob.sentiment.polarity
    st.write(f'Sentiment score: {sent}')
    if sent >= 0.5:
         st.success('Positive')
    elif sent <= -0.5:
         st.error('Negetive')
    else:
         st.warning('Netural')

st.write(sentiment_analysis(st.text_area('How was your day?')))

txt = st.text_area('Text')
if st.button('Analysize'):
    st.write(sentiment_analysis(txt))

