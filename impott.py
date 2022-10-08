import telegram
from telegram.ext import *
from tradingview_ta import TA_Handler, Interval
import os
import time
import config
import pump
from timeframe import dics
from config import client, wait, database_name , admin , sorry
import fearindex
import cmc
import pump2
import grid
import top
import dumps