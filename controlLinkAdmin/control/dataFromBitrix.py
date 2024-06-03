from bitrix24 import *
import requests
from datetime import date



class DataBitrix:
    bx24 = Bitrix24('https://novoedelo.bitrix24.ru/rest/24/d1f80xwpra20vfei/')

    def __init__(self, id):
        self.id = id

    def getData(self):
        data = self.bx24.callMethod('crm.lead.list',
                filter={'UTM_MEDIUM': self.id},
                select=['ID'])
        return data

class DataMetrika:
    """62866"""
    def __init__(self, id):
        self.id = id
        self.dateNow = date.today()

    def getData(self):
        headers = {'Authorization': 'OAuth y0_AgAAAAA8bbPQAAvlPAAAAAEGhxsTAABqCPHZ9iFLEK7C5lgG6lKM_u72Qw',
                   'Content-Length': '123', 'Content-Type': 'application/x-yametrika+json'}
        r = requests.get('https://api-metrika.yandex.net/stat/v1/data',
                         params={'id': '84078475', 'metrics': 'ym:s:visits', 'filters': f"ym:pv:UTMMedium=='{self.id}'",
                                 'date1': '2023-09-01', 'date2': f'{self.dateNow}'
                                 }, headers=headers)
        return r.json()
