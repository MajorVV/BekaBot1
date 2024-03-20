import requests


response = requests.get("https://contract.mexc.com/api/v1/contract/fair_price/BTC_USDT")
result = response.json()
print(result)





# EXCHANGE_URLS = {'mexc': "https://contract.mexc.com/api/v1/contract/last_price/{}"}
# SYMBOLS = {'mexc': {'BTC_USD': 'BTC_USDT'}}
#
# def get_price(exchange, symbol):
#     symbol_code = SYMBOLS[exchange][symbol]
#     url = EXCHANGE_URLS[exchange].format(symbol_code)
#     try:
#         response = requests.get(url)
#         data = response.json()
#
#         if exchange == 'mexc':
#             return float(data['data']['index_price'])
#
#     except Exception as e:
#         print(f"Ошибка {exchange}: {e}")
#         return None
#
# price = get_price('mexc', 'BTC_USD')
# if price is not None:
#     print(f"Цена на бирже Mexc: {price}")
