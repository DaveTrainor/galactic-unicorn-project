import builtins

import tests.mocks.urequests
from app.settings import LocaleSettings

def test_getting_the_time(mocker):
    print_mock = mocker.spy(builtins, 'print')

    mock = tests.mocks.urequests.get_requests_mock(mocker, {
        'datetime': '2023-04-04T12:03:26.543254+01:00'
    })
    import app.clients.TimeClient
    client = app.clients.TimeClient.TimeClient()

    locale = LocaleSettings()
    locale.timezone = 'Europe/London'

    current_time = client.get_time(locale)

    mock.assert_any_call('https://worldtimeapi.org/api/timezone/Europe/London')
    assert '12:03' == current_time
    print_mock.assert_any_call('[client.time] getting time for timezone Europe/London')
    mocker.stop(print_mock)
    mocker.stop(mock)
