import tests.mocks.urequests


def test_making_a_request(mocker):
    mock = tests.mocks.urequests.get_requests_mock(mocker)
    from app.clients.BaseClient import BaseClient

    client = BaseClient()
    client.base_url = 'base_url'
    client.do_request('?query')

    mock.assert_any_call('base_url?query')
