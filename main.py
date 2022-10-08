from impott import *
import talib
import pandas as pd
import math
from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
import time
import sqlite3

##############################################################################################
# Telegram bot
bot = telegram.Bot(token=config.telegram_api)


def bot_users():
    allowed = []
    dbname = f"{database_name}.sqlite3"
    db = sqlite3.connect(dbname)
    dbcursor = db.cursor()
    hey = db.execute('SELECT userid FROM users').fetchall()
    db.commit()
    db.close()
    result_list = [row[0] for row in hey]
    for member in result_list:
        allowed.append(member)
    return allowed


def add_user_to_data(userid, username):
    dbname = f"{database_name}.sqlite3"
    db = sqlite3.connect(dbname)
    dbcursor = db.cursor()
    dbcursor.execute('''CREATE TABLE IF NOT EXISTS users
              (userid TEXT, username TEXT)''')
    print(f"Database '{dbname}' opened successfully")

    data = db.execute(
        f"SELECT userid FROM users WHERE userid = {userid}"
    ).fetchone()
    if data:
        return
    else:
        dbcursor.execute(
            "INSERT INTO users ('userid','username')"
            f"VALUES ('{userid}' , '{username}')"
        )
        db.commit()
        db.close()

    return db


################################
def remove_files():
    for pine in os.listdir("../bot/"):  # Change to your dir
        if pine == "pinescript.txt":
            os.unlink("../bot/pinescript.txt")


##############################################################################################
# Telegram Commands - you can add as many as you want .


def start_command(update, context):
    uid = update.message.chat["id"]
    uname = update.message.chat["username"]
    add_user_to_data(uid, uname)
    update.message.reply_text(
        "Thank you for Using 'ZCrypto Bot'")
    update.message.reply_text(
        "To use the bot type /commands")


def gdhelp_command(update, context):
    uid = update.message.chat["id"]
    if str(uid) not in bot_users():
        update.message.reply_text(sorry + " click on /start", parse_mode="MARKDOWN")
    else:
        update.message.reply_text(
            "Get the Upper limit and Lower limit for your Grid Bot")
        update.message.reply_text(
            "To Use it /gd COIN setup")
        update.message.reply_text(
            "Example : /gd ETCUSDT setup")


def reshelp_command(update, context):
    uid = update.message.chat["id"]
    if str(uid) not in bot_users():
        update.message.reply_text(sorry + " click on /start", parse_mode="MARKDOWN")
    else:
        update.message.reply_text(
            "--get Support and Resistance levels By AI Bot--'")
        update.message.reply_text(
            "To get Support and Resistance levels for any coins type /res Coinname timeframe")
        update.message.reply_text(
            "Example: /res BTCUSDT 4h")
        update.message.reply_text(
            "Example: /res ETHUSDT 1h")
        update.message.reply_text(
            "Example: /res MANAUSDT 1d")
        update.message.reply_text(
            "Happy Trading!.")


def grid_command(update, context):
    uid = update.message.chat["id"]
    if str(uid) not in bot_users():
        update.message.reply_text(sorry + " click on /start", parse_mode="MARKDOWN")
    else:
        update.message.reply_text(wait)

        update.message.reply_text(grid.grids(), parse_mode="MARKDOWN")


def dca_command(update, context):
    uid = update.message.chat["id"]
    if str(uid) not in bot_users():
        update.message.reply_text(sorry + " click on /start", parse_mode="MARKDOWN")
    else:
        update.message.reply_text(wait)

        update.message.reply_text(pump2.get_usdt_coins(), parse_mode="MARKDOWN")


def fear_command(update, context):
    uid = update.message.chat["id"]
    if str(uid) not in bot_users():
        update.message.reply_text(sorry + " click on /start", parse_mode="MARKDOWN")
    else:
        update.message.reply_text(fearindex.fear(), parse_mode="MARKDOWN")


def info_command(update, context):
    uid = update.message.chat["id"]
    if str(uid) not in bot_users():
        update.message.reply_text(sorry + " click on /start", parse_mode="MARKDOWN")
    else:
        update.message.reply_text(cmc.market(), parse_mode="MARKDOWN")


