import streamlit as st
import datetime
import matplotlib.pyplot as plt
import pickle
import os


def app():
	st.title("ARIMA Model")
	
	st.write("Context will be here")
	
	st.write("Train data 2005-01 -> 2018-08. Min date to forecast 2018-09")
	
	selected_date = st.date_input("Select a date", min_value=datetime.date(2018, 9, 1))
	
	last_date = datetime.date(2018, 8, 1)

	subtract, add = 0, 0
	if selected_date.month < 8:
   		subtract = 8 - selected_date.month
	elif selected_date.month == 8:
		subtract  = 0
	else:
		add = selected_date.month - 8
	steps = (selected_date.year - last_date.year)*12+add-subtract
	
	
	
	
	load_model = pickle.load(open('./apps/arima_model.pkl', 'rb'))
	
	predictions = load_model.forecast(steps)[0]
	#st.write(predictions)
	
	fig, ax = plt.subplots()
	ax.plot(predictions)
	#add date to the x-axes
	#add data before the forecast with different color
	#add title
	st.pyplot(fig)
	
