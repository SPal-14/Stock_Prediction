import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance
from keras.models import load_model

start = '2010-01-01'
end = '2019-12-31'
st.title("Stock Trend Prediction")
user_input = st.text_input('Enter Stock Ticker','AAPL')
df = yfinance.download(user_input, start=start, end=end)

st.subheader('Data From 2010 - 2019')
st.write(df.describe())

st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)