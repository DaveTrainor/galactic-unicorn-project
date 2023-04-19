import builtins

import tests.mocks.urequests


def test_getting_the_current_temperature_hot(mocker):
    print_mock = mocker.spy(builtins, 'print')
    mock = tests.mocks.urequests.get_requests_mock(mocker, {
        'current_weather': {
            'temperature': 32.1
        },
    })
    import app.clients.WeatherForecastClient

    client = app.clients.WeatherForecastClient.WeatherForecastClient()
    current_temperature, temperature_colour = client.get_temperature()

    mock.assert_any_call('https://api.open-meteo.com/v1/forecast?current_weather=true&latitude=0&longitude=0')
    assert '32.1°C' == current_temperature
    assert (255, 10, 10) == temperature_colour
    print_mock.assert_any_call('[client.weather] getting temperature for (0, 0)')
    mocker.stop(print_mock)
    mocker.stop(mock)


def test_getting_the_current_temperature(mocker):
    print_mock = mocker.spy(builtins, 'print')
    mock = tests.mocks.urequests.get_requests_mock(mocker, {
        'current_weather': {
            'temperature': 16.3
        },
    })
    import app.clients.WeatherForecastClient

    client = app.clients.WeatherForecastClient.WeatherForecastClient()
    current_temperature, temperature_colour = client.get_temperature()

    mock.assert_any_call('https://api.open-meteo.com/v1/forecast?current_weather=true&latitude=0&longitude=0')
    assert '16.3°C' == current_temperature
    assert (10, 255, 10) == temperature_colour
    print_mock.assert_any_call('[client.weather] getting temperature for (0, 0)')
    mocker.stop(print_mock)
    mocker.stop(mock)


def test_getting_the_current_temperature_cold(mocker):
    print_mock = mocker.spy(builtins, 'print')
    mock = tests.mocks.urequests.get_requests_mock(mocker, {
        'current_weather': {
            'temperature': 2.7
        },
    })
    import app.clients.WeatherForecastClient

    client = app.clients.WeatherForecastClient.WeatherForecastClient()
    current_temperature, temperature_colour = client.get_temperature()

    mock.assert_any_call('https://api.open-meteo.com/v1/forecast?current_weather=true&latitude=0&longitude=0')
    assert '2.7°C' == current_temperature
    assert (10, 10, 255) == temperature_colour
    print_mock.assert_any_call('[client.weather] getting temperature for (0, 0)')
    mocker.stop(print_mock)
    mocker.stop(mock)
