import requests

API_KEY = '52dc41fbcbb24227424dba1d55df9bd1'
def get_data(place, forecast_days=None, type=None):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    if type == 'Temperature':
        filtered_data = [i['main']['temp'] / 10 for i in filtered_data]
    else:
        filtered_data = [i['weather']['main'] for i in filtered_data]

    print(filtered_data)
    return filtered_data

if __name__ == '__main__':
    get_data('Berlin', 3, 'Temperature')