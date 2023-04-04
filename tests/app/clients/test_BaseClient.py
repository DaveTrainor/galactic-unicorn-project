import builtins
import tests.mocks.urequests


def test_making_a_request(mocker):
    mock = tests.mocks.urequests.get_requests_mock(mocker, {'test': 1})
    import app.clients.BaseClient

    client = app.clients.BaseClient.BaseClient()
    client.base_url = 'base_url'
    response = client.do_request('?query')

    assert {'test': 1} == response
    mock.assert_any_call('base_url?query')

    mocker.stop(mock)
