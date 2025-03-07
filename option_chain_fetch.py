from fyers_apiv3 import fyersModel

client_id = "ZHQ4IJL7TI-100"
with open("access_token", "r") as f:
    access_token = f.read()

# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")

data = {
    "symbol": "NSE:NIFTY50-INDEX",
    "strikecount": 1,
    "timestamp": "1727344800"
}

response = fyers.optionchain(data=data)
print("option chain:", response)
#
# option_chain = {'code': 200, 'data':
#     {'callOi': 110002530,
#      'expiryData':
#          [{'date': '12-09-2024', 'expiry': '1726135200'},
#           {'date': '19-09-2024', 'expiry': '1726740000'},
#           {'date': '26-09-2024', 'expiry': '1727344800'},
#           {'date': '03-10-2024', 'expiry': '1727949600'},
#           {'date': '10-10-2024', 'expiry': '1728554400'},
#           {'date': '31-10-2024', 'expiry': '1730368800'},
#           {'date': '28-11-2024', 'expiry': '1732788000'},
#           {'date': '26-12-2024', 'expiry': '1735207200'},
#           {'date': '27-03-2025', 'expiry': '1743069600'},
#           {'date': '26-06-2025', 'expiry': '1750932000'},
#           {'date': '24-12-2025', 'expiry': '1766570400'},
#           {'date': '25-06-2026', 'expiry': '1782381600'},
#           {'date': '31-12-2026', 'expiry': '1798711200'},
#           {'date': '24-06-2027', 'expiry': '1813831200'},
#           {'date': '30-12-2027', 'expiry': '1830160800'},
#           {'date': '29-06-2028', 'expiry': '1845885600'},
#           {'date': '28-12-2028', 'expiry': '1861610400'},
#           {'date': '28-06-2029', 'expiry': '1877335200'}],
#      'indiavixData': {'ask': 0, 'bid': 0, 'description': 'INDIAVIX-INDEX', 'ex_symbol': 'INDIAVIX', 'exchange': 'NSE',
#                       'fyToken': '101000000026017', 'ltp': 15.22, 'ltpch': 1.01, 'ltpchp': 7.11, 'option_type': '',
#                       'strike_price': -1, 'symbol': 'NSE:INDIAVIX-INDEX'},
#      'optionsChain': [
#          {'ask': 0, 'bid': 0, 'description': 'NIFTY50-INDEX', 'ex_symbol': 'NIFTY', 'exchange': 'NSE', 'fp': 24909.4,
#           'fpch': -327.35, 'fpchp': -1.3, 'fyToken': '101000000026000', 'ltp': 24852.15, 'ltpch': -292.95,
#           'ltpchp': -1.17, 'option_type': '', 'strike_price': -1, 'symbol': 'NSE:NIFTY50-INDEX'},
#          {'ask': 193.4, 'bid': 192.1, 'fyToken': '101124091250189', 'ltp': 193.9, 'ltpch': -229.95, 'ltpchp': -54.25,
#           'oi': 1392650, 'oich': 0, 'oichp': 0, 'option_type': 'CE', 'prev_oi': 1392650, 'strike_price': 24800,
#           'symbol': 'NSE:NIFTY2491224800CE', 'volume': 28133075},
#          {'ask': 129, 'bid': 128.35, 'fyToken': '101124091250190', 'ltp': 128.4, 'ltpch': 94.85, 'ltpchp': 282.71,
#           'oi': 2567120, 'oich': 0, 'oichp': 0, 'option_type': 'PE', 'prev_oi': 2567120, 'strike_price': 24800,
#           'symbol': 'NSE:NIFTY2491224800PE', 'volume': 75401825},
#          {'ask': 151.3, 'bid': 150.05, 'fyToken': '101124091250192', 'ltp': 151.3, 'ltpch': 110.7, 'ltpchp': 272.66,
#           'oi': 1671350, 'oich': 0, 'oichp': 0, 'option_type': 'PE', 'prev_oi': 1671350, 'strike_price': 24850,
#           'symbol': 'NSE:NIFTY2491224850PE', 'volume': 47313150},
#          {'ask': 165.45, 'bid': 164.15, 'fyToken': '101124091250191', 'ltp': 164.45, 'ltpch': -216.9, 'ltpchp': -56.88,
#           'oi': 1807700, 'oich': 0, 'oichp': 0, 'option_type': 'CE', 'prev_oi': 1807700, 'strike_price': 24850,
#           'symbol': 'NSE:NIFTY2491224850CE', 'volume': 26126050},
#          {'ask': 175, 'bid': 174.5, 'fyToken': '101124091250194', 'ltp': 175, 'ltpch': 125.85, 'ltpchp': 256.05,
#           'oi': 2098720, 'oich': 0, 'oichp': 0, 'option_type': 'PE', 'prev_oi': 2098720, 'strike_price': 24900,
#           'symbol': 'NSE:NIFTY2491224900PE', 'volume': 92309000},
#          {'ask': 140, 'bid': 137.75, 'fyToken': '101124091250193', 'ltp': 139, 'ltpch': -200.85, 'ltpchp': -59.1,
#           'oi': 3065400, 'oich': 0, 'oichp': 0, 'option_type': 'CE', 'prev_oi': 3065400, 'strike_price': 24900,
#           'symbol': 'NSE:NIFTY2491224900CE', 'volume': 70619850}],
#      'putOi': 66660115},
#                 'message': '', 's': 'ok'}
#
# option_chain = {'code': 200, 'data':
#     {'callOi': 110002530,
#      'expiryData':
#          [{'date': '12-09-2024', 'expiry': '1726135200'}, {'date': '19-09-2024', 'expiry': '1726740000'},
#           {'date': '26-09-2024', 'expiry': '1727344800'}, {'date': '03-10-2024', 'expiry': '1727949600'},
#           {'date': '10-10-2024', 'expiry': '1728554400'}, {'date': '31-10-2024', 'expiry': '1730368800'},
#           {'date': '28-11-2024', 'expiry': '1732788000'}, {'date': '26-12-2024', 'expiry': '1735207200'},
#           {'date': '27-03-2025', 'expiry': '1743069600'}, {'date': '26-06-2025', 'expiry': '1750932000'},
#           {'date': '24-12-2025', 'expiry': '1766570400'}, {'date': '25-06-2026', 'expiry': '1782381600'},
#           {'date': '31-12-2026', 'expiry': '1798711200'}, {'date': '24-06-2027', 'expiry': '1813831200'},
#           {'date': '30-12-2027', 'expiry': '1830160800'}, {'date': '29-06-2028', 'expiry': '1845885600'},
#           {'date': '28-12-2028', 'expiry': '1861610400'}, {'date': '28-06-2029', 'expiry': '1877335200'}],
#      'indiavixData': {'ask': 0, 'bid': 0, 'description': 'INDIAVIX-INDEX', 'ex_symbol': 'INDIAVIX', 'exchange': 'NSE',
#                       'fyToken': '101000000026017', 'ltp': 15.22, 'ltpch': 1.01, 'ltpchp': 7.11, 'option_type': '',
#                       'strike_price': -1, 'symbol': 'NSE:INDIAVIX-INDEX'},
#      'optionsChain': [
#         {'ask': 0, 'bid': 0, 'description': 'NIFTY50-INDEX', 'ex_symbol': 'NIFTY', 'exchange': 'NSE', 'fp': 24909.4,
#          'fpch': -327.35, 'fpchp': -1.3, 'fyToken': '101000000026000', 'ltp': 24852.15, 'ltpch': -292.95,
#          'ltpchp': -1.17, 'option_type': '', 'strike_price': -1, 'symbol': 'NSE:NIFTY50-INDEX'},
#         {'ask': 93.4, 'bid': 92.45, 'fyToken': '101124091248610', 'ltp': 93, 'ltpch': 70, 'ltpchp': 304.35,
#          'oi': 2102220, 'oich': 0, 'oichp': 0, 'option_type': 'PE', 'prev_oi': 2102220, 'strike_price': 24700,
#          'symbol': 'NSE:NIFTY2491224700PE', 'volume': 51517175},
#         {'ask': 257.65, 'bid': 254.8, 'fyToken': '101124091248609', 'ltp': 257.7, 'ltpch': -255.25, 'ltpchp': -49.76,
#          'oi': 523250, 'oich': 0, 'oichp': 0, 'option_type': 'CE', 'prev_oi': 523250, 'strike_price': 24700,
#          'symbol': 'NSE:NIFTY2491224700CE', 'volume': 6547100},
#         {'ask': 110.35, 'bid': 109.1, 'fyToken': '101124091248614', 'ltp': 109.05, 'ltpch': 81.55, 'ltpchp': 296.55,
#          'oi': 623725, 'oich': 0, 'oichp': 0, 'option_type': 'PE', 'prev_oi': 623725, 'strike_price': 24750,
#          'symbol': 'NSE:NIFTY2491224750PE', 'volume': 28842450},
#         {'ask': 225, 'bid': 222.05, 'fyToken': '101124091248612', 'ltp': 224, 'ltpch': -242.4, 'ltpchp': -51.97,
#          'oi': 170625, 'oich': 0, 'oichp': 0, 'option_type': 'CE', 'prev_oi': 170625, 'strike_price': 24750,
#          'symbol': 'NSE:NIFTY2491224750CE', 'volume': 3685175},
#         {'ask': 193.4, 'bid': 192.1, 'fyToken': '101124091250189', 'ltp': 193.9, 'ltpch': -229.95, 'ltpchp': -54.25,
#          'oi': 1392650, 'oich': 0, 'oichp': 0, 'option_type': 'CE', 'prev_oi': 1392650, 'strike_price': 24800,
#          'symbol': 'NSE:NIFTY2491224800CE', 'volume': 28133075},
#         {'ask': 129, 'bid': 128.35, 'fyToken': '101124091250190', 'ltp': 128.4, 'ltpch': 94.85, 'ltpchp': 282.71,
#          'oi': 2567120, 'oich': 0, 'oichp': 0, 'option_type': 'PE', 'prev_oi': 2567120, 'strike_price': 24800,
#          'symbol': 'NSE:NIFTY2491224800PE', 'volume': 75401825},
#         {'ask': 151.3, 'bid': 150.05, 'fyToken': '101124091250192', 'ltp': 151.3, 'ltpch': 110.7, 'ltpchp': 272.66,
#          'oi': 1671350, 'oich': 0, 'oichp': 0, 'option_type': 'PE', 'prev_oi': 1671350, 'strike_price': 24850,
#          'symbol': 'NSE:NIFTY2491224850PE', 'volume': 47313150},
#         {'ask': 165.45, 'bid': 164.15, 'fyToken': '101124091250191', 'ltp': 164.45, 'ltpch': -216.9, 'ltpchp': -56.88,
#          'oi': 1807700, 'oich': 0, 'oichp': 0, 'option_type': 'CE', 'prev_oi': 1807700, 'strike_price': 24850,
#          'symbol': 'NSE:NIFTY2491224850CE', 'volume': 26126050},
#         {'ask': 175, 'bid': 174.5, 'fyToken': '101124091250194', 'ltp': 175, 'ltpch': 125.85, 'ltpchp': 256.05,
#          'oi': 2098720, 'oich': 0, 'oichp': 0, 'option_type': 'PE', 'prev_oi': 2098720, 'strike_price': 24900,
#          'symbol': 'NSE:NIFTY2491224900PE', 'volume': 92309000},
#         {'ask': 140, 'bid': 137.75, 'fyToken': '101124091250193', 'ltp': 139, 'ltpch': -200.85, 'ltpchp': -59.1,
#          'oi': 3065400, 'oich': 0, 'oichp': 0, 'option_type': 'CE', 'prev_oi': 3065400, 'strike_price': 24900,
#          'symbol': 'NSE:NIFTY2491224900CE', 'volume': 70619850},
#         {'ask': 203.05, 'bid': 200.85, 'fyToken': '101124091250196', 'ltp': 200.75, 'ltpch': 140.7, 'ltpchp': 234.31,
#          'oi': 737375, 'oich': 0, 'oichp': 0, 'option_type': 'PE', 'prev_oi': 737375, 'strike_price': 24950,
#          'symbol': 'NSE:NIFTY2491224950PE', 'volume': 37983700},
#         {'ask': 115.8, 'bid': 115.1, 'fyToken': '101124091250195', 'ltp': 115.1, 'ltpch': -185.6, 'ltpchp': -61.72,
#          'oi': 1260420, 'oich': 0, 'oichp': 0, 'option_type': 'CE', 'prev_oi': 1260420, 'strike_price': 24950,
#          'symbol': 'NSE:NIFTY2491224950CE', 'volume': 32414250},
#         {'ask': 232, 'bid': 231.05, 'fyToken': '101124091250201', 'ltp': 231.95, 'ltpch': 160.2, 'ltpchp': 223.28,
#          'oi': 2877550, 'oich': 0, 'oichp': 0, 'option_type': 'PE', 'prev_oi': 2877550, 'strike_price': 25000,
#          'symbol': 'NSE:NIFTY2491225000PE', 'volume': 83574300},
#         {'ask': 95, 'bid': 94.4, 'fyToken': '101124091250197', 'ltp': 94.4, 'ltpch': -168, 'ltpchp': -64.02,
#          'oi': 6628000, 'oich': 0, 'oichp': 0, 'option_type': 'CE', 'prev_oi': 6628000, 'strike_price': 25000,
#          'symbol': 'NSE:NIFTY2491225000CE', 'volume': 93755925}], 'putOi': 66660115}, 'message': '', 's': 'ok'}


