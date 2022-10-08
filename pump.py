from lunarcrush import LunarCrush

lc = LunarCrush()


def pumping_coins():
    result = lc.get_market(limit=20, sort="acr")
    if "data" in result:
        listcoin = []
        pricelist = []
        for i, crush in enumerate(result["data"], start=1):
            noname = f"#{crush['s']}_USDT"
            price = f"{crush['pc']}"
            listcoin.append(noname)
            pricelist.append(price)
        return f"The top 15 pumping coins now are \n" \
               f"1: {listcoin[0]} *24h price change*  +{pricelist[0]}%\n" \
               f"2: {listcoin[1]} *24h price change*  +{pricelist[1]}%\n" \
               f"3: {listcoin[2]} 24h price change  +{pricelist[2]}%\n" \
               f"4: {listcoin[3]} 24h price change  +{pricelist[3]}%\n" \
               f"5: {listcoin[4]} 24h price change  +{pricelist[4]}%\n" \
               f"6: {listcoin[5]} 24h price change  +{pricelist[5]}%\n" \
               f"7: {listcoin[6]} 24h price change  +{pricelist[6]}%\n" \
               f"8: {listcoin[7]} 24h price change  +{pricelist[7]}%\n" \
               f"9: {listcoin[8]} 24h price change  +{pricelist[8]}%\n" \
               f"10: {listcoin[9]} 24h price change  +{pricelist[9]}%\n" \
               f"11: {listcoin[10]} 24h price change  +{pricelist[10]}%\n" \
               f"12: {listcoin[11]} 24h price change  +{pricelist[11]}%\n" \
               f"13: {listcoin[12]} 24h price change  +{pricelist[12]}%\n" \
               f"14: {listcoin[13]} 24h price change  +{pricelist[13]}%\n" \
               f"15: {listcoin[14]} 24h price change  +{pricelist[14]}%\n"



