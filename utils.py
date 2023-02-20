import requests
import json

from config import MyAPI_key, exchange

class ApiException(Exception):
    pass
class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchange[base]
        except KeyError:
            raise ApiException(f"Валюта {base} не найдена!")

        try:
            sym_key = exchange[sym]
        except KeyError:
            raise ApiException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise ApiException(f"Невозможно перевести одинаковые валюты {base}! ")

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise ApiException(f"Не удалось обработать количество {amount}!")

        r = requests.get(f"https://v6.exchangerate-api.com/v6/{MyAPI_key}/pair/{base_key}/{sym_key}/{amount}")
        resp = json.loads(r.content)
        new_price = resp['conversion_result']
        return round(new_price, 4)