def pump_command(update, context):
    uid = update.message.chat["id"]
    if str(uid) not in bot_users():
        update.message.reply_text(sorry + " click on /start", parse_mode="MARKDOWN")
    else:
        update.message.reply_text(pump.pumping_coins())
        update.message.reply_text("[Join Our Telegram Channel](https://t.me/Zcryptochannel)\n[Join Our Discord "
                                  "Server](https://discord.gg/RWtT7Nx9jh)\n", parse_mode="MARKDOWN")


def dump_command(update, context):
    uid = update.message.chat["id"]
    if str(uid) not in bot_users():
        update.message.reply_text(sorry + " click on /start", parse_mode="MARKDOWN")
    else:
        update.message.reply_text(wait)
        update.message.reply_text(dumps.get_usdt_coins(), parse_mode="MARKDOWN")


def top_command(update, context):
    uid = update.message.chat["id"]
    if str(uid) not in bot_users():
        update.message.reply_text(sorry + " click on /start", parse_mode="MARKDOWN")
    else:
        update.message.reply_text(config.wait)
        update.message.reply_text(top.topcoin(), parse_mode="MARKDOWN")


def liq_command(update, context):
    uid = update.message.chat["id"]
    if str(uid) not in bot_users():
        update.message.reply_text(sorry + " click on /start", parse_mode="MARKDOWN")
    else:
        update.message.reply_text("https://t.me/Binanceliqs", parse_mode="MARKDOWN")


def commands_command(update, context):
    uid = update.message.chat["id"]
    if str(uid) not in bot_users():
        update.message.reply_text(sorry + " click on /start", parse_mode="MARKDOWN")
    else:
        update.message.reply_text("Commands are\n"
                                  "1:/top - *Get Prices of the TOP MC coins*\n"
                                  "2:/info - *Get information about the Crypto Market.*\n"
                                  "3:/fear - *Get Crypto Fear&Greed Index*\n"
                                  "4:/liq - *Get Binance liquidations*\n"
                                  "5:/pump - *Get Top pumping coins*\n"
                                  "6:/gd - *Get Grid Setup configuration --> /gd BTCUSDT setup*\n"
                                  "7:/grid - *Get the Top Pairs for Grid bots*\n"
                                  "8:/dca - *Get TA based Pumping coins*\n"
                                  "9:/dump - *Get TA based dumping coins*\n"
                                  "10:/ta - *Get TA Indicators --> /ta BTCUSDT 4h*\n"
                                  "11:/config - *Get DCA BOT configuration --> /config sand*\n"
                                  "12:/res - *Get sup and res levels --> /res BTCUSDT 4h*", parse_mode="MARKDOWN")


def pinescript_command(update, context):
    textfile = '../bot/pinescript.txt'
    if os.path.exists(textfile):
        update.message.reply_document(open(textfile, 'rb'))
        remove_files()
    else:
        update.message.reply_text('There is no pinescript.txt file')


def help_command(update, context):
    update.message.reply_text("Commands")


def handle_message(update, context):
    text = str(update.message.text).lower()
    r_text = responses(text)
    update.message.reply_text(r_text)


def get_alarm_data():
    pass


##############################################################################################


# receive inputs from users on telegram bot

