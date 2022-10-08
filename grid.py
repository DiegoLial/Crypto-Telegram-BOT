from config import api_key, api_secret, client
from binance.client import Client
import talib
import pandas as pd


def grids():
    symbols = []
    grid_pairs = []
    tickers = client.get_all_tickers()
    for x in tickers:
        coin = x["symbol"]
        if ("UP" in coin) or ("DOWN" in coin) or ("BULL" in coin) or ("BEAR" in coin):
            continue
        if coin.endswith("USDT"):
            symbols.append(coin)

    """Get the recommendation of Tradingview analysis based on Moving averages and oscillators  """
    for symbol in symbols:
        pair = symbol
        candles = client.get_klines(symbol=pair, interval=Client.KLINE_INTERVAL_1WEEK)
        oneweek_df = pd.DataFrame(candles)
        oneweek_df.columns = ['Open time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close time', 'Quote asset volume',
                              'Number of trades', 'Taker buy base asset volume', 'Taker buy quote asset volume',
                              'Can be ignored']
        oneweek_df.Close = oneweek_df.Close.astype(float)
        oneweek_df.High = oneweek_df.High.astype(float)
        oneweek_df.Low = oneweek_df.Low.astype(float)

        # Get Last/Current price
        current_price = oneweek_df['Close'].iloc[-1]

        # Calculate ATR
        atr_df = talib.ATR(oneweek_df.High, oneweek_df.Low, oneweek_df.Close, timeperiod=14)
        atr = atr_df.iloc[-1]
        cal_atr = round(((atr / current_price) * 100), 2)
        if 70<cal_atr<100:
            grid_pairs.append(f"#{pair} with an MV of {cal_atr}%")
    if len(grid_pairs)<=25:
        grid_coins = '\n'.join(map(str, grid_pairs))
        return f"Top Pairs for Grid Bots \n {grid_coins}\n" \
               f"[Join Our Telegram Channel](https://t.me/Zcryptochannel)\n" \
               f"[Join Our Discord Server](https://discord.gg/RWtT7Nx9jh)\n"

    elif len(grid_pairs)>=27:
        new = grid_pairs[0:25]
        grid_coins = '\n'.join(map(str, new))
        return f"Top Pairs for Grid Bots \n {grid_coins}" \
               f"[Join Our Telegram Channel](https://t.me/Zcryptochannel)\n" \
               f"[Join Our Discord Server](https://discord.gg/RWtT7Nx9jh)\n"
