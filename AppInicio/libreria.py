import requests
import json
from datetime import datetime
import pandas as pd

def valorUf():
    _dia = datetime.today().date().strftime('%d-%m-%Y')
    url = f'https://mindicador.cl/api/uf/{_dia}'
    response = requests.get(url)
    data = json.loads(response.text.encode("utf-8"))
    for e in data["serie"]:
        _valor_uf = e["valor"]
    return _valor_uf