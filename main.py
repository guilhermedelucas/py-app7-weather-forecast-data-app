import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast days:', min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox('Select data to view:',
                      ('Temperature', 'Sky'))

st.subheader(f'{option} for the next {days} in {place}')


# def get_data(days_local):
#     days_local = ["2022-25-10", "2022-26-10", "2022-27-10"]
#     temperatures_local = [10, 11, 15]
#     temperatures_local = [days * i for i in temperatures_local]
#     return days_local, temperatures_local


d, t = get_data(place=place, forecast_days=days, type=option)


figure = px.line(x=d, y=t, labels={ "x": "Date", "y": "Temperature" })
st.plotly_chart(figure)