from config import client
import time


def topcoin():
    widget_list = ("BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "DOTUSDT", "AVAXUSDT")
    majors = []
    perf = time.perf_counter()
    for w in widget_list:
        values = list(client.get_symbol_ticker(symbol=w).values())
        majors.extend([values[0].removesuffix('USDT'), values[1].rstrip('0')])
    return f"#{majors[0]}: {majors[1]}\n#{majors[2]}: {majors[3]}\n#{majors[4]}: {majors[5]}\n#" \
           f"{majors[6]}: {majors[7]}\n#{majors[8]}: {majors[9]}\n#{majors[10]}: {majors[11]}\nHappy Trading!.\n" \
           f"[Join Our Telegram Channel](https://t.me/Zcryptochannel)\n" \
           f"[Join Our Discord Server](https://discord.gg/RWtT7Nx9jh)\n"

