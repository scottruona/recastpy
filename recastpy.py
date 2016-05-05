import requests


class RequestResponse(object):
    """
    Recast.AI Request Response class

    .json -- JSON response
    """

    def __init__(self, response):
        self.json = response.json()


class Recast(object):
    """
    Recast.AI API class

    token -- Access token provided by Recast.AI
    """

    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization': 'Token ' + self.token}
        self.url = 'https://api.recast.ai/v1'

    def text_request(self, text):
        """
        POST to /request endpoint with text.

        text -- string, max 256 characters
        """

        return RequestResponse(requests.post('{url}/request'.format(url=self.url),
                                             params={'text': text},
                                             headers=self.headers
                                            )
                              )

    def voice_request(self, voice):
        """
        POST to /request endpoint with voice file.

        voice -- .wav file object
                 Not empty, not blank, no empty file,
                 Minimum duration : 200 milliseconds.
                 Maximum duration: 10 seconds.
        """

        return RequestResponse(requests.post('{url}/request'.format(url=self.url),
                                             files={'voice':voice},
                                             headers=self.headers
                                            )
                              )