def responses(input_text):
    user_message = str(input_text).lower()
    chat_id = bot.get_updates()[-1].message.chat_id
    print(chat_id)
    if str(chat_id) not in bot_users():
        bot.send_message(chat_id=chat_id, text=sorry + " click on /start")
    else:
        if user_message.startswith("/send"):
            if str(chat_id) == admin:
                realmsg = user_message.split("|")
                to_be_sent = realmsg[1]
                for person in bot_users():
                    bot.send_message(chat_id=person, text=to_be_sent)
            else:
                return "You not allowed to use this command"
        if user_message == "test":
            return f"Bot is working well Boss - T Zack\nAPI System status:" \
                   f" {client.get_system_status().get('msg').capitalize()}\n" \
                   f"Server time: " \
                   f"{time.time()}"
        ##############################################################################################

        if user_message.startswith("/config"):
            msg11 = user_message.removeprefix("/config ")
            tck11 = msg11.upper()
            sys1 = f"{tck11}USDT"
            time_frame11 = "1d"
            for ws in range(len(dics)):
                if time_frame11 == dics[ws]["time"]:
                    tim11 = dics[ws]["var"]

            def fetch_dca_bot():
                global a

                candles = client.get_klines(symbol=sys1, interval=tim11, limit=25)
                coin_name = sys1.replace("USDT", "")
                candle_df = pd.DataFrame(candles)
                candle_df.columns = [
                    "Open time",
                    "Open",
                    "High",
                    "Low",
                    "Close",
                    "Volume",
                    "Close time",
                    "Quote asset volume",
                    "Number of trades",
                    "Taker buy base asset volume",
                    "Taker buy quote asset volume",
                    "Can be ignored",
                ]
                candle_df.Close = candle_df.Close.astype(float)
                candle_df.High = candle_df.High.astype(float)
                candle_df.Low = candle_df.Low.astype(float)

                """Get price"""
                price = candle_df["Close"].iloc[-1]

                """ Calculate ATR """
                atr_df = talib.ATR(
                    candle_df.High, candle_df.Low, candle_df.Close, timeperiod=10
                )
                atr = atr_df.iloc[-1]
                cal_atr = round(((atr / price) * 100), 2) * 2
                """1h Data """
                # Getting the 1h Candle data to get the ATR FOR the AVG volatility
                candles1h = client.get_klines(symbol=sys1, interval=Interval.INTERVAL_4_HOURS, limit=25)
                candles1h_df = pd.DataFrame(candles1h)
                candles1h_df.columns = [
                    "Open time",
                    "Open",
                    "High",
                    "Low",
                    "Close",
                    "Volume",
                    "Close time",
                    "Quote asset volume",
                    "Number of trades",
                    "Taker buy base asset volume",
                    "Taker buy quote asset volume",
                    "Can be ignored",
                ]
                candles1h_df.Close = candles1h_df.Close.astype(float)
                candles1h_df.High = candles1h_df.High.astype(float)
                candles1h_df.Low = candles1h_df.Low.astype(float)

                """Get price"""
                price1h = candles1h_df["Close"].iloc[-1]

                """ Calculate ATR """
                atr_df1h = talib.ATR(
                    candles1h_df.High, candles1h_df.Low, candles1h_df.Close, timeperiod=10
                )
                atr1h = atr_df1h.iloc[-1]
                cal_atr1h = round(((atr1h / price1h) * 100), 2)

                """15 MINS"""
                # Getting the 15mins Candle data to get the ATR FOR the AVG volatility
                candles15 = client.get_klines(symbol=sys1, interval=Interval.INTERVAL_15_MINUTES, limit=25)
                candles15_df = pd.DataFrame(candles15)
                candles15_df.columns = [
                    "Open time",
                    "Open",
                    "High",
                    "Low",
                    "Close",
                    "Volume",
                    "Close time",
                    "Quote asset volume",
                    "Number of trades",
                    "Taker buy base asset volume",
                    "Taker buy quote asset volume",
                    "Can be ignored",
                ]
                candles15_df.Close = candles15_df.Close.astype(float)
                candles15_df.High = candles15_df.High.astype(float)
                candles15_df.Low = candles15_df.Low.astype(float)

                """Get price"""
                price15 = candles15_df["Close"].iloc[-1]

                """ Calculate ATR """
                atr_df15 = talib.ATR(
                    candles15_df.High, candles15_df.Low, candles15_df.Close, timeperiod=10
                )
                atr15 = atr_df15.iloc[-1]
                cal_atr15 = round(((atr15 / price15) * 100), 2) * 2
                """# Of SO"""
                max_safety_orders = math.ceil(cal_atr / cal_atr15)

                # ==  DCA Calculator ===
                """DCA Calculator"""
                coin = sys1
                static_price = None  # static price instead
                leverage = 1
                safety_order_step_scale = (cal_atr15 / cal_atr) * max_safety_orders
                safety_order_volume_scale = round(cal_atr15 + (cal_atr15 * 10 / 100), 2)
                # max_safety_orders = 6
                pds = round(cal_atr1h / cal_atr15, 2)
                price_deviation = cal_atr1h / cal_atr15
                # print(price_deviation)
                additionnal_dump = 0

                sum_price_deviation = 0

                if static_price is not None:
                    base_price = static_price
                else:
                    base_price = price
                avg_price = base_price
                onlpercent = 0

                for i in range(max_safety_orders):
                    sum_price_deviation = price_deviation + sum_price_deviation
                    price = (base_price / 100) * (100 - sum_price_deviation)
                    if sum_price_deviation>=cal_atr:
                        a = i
                        break

                    if i != 9:
                        price_deviation = price_deviation * safety_order_step_scale
                MSG = f"*Coin name*: {sys1}\n" \
                      f"*Price Deviation*: {pds}\n" \
                      f"*MAX Number of SOs* : {max_safety_orders}\n" \
                      f"*Actual Number of SOs* : {a}\n" \
                      f"*Safety Step Scale* : {round(safety_order_step_scale, 2)}\n" \
                      f"--- *BETA* ---\n" \
                      f"*Safety volume scale* : {safety_order_volume_scale}\n\n" \
                      f"Safety Volume Scale could be Decreased/increased depends on your capital\n\n" \
                      f"[Join Our Telegram Channel](https://t.me/Zcryptochannel)\n" \
                      f"[Join Our Discord Server](https://discord.gg/RWtT7Nx9jh)\n"
                return MSG

            return bot.send_message(chat_id=chat_id, text=fetch_dca_bot(), parse_mode="MARKDOWN")

        msg = user_message.split(" ")

        tck = msg[1]
        tfr = msg[2]
        if user_message.startswith("/gd"):
            sys = tck.upper()
            time_frame = Interval.INTERVAL_4_HOURS

            def gridsetup():
                df = TA_Handler(
                    symbol=sys,
                    screener="crypto",
                    exchange="BINANCE",
                    interval=Interval.INTERVAL_15_MINUTES,
                )
                df1 = TA_Handler(
                    symbol=sys,
                    screener="crypto",
                    exchange="BINANCE",
                    interval=Interval.INTERVAL_1_HOUR,
                )
                last_cande = client.get_klines(symbol=sys, interval=Interval.INTERVAL_1_HOUR)
                current_price = float(last_cande[-1][4])
                df1.add_indicators(["ATR"])
                atr = float(df1.get_indicators()["ATR"])
                # getting the analysis data from tradingview + returning it
                support = df.get_indicators()["Pivot.M.Fibonacci.S1"]
                cal_atr = round(((atr / current_price) * 100), 2)
                res1 = df1.get_indicators()["Pivot.M.Classic.R2"]
                res2 = df1.get_indicators()["Pivot.M.Classic.R3"]

                return f"*There are 2 upper Limits - Use any of them or something in between*.\n" \
                       f"*1st Upper*: {res1} \n*2nd Upper*: {res2}\n" \
                       f"*Lower limit* : {support}\n" \
                       f"*Grid Width* : {cal_atr} %"

            return bot.send_message(chat_id=chat_id, text=gridsetup(), parse_mode="MARKDOWN")
        ##############################################################################################
        # Usage  /res coin timeframe  "" example /res BTCUSDT 4h
        msg = user_message.split(" ")
        tck = msg[1]
        tfr = msg[2]
        if user_message.startswith("/res"):
            sys = tck.upper()
            time_frame = tfr
            for x in range(len(dics)):
                if time_frame == dics[x]["time"]:
                    tim = dics[x]["var"]

            def res_sup_analysis():
                df = TA_Handler(
                    symbol=sys,
                    screener="crypto",
                    exchange="BINANCE",
                    interval=tim,
                )
                # getting the analysis data from tradingview + returning it
                subs = []
                res = []
                subs.append(df.get_indicators()["Pivot.M.Fibonacci.S1"])
                subs.append(df.get_indicators()["Pivot.M.Fibonacci.S2"])
                subs.append(df.get_indicators()["Pivot.M.Fibonacci.S3"])
                res.append(df.get_indicators()["Pivot.M.Fibonacci.R1"])
                res.append(df.get_indicators()["Pivot.M.Fibonacci.R2"])
                res.append(df.get_indicators()["Pivot.M.Fibonacci.R3"])
                subs.append(df.get_indicators()["Pivot.M.Classic.S1"])
                subs.append(df.get_indicators()["Pivot.M.Classic.S2"])
                subs.append(df.get_indicators()["Pivot.M.Classic.S3"])
                res.append(df.get_indicators()["Pivot.M.Classic.R1"])
                res.append(df.get_indicators()["Pivot.M.Classic.R2"])
                res.append(df.get_indicators()["Pivot.M.Classic.R3"])
                ########################################################
                subs.append(df.get_indicators()["Pivot.M.Woodie.S1"])
                subs.append(df.get_indicators()["Pivot.M.Woodie.S2"])
                subs.append(df.get_indicators()["Pivot.M.Woodie.S3"])
                res.append(df.get_indicators()["Pivot.M.Woodie.R1"])
                res.append(df.get_indicators()["Pivot.M.Woodie.R2"])
                res.append(df.get_indicators()["Pivot.M.Woodie.R3"])

                def pinescript_code():
                    temp = []
                    lines_sma = f"//@version=5\nindicator('ZCrypto {sys} {tim}', overlay=true)\n" \
                                "plot(ta.sma(close, 50), title='50 SMA', color=color.new(color.blue, 0), linewidth=2)\n" \
                                "plot(ta.sma(close, 100), title='100 SMA', color=color.new(color.purple, 0), linewidth=2)\n" \
                                "plot(ta.sma(close, 200), title='200 SMA', color=color.new(color.red, 0), linewidth=2)\n"

                    for line_res in res:
                        if line_res != None:
                            lr = f"hline({line_res}, title=\"Lines\", color=color.red, linestyle=hline.style_solid, linewidth=1)"
                            temp.append(lr)

                    for line_sup in subs:
                        if line_sup != None:
                            ls = f"hline({line_sup}, title=\"Lines\", color=color.green, linestyle=hline.style_solid, " \
                                 f"linewidth=1) "
                            temp.append(ls)
                    lines = '\n'.join(map(str, temp))
                    f = open("../bot/pinescript.txt", "w")  # replace it with the path of the pinescript.txt
                    f.write(lines_sma + lines)
                    f.close()

                pinescript_code()
                return f"\nCompleted execution in {time.perf_counter()} seconds\n Now use the /pinescript command to " \
                       f"get " \
                       f"your file . "

            return bot.send_message(chat_id=chat_id, text=res_sup_analysis())
        ############################################################################################
        msg = user_message.split(" ")
        tck = msg[1]
        tfr = msg[2]
        if user_message.startswith("/ta"):
            sys = tck.upper()
            time_frame = tfr
            for x in range(len(dics)):
                if time_frame == dics[x]["time"]:
                    tim = dics[x]["var"]

            def fetch_all_ta():
                df = TA_Handler(
                    symbol=sys,
                    screener="crypto",
                    exchange="BINANCE",
                    interval=tim,
                )

                ta_summry_raw = df.get_analysis().summary["RECOMMENDATION"]
                ta_ma_raw = df.get_analysis().moving_averages["RECOMMENDATION"]
                ta_osc_raw = df.get_analysis().oscillators["RECOMMENDATION"]

                ta_summry = ta_summry_raw.replace("_", " ")
                ta_ma = ta_ma_raw.replace("_", " ")
                ta_osc = ta_osc_raw.replace("_", " ")

                if "BUY" in ta_summry:
                    tv_side = "🟢"
                elif "SELL" in ta_summry:
                    tv_side = "🔴"
                else:
                    tv_side = "⚪"

                if "BUY" in ta_ma:
                    tv_side1 = "🟢"
                elif "SELL" in ta_ma:
                    tv_side1 = "🔴"
                else:
                    tv_side1 = "⚪"

                if "BUY" in ta_osc:
                    tv_side2 = "🟢"
                elif "SELL" in ta_osc:
                    tv_side2 = "🔴"
                else:
                    tv_side2 = "⚪"

                candles = client.get_klines(symbol=sys, interval=tim, limit=250)
                coin_name = sys.replace("USDT", "")
                candle_df = pd.DataFrame(candles)
                candle_df.columns = [
                    "Open time",
                    "Open",
                    "High",
                    "Low",
                    "Close",
                    "Volume",
                    "Close time",
                    "Quote asset volume",
                    "Number of trades",
                    "Taker buy base asset volume",
                    "Taker buy quote asset volume",
                    "Can be ignored",
                ]
                candle_df.Open = candle_df.Open.astype(float)
                candle_df.Close = candle_df.Close.astype(float)
                candle_df.High = candle_df.High.astype(float)
                candle_df.Low = candle_df.Low.astype(float)

                """Get price"""

                price = candle_df["Close"].iloc[-1]

                """Get Rate of Change"""

                rate_of_change = talib.ROC(candle_df.Close, timeperiod=10)
                roc = round(float(rate_of_change.iloc[-1]), 2)

                """Get Volume"""

                volume = round(float(candle_df["Volume"].iloc[-1]), 2)

                """ Calculate ATR """

                atr_df = talib.ATR(
                    candle_df.High, candle_df.Low, candle_df.Close, timeperiod=14
                )
                atr = atr_df.iloc[-1]
                cal_atr = round(((atr / price) * 100), 2)

                """ Calculate RSI """

                candle_df["RSI"] = (talib.RSI(candle_df.Close))
                rsi = round(float(candle_df["RSI"].iloc[-1]), 2)
                if rsi>=55:
                    side = "🟢"
                    side1 = "Bullish"
                elif rsi>=71:
                    side = "🟡"
                    side1 = "Overbought"
                else:
                    side = "🔴"
                    side1 = "Bearish"

                """ Calculate MFI """

                candle_df["MFI"] = (talib.MFI(candle_df.High, candle_df.Low, candle_df.Close, candle_df.Volume))
                mfi = round(float(candle_df["MFI"].iloc[-1]), 2)
                if mfi>=51:
                    mfi_side = "🟢"
                    mfi_side1 = "Bullish"
                elif mfi>=71:
                    mfi_side = "🟡"
                    mfi_side1 = "Overbought"
                else:
                    mfi_side = "🔴"
                    mfi_side1 = "Bearish"

                """ Calculate MACD """

                macd, macdsignal, macdhist = talib.MACD(candle_df.Close, fastperiod=12, slowperiod=26,
                                                        signalperiod=9)
                macd = float(macd.iloc[-1])
                macdsignal = float(macdsignal.iloc[-1])
                # print(macd)
                # print(macdsignal)
                if macd>macdsignal:
                    macd_icon = "🟢"
                    macd_signal = "Bullish Crossover"
                else:
                    macd_icon = "🔴"
                    macd_signal = "Bearish Crossover"

                """ Calculate Stochastic """

                slowk, slowd = talib.STOCH(candle_df.High, candle_df.Low, candle_df.Close, fastk_period=8,
                                           slowk_period=5,
                                           slowk_matype=0, slowd_period=5,
                                           slowd_matype=0)
                slowk = float(slowk.iloc[-1])
                slowd = float(slowd.iloc[-1])
                if slowk>slowd:
                    stoch_icon = "🟢"
                    stoch_signal = "Bullish Crossover"
                else:
                    stoch_icon = "🔴"
                    stoch_signal = "Bearish Crossover"

                """ Calculate CCI """

                cci_raw = talib.CCI(candle_df.High, candle_df.Low, candle_df.Close, timeperiod=14)
                cci = round(float(cci_raw.iloc[-1]), 2)
                if cci>100:
                    cci_icon = "⚠"
                    cci_side = "Overbought"
                elif cci<-100:
                    cci_icon = "⚠"
                    cci_side = "Oversold"
                else:
                    cci_icon = "⚪️"
                    cci_side = " Normal"

                """ Calculate BB """
                upperband, middleband, lowerband = talib.BBANDS(candle_df.Close, timeperiod=20, nbdevup=2,
                                                                nbdevdn=2,
                                                                matype=0)
                upperband = float(upperband.iloc[-1])
                middleband = float(middleband.iloc[-1])
                lowerband = float(lowerband.iloc[-1])
                # calculating the price difference between mid and upper band
                calculate_high = (upperband - middleband) / 2
                calculate_low = (middleband - lowerband) / 2
                upper = middleband + calculate_high
                lower = middleband - calculate_low
                if price>upper:
                    bb_icon = "⚠"
                    bb_sign = "Near Upper Band"
                elif price<lower:
                    bb_icon = "⚠"
                    bb_sign = "Near lower Band"
                else:
                    bb_icon = "⚪"
                    bb_sign = "Normal Range"

                """ Calculate 10 SMA """

                sma10 = talib.SMA(candle_df.Close, timeperiod=10)
                ten_sma = float(sma10.iloc[-1])

                """ Calculate 20 SMA """

                sma20 = talib.SMA(candle_df.Close, timeperiod=20)
                twenty_sma = float(sma20.iloc[-1])

                """ Calculate 50 SMA """

                sma50 = talib.SMA(candle_df.Close, timeperiod=50)
                fifty_sma = float(sma50.iloc[-1])

                """ Calculate 100 SMA """

                sma100 = talib.SMA(candle_df.Close, timeperiod=100)
                hund_sma = float(sma100.iloc[-1])

                if price>ten_sma:
                    ten_icon = "🟢"
                    ten_sign = "Bullish"
                else:
                    ten_icon = "🔴"
                    ten_sign = "Bearish"

                if price>twenty_sma:
                    twenty_icon = "🟢"
                    twenty_sign = "Bullish"
                else:
                    twenty_icon = "🔴"
                    twenty_sign = "Bearish"

                if price>fifty_sma:
                    fifty_icon = "🟢"
                    fifty_sign = "Bullish"
                else:
                    fifty_icon = "🔴"
                    fifty_sign = "Bearish"

                if price>hund_sma:
                    hund_icon = "🟢"
                    hund_sign = "Bullish"
                else:
                    hund_icon = "🔴"
                    hund_sign = "Bearish"

                """ Calculate PSAR"""

                psar_raw = talib.SAR(candle_df.High, candle_df.Low, acceleration=0.02, maximum=0.2)
                psar = float(psar_raw.iloc[-1])
                if price>psar:
                    psar_icon = "🟢"
                    psar_sign = "Bullish"
                else:
                    psar_icon = "🔴"
                    psar_sign = "Bearish"

                """ Calculate ADX"""
                adx_raw = talib.ADX(candle_df.High, candle_df.Low, candle_df.Close, timeperiod=14)
                adx = float(adx_raw.iloc[-1])
                if price>twenty_sma:
                    if adx<25:
                        adx_icon = "🔴"
                        adx_sign = "Absent or Weak Bullish Trend"
                    elif 25<adx<50:
                        adx_icon = "🟢"
                        adx_sign = "Strong Bullish Trend"

                    elif 50<adx<75:
                        adx_icon = "🟢"
                        adx_sign = "Very Strong Bullish Trend"
                    elif adx>75:
                        adx_icon = "🟢"
                        adx_sign = "Extremely Strong Bullish Trend"
                    else:
                        adx_icon = "⚪"
                        adx_sign = "Normal"
                else:
                    if adx<25:
                        adx_icon = "🔴"
                        adx_sign = "Absent or Weak Bearish Trend"
                    elif 25<adx<50:
                        adx_icon = "🔴"
                        adx_sign = "Strong Bearish Trend"

                    elif 50<adx<75:
                        adx_icon = "🔴"
                        adx_sign = "Very Strong Bearish Trend"
                    elif adx>75:
                        adx_icon = "🔴"
                        adx_sign = "Extremely Strong Bearish Trend"
                    else:
                        adx_icon = "⚪"
                        adx_sign = "Normal"

                """ Calculate MOM"""

                mom_raw = talib.MOM(candle_df.Close, timeperiod=10)
                mom = float(mom_raw.iloc[-1])
                if mom>0:
                    mom_icon = "🟢"
                    mom_sign = "Bullish"
                else:
                    mom_icon = "🔴"
                    mom_sign = "Bearish"

                """ Calculate CMO"""
                cmo_raw = talib.CMO(candle_df.Close, timeperiod=9)
                cmo = float(cmo_raw.iloc[-1])
                if cmo>0:
                    cmo_icon = "🟢"
                    cmo_sign = "Bullish"
                else:
                    cmo_icon = "🔴"
                    cmo_sign = "Bearish"

                msg = f"#{sys} on *Binance* [{time_frame}] \n" \
                      f"💰 *Price*: {price} \n💲 Rate of Change : {roc} %\n" \
                      f"📊 *Volume* : {volume} {coin_name}\n" \
                      f"\n" \
                      f"➡️ *TradingView Recommendation* ⬅️ \n" \
                      f"{tv_side} *TV Summry* :{ta_summry}\n" \
                      f"{tv_side1} *TV MA* :{ta_ma}\n" \
                      f"{tv_side2} *TV OSC* :{ta_osc}\n" \
                      f"\n" \
                      f"🔥 *Average Volatility*: {cal_atr} %\n" \
                      f"{side} *RSI* : {rsi}  {side1}\n" \
                      f"{mfi_side} *MFI* : {mfi} {mfi_side1}\n" \
                      f"{cci_icon}️*CCI* : {cci} {cci_side}\n" \
                      f"{ten_icon} *SMA(10)* : {ten_sign}\n" \
                      f"{twenty_icon} *SMA(20)* : {twenty_sign}\n" \
                      f"{fifty_icon} *SMA(50)* : {fifty_sign}\n" \
                      f"{hund_icon} *SMA(100)* : {hund_sign}\n" \
                      f"{psar_icon} *P-SAR* : {psar_sign}\n" \
                      f"{mom_icon} *MOM* : {mom_sign}\n" \
                      f"{cmo_icon} *CMO* : {cmo_sign}\n" \
                      f"{bb_icon} *BBands* :{bb_sign}\n" \
                      f"{macd_icon} *MACD* :{macd_signal}\n" \
                      f"{stoch_icon} *STOCH* :{stoch_signal}\n" \
                      f"{adx_icon} *ADX* :{adx_sign}\n" \
                      f"[Join Our Telegram Channel](https://t.me/Zcryptochannel)\n" \
                      f"[Join Our Discord Server](https://discord.gg/RWtT7Nx9jh)\n"
                return msg

            return bot.send_message(chat_id=chat_id, text=fetch_all_ta(), parse_mode="MARKDOWN")


