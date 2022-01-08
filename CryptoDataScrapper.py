# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 19:21:44 2022

@author: ajjay
"""

import requests
import datetime
import csv

prod_id = "ETH-USD"
timeframe = 3600

end = datetime.datetime(2022,1,6,0,0,0)
start = datetime.datetime(2022,1,4,0,0,0)
end_f = end.strftime('%d-%m-%y')
start_f = start.strftime('%d-%m-%y')
interlude = [["Time", "Low", "High", "Open", "Close", "Volume"]]

while (end > start):
    temp = start + datetime.timedelta(days= 12)
    if temp > end:
        temp = end
    request_url = f"https://api.exchange.coinbase.com/products/{prod_id}/candles?granularity={timeframe}&start={start}&end={temp}"

    request = requests.get(request_url)
    data = request.json()
    
    for row in data:
        interlude.append(row)
        
    start = temp

with open(f"{prod_id} {start_f} to {end_f}.csv","a", encoding='utf-8',newline='') as file:
     writer = csv.writer(file)
     writer.writerows(interlude)

