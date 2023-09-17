import requests
import json
import urllib.parse

class ApiController(object):
    def __init__(self, url: str):
        self.url = url if url[-1] != '/' else url[:-1]
        self.endpoints = {
            'levels': '/levels',
            'groups': '/groups',
            'schedules': '/schedules'
        }

    def error_check(self, endpoint, params = ''):
        response = requests.get(self.url + self.endpoints[endpoint] + params).json()
        status = 'success' if 'response' in response else 'error'
        response = response['response'] if status == 'success' else response['error']
        return {'status': status, 'response': response}

    def get_levels(self):
        return api.error_check('levels')

    def get_groups(self, level_id: str | int):
        params = f'?level_id={level_id}'
        return api.error_check('groups', params)

    def get_schedules(self, group: str | int, dateStart: str, dateEnd: str, subgroups: list | None = None):
        params = f'?group={group}&dateStart={dateStart}&dateEnd={dateEnd}'
        if subgroups:
            subgroups = urllib.parse.quote(json.dumps(subgroups))
            params += f'&subgroups={subgroups}'
        return api.error_check('schedules', params)

if __name__ == '__main__':
    from dotenv import dotenv_values
    env = dotenv_values('.env')
    api = ApiController(env['API_URL'])

    levels = api.get_levels()['response']
    print(levels, '\n')

    groups = api.get_groups(levels[2]['id'])['response']
    print(groups[0], '\n')

    schedule = api.get_schedules(2424, '18.09.2023', '19.09.2023')['response']
    print(schedule)
   
    print(api.get_schedules(
        1482,
        '18.09.2023',
        '24.09.2023',
        [
            {
                'subject': 'Ин.язык',
                'group': 'А',
                'subgroup': '1'
            }
        ])
    )