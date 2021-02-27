import streamlit as st
from multiapp import MultiApp
from apps import home, arima, lstm

app = MultiApp()


app.add_app("Home", home.app)
app.add_app("ARIMA", arima.app)
app.add_app("LSTM", lstm.app)
app.run()
