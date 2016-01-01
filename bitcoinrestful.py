#
# bitcoinrestful.py - RESTful app to retrieve current Bitcoin price
#
# Reddit: Daily Programmer - Intermediate - Challenge #228
#


# external modules

import requests


# main logic

# exchange - one of the following {bitfinex, bitstamp, btce, itbit, anxhk, hitbtc, kraken, bitkonan, bitbay, rock, cbx, cotr, vcx}
# currency - one of the following {KRW, NMC, IDR, RON, ARS, AUD, BGN, BRL, BTC, CAD, CHF, CLP, CNY, CZK, DKK, EUR, GAU, GBP, HKD, HUF, ILS, INR, JPY, LTC, MXN, NOK, NZD, PEN, PLN, RUB, SAR, SEK, SGD, SLL, THB, UAH, USD, XRP, ZAR}

def getCurrentPrice(exchange, currency):

    symbol = exchange + currency

    response = requests.get("http://api.bitcoincharts.com/v1/trades.csv?symbol=" + symbol)

    if ("302" in str(response)) or ("404" in str(response)) or (not "," in response.text):

        raise RuntimeError, "Data not found..."

    else:

        latest_csv = response.text.split("\n")[0].strip()

        return float(latest_csv.split(",")[1])
