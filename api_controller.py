import requests

class Api (object):
    def __init__(self):
        self.url = 'https://rasp-back.utme.space'
        self.groups = '/groups'

    def get_groups(self, level_id):
        return requests.get(self.url + self.groups + f'?level_id={level_id}').json()


if __name__ == '__main__':
    api = Api()
    print(api.get_groups(1))
