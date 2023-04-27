import builtins
from importlib import reload
import tests.mocks.settings as mock_settings
import tests.mocks.urequests

def test_getting_the_time(mocker):
    import app.settings
    print_mock = mocker.spy(builtins, 'print')
    mock_settings.full_settings()
    reload(app.settings)
    settings = app.settings.Settings()

    mock = tests.mocks.urequests.get_requests_mock(mocker, {
        'datetime': '2023-04-04T12:03:26.543254+01:00'
    })
    import app.clients.TimeClient

    client = app.clients.TimeClient.TimeClient()
    current_time = client.get_time()

    mock.assert_any_call('https://worldtimeapi.org/api/timezone/Europe/London')
    assert '12:03' == current_time
    print_mock.assert_any_call('[client.time] getting time for timezone Europe/London')
    mocker.stop(print_mock)
    mocker.stop(mock)
