import streamlit as st
import yfinance as yf
import datetime

ticker_symbol = st.text_input("Enter the ticker Symbol","TCS")
start_date = st.date_input("Start Date", datetime.date(2019, 7, 6))
end_date = st.date_input("End Date", datetime.date(2023, 7, 6))

data= yf.download(ticker_symbol,start=start_date,end=end_date)
st.write(data)