option_chain = {'code': 200, 'data': {'callOi': 99146625, 'expiryData': [{'date': '26-09-2024', 'expiry': '1727344800'}, {'date': '03-10-2024', 'expiry': '1727949600'}, {'date': '10-10-2024', 'expiry': '1728554400'}, {'date': '17-10-2024', 'expiry': '1729159200'}, {'date': '24-10-2024', 'expiry': '1729764000'}, {'date': '31-10-2024', 'expiry': '1730368800'}, {'date': '28-11-2024', 'expiry': '1732788000'}, {'date': '26-12-2024', 'expiry': '1735207200'}, {'date': '27-03-2025', 'expiry': '1743069600'}, {'date': '26-06-2025', 'expiry': '1750932000'}, {'date': '24-12-2025', 'expiry': '1766570400'}, {'date': '25-06-2026', 'expiry': '1782381600'}, {'date': '31-12-2026', 'expiry': '1798711200'}, {'date': '24-06-2027', 'expiry': '1813831200'}, {'date': '30-12-2027', 'expiry': '1830160800'}, {'date': '29-06-2028', 'expiry': '1845885600'}, {'date': '28-12-2028', 'expiry': '1861610400'}, {'date': '28-06-2029', 'expiry': '1877335200'}], 'indiavixData': {'ask': 0, 'bid': 0, 'description': 'INDIAVIX-INDEX', 'ex_symbol': 'INDIAVIX', 'exchange': 'NSE', 'fyToken': '101000000026017', 'ltp': 12.79, 'ltpch': 0.32, 'ltpchp': 2.57, 'option_type': '', 'strike_price': -1, 'symbol': 'NSE:INDIAVIX-INDEX'}, 'optionsChain': [{'ask': 0, 'bid': 0, 'description': 'NIFTY50-INDEX', 'ex_symbol': 'NIFTY', 'exchange': 'NSE', 'fp': 25790.2, 'fpch': 301.1, 'fpchp': 1.18, 'fyToken': '101000000026000', 'ltp': 25790.95, 'ltpch': 375.15, 'ltpchp': 1.48, 'option_type': '', 'strike_price': -1, 'symbol': 'NSE:NIFTY50-INDEX'}, {'ask': 158, 'bid': 154.1, 'fyToken': '101124092656036', 'ltp': 155.1, 'ltpch': 106.5, 'ltpchp': 219.14, 'oi': 963375, 'oich': 268975, 'oichp': 38.73, 'option_type': 'CE', 'prev_oi': 694400, 'strike_price': 25750, 'symbol': 'NSE:NIFTY24SEP25750CE', 'volume': 69551425}, {'ask': 119.35, 'bid': 118.1, 'fyToken': '101124092656037', 'ltp': 119.45, 'ltpch': -188.05, 'ltpchp': -61.15, 'oi': 1297575, 'oich': 1175300, 'oichp': 961.19, 'option_type': 'PE', 'prev_oi': 122275, 'strike_price': 25750, 'symbol': 'NSE:NIFTY24SEP25750PE', 'volume': 29438200}, {'ask': 128, 'bid': 125.4, 'fyToken': '101124092656046', 'ltp': 128, 'ltpch': 91.65, 'ltpchp': 252.13, 'oi': 5347450, 'oich': 32670, 'oichp': 0.61, 'option_type': 'CE', 'prev_oi': 5314780, 'strike_price': 25800, 'symbol': 'NSE:NIFTY24SEP25800CE', 'volume': 136618575}, {'ask': 139.9, 'bid': 137, 'fyToken': '101124092656047', 'ltp': 137, 'ltpch': -208.05, 'ltpchp': -60.3, 'oi': 2836125, 'oich': 2681550, 'oichp': 1734.79, 'option_type': 'PE', 'prev_oi': 154575, 'strike_price': 25800, 'symbol': 'NSE:NIFTY24SEP25800PE', 'volume': 42709750}, {'ask': 101.95, 'bid': 100.65, 'fyToken': '101124092656048', 'ltp': 101.8, 'ltpch': 74.3, 'ltpchp': 270.18, 'oi': 1683150, 'oich': 1056800, 'oichp': 168.72, 'option_type': 'CE', 'prev_oi': 626350, 'strike_price': 25850, 'symbol': 'NSE:NIFTY24SEP25850CE', 'volume': 54511525}, {'ask': 164.7, 'bid': 162.45, 'fyToken': '101124092656049', 'ltp': 163.1, 'ltpch': -218.45, 'ltpchp': -57.25, 'oi': 639850, 'oich': 622825, 'oichp': 3658.3, 'option_type': 'PE', 'prev_oi': 17025, 'strike_price': 25850, 'symbol': 'NSE:NIFTY24SEP25850PE', 'volume': 7727175}], 'putOi': 148629625}, 'message': '', 's': 'ok'}
