
# import math
# import random
#
# profit = random.randrange(300, 710, 1)
# profit = 789
# print(profit)
# binance = 0.0149
# okey = 0.0155
#
# found = False  # Flag to indicate if we've found the solution
#
# for okx in range(1, 10000):
#     if found:
#         break  # If we found our pair, break out of the outer loop as well
#     for bin in range(1, 10000):
#         if (okey * okx) - (binance * bin) == profit:
#             print("First OKX:", okx, "First BIN:", bin)
#             found = True  # Set the flag to True since we've found our pair
#             break  # Break out of the inner loop
#
# if not found:
#     print("No solution found within the given ranges.")
#

import numpy as np
import random

def check_spreads(context: CallbackContext) -> None:
    chat_id = context.job.context

    for symbol in SYMBOLS.keys():
        prices_dict = {}
        for exchange in EXCHANGE_URLS.keys():
            price = get_price(exchange, symbol)
            if price is not None:  # Убедитесь, что цена успешно получена
                prices_dict[exchange] = price

        if len(prices_dict) >= 2:  # Нужно минимум две цены для расчёта спреда
            min_price_exchange, min_price = min(prices_dict.items(), key=lambda x: x[1])
            max_price_exchange, max_price = max(prices_dict.items(), key=lambda x: x[1])
            spread_value = (max_price - min_price) / min_price

            # Формируем URL для покупки и продажи
            buy_url = EXCHANGE_TRADE_URLS[min_price_exchange].format(symbol)
            sell_url = EXCHANGE_TRADE_URLS[max_price_exchange].format(symbol)

            if spread_value > 0.0002:  # Пороговое значение 0.02%
                message = (f"Купить {symbol} можно на бирже {min_price_exchange.upper()} по цене {min_price} USD\n"
                           f"🔗 [Купить здесь]({buy_url})\n\n"
                           f"Продать {symbol} можно на бирже {max_price_exchange.upper()} по цене {max_price} USD\n"
                           f"🔗 [Продать здесь]({sell_url})\n\n"
                           f"Потенциальная прибыль: {max_price - min_price:.2f} USD или {spread_value * 100:.2f}%.")
                context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
        else:
            context.bot.send_message(chat_id=chat_id, text=f"Недостаточно данных для расчета спреда для {symbol}.")