############################################################################################


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(config.telegram_api, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("Start", start_command, run_async=True))
    dp.add_handler(CommandHandler("Help", help_command, run_async=True))
    dp.add_handler(CommandHandler("gdhelp", gdhelp_command, run_async=True))
    dp.add_handler(CommandHandler("liq", liq_command, run_async=True))
    dp.add_handler(CommandHandler("grid", grid_command, run_async=True))
    dp.add_handler(CommandHandler("pinescript", pinescript_command, run_async=True))
    dp.add_handler(CommandHandler("dca", dca_command, run_async=True))
    dp.add_handler(CommandHandler("pump", pump_command, run_async=True))
    dp.add_handler(CommandHandler("dump", dump_command, run_async=True))
    dp.add_handler(CommandHandler("top", top_command, run_async=True))
    dp.add_handler(CommandHandler("fear", fear_command, run_async=True))
    dp.add_handler(CommandHandler("info", info_command, run_async=True))
    dp.add_handler(CommandHandler("commands", commands_command, run_async=True))
    dp.add_handler(CommandHandler("reshelp", reshelp_command, run_async=True))
    dp.add_handler(MessageHandler(Filters.text, handle_message, run_async=True))
    dp.add_handler(MessageHandler(Filters.text, handle_message, run_async=True))
    dp.add_error_handler(error)
    updater.start_polling(1, timeout=10)


if __name__ == "__main__":
    print("Telegram Bot started.")
    main()
