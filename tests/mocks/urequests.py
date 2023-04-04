import sys
from importlib import reload


class Response:
    json_response = {}

    def __init__(self, json_response=None):
        self.json_response = {} if json_response is None else json_response

    def json(self):
        return self.json_response


def get_requests_mock(mocker, json_response=None):
    try:
        del sys.modules['urequests']
    except KeyError:
        pass
    try:
        import urequests.urequests as urequests
    except ImportError:
        reload(urequests.urequests)
    sys.modules['urequests'] = urequests

    mock = mocker.patch('urequests.get')
    mock.return_value = Response(json_response)

    return mock
