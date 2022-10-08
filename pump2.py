from binance.client import Client
import talib
import pandas as pd
import re
api_key = "xxx"  # Replace it with your APi key
api_secret = "xxx"  # replace it with your api secret
client = Client(api_key, api_secret)


def get_usdt_coins():
    symbols = []
    hmpairs = []
    tickers = client.get_all_tickers()
    for x in tickers:
        coin = x["symbol"]
        if ("UP" in coin) or ("DOWN" in coin) or ("BULL" in coin) or ("BEAR" in coin) or ("NANO" in coin) or ("BCC" in coin):
            continue
        if coin.endswith("USDT"):
            symbols.append(coin)

    # print(dca_coins)

    for symbol in symbols:
        pair = symbol
        candles = client.get_klines(symbol=pair, interval=Client.KLINE_INTERVAL_1HOUR)
        onehour_df = pd.DataFrame(candles)
        onehour_df.columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume',
                              'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume',
                              'Can be ignored']
        onehour_df.Close = onehour_df.Close.astype(float)
        onehour_df.High = onehour_df.High.astype(float)
        onehour_df.Low = onehour_df.Low.astype(float)

        # Calculate 20 smoothed moving average
        onehour_df['sma'] = talib.SMA(onehour_df.Close, timeperiod=20)
        twenty_sma = onehour_df['sma'].iloc[-1]

        # Get Last/Current price
        current_price = onehour_df['Close'].iloc[-1]

        if current_price > twenty_sma:
            # Calculate ATR
            atr_df = talib.ATR(onehour_df.High, onehour_df.Low, onehour_df.Close, timeperiod=14)
            atr = atr_df.iloc[-1]

            cal_atr = round(((atr / current_price) * 100), 2)
            if cal_atr > 2:
                hmpairs.append(f"#{pair} with an HM of {cal_atr}%")
    if len(hmpairs) <= 30:
        hmcoins = sorted(hmpairs, key=lambda kv: kv[1], reverse=True)
        new = hmcoins[0:30]
        dca_coins = '\n'.join(map(str, new))
        return f"Top Pairs for DCA Bots \n {dca_coins}\n" \
               f"[Join Our Telegram Channel](https://t.me/Zcryptochannel)\n" \
               f"[Join Our Discord Server](https://discord.gg/RWtT7Nx9jh)\n"

    elif len(hmpairs) >= 31:
        hmcoins = sorted(hmpairs, key=lambda kv: kv[1], reverse=True)
        new = hmcoins[0:30]
        dca_coins = '\n'.join(map(str, new))
        return f"Top Pairs for DCA Bots 2 \n {dca_coins}\n" \
               f"[Join Our Telegram Channel](https://t.me/Zcryptochannel)\n" \
               f"[Join Our Discord Server](https://discord.gg/RWtT7Nx9jh)\n"
    else:
        return f"NO DATA"
