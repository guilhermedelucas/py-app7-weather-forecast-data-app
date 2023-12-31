import requests
import config

def get_data(place, forecast_days=None):
    try:
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={config.API_KEY}'
        response = requests.request('get', url)
        data = response.json()
        filtered_data = data['list']
        nr_values = 8 * forecast_days
        filtered_data = filtered_data[:nr_values]
        return filtered_data
    except KeyError:
        return None

if __name__ == '__main__':
    get_data('Berlin', 3)