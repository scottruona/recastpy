import requests


class Recast(object):
    
    def __init__(self, token):
        self.token = token
    
    def req(self, text):
        return requests.post('https://api.recast.ai/request', params={'text': text}, headers={'Authorization': 'Token ' + self.token}).json()
    


