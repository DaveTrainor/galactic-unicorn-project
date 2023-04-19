from app.clients.BaseClient import BaseClient


class WeatherForecastClient(BaseClient):
    base_url = 'https://api.open-meteo.com/v1/forecast?current_weather=true'

    def get_temperature(self, coordinates=(0, 0)) -> (str, (int, int, int)):
        latitude, longitude = coordinates
        print(f'[client.weather] getting temperature for {coordinates}')
        query = f'&latitude={latitude}&longitude={longitude}'
        data = self.do_request(query)
        temp = str(data['current_weather']['temperature'])

        colour = (10, 255, 10)
        if float(temp) >= 20:
            colour = (255, 10, 10)
        if float(temp) <= 4:
            colour = (10, 10, 255)

        return f'{temp}°C', colour
