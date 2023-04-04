import sys


def get_requests_mock(mocker):
    module = type(sys)('urequests')

    class Response:
        def json(self):
            return {'test': 'response'}

    def get_request(url):
        return Response()

    module.get = get_request
    sys.modules['urequests'] = module

    import urequests as requests

    return mocker.spy(requests, 'get')
