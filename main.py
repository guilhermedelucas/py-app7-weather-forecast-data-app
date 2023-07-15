import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast days:', min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox('Select data to view:',
                      ('Temperature', 'Sky'))

if place:
    st.subheader(f'{option} for the next {days} in {place}')
    data = get_data(place=place, forecast_days=days)

    if option == 'Temperature':
        # Create a temperature plot
        temperatures = [i['main']['temp'] / 10 for i in data]
        dates = [i['dt_txt'] for i in data]
        # Create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
        st.plotly_chart(figure)

    if option == 'Sky':
        sky_conditions = [i['weather'][0]['main'] for i in data]

        images = {
            'Clear': 'images/clear.png',
            'Clouds': 'images/cloud.png',
            'Rain': 'images/rain.png',
            'Snow': 'images/snow.png',
        }

        image_paths = [images[conditions] for conditions in sky_conditions]
        dates = [i['dt_txt'] for i in data]
        print(dates)
        # Render sky images
        st.image(image_paths, caption=dates, width=115)