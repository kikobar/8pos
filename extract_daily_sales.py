import requests
import json
from config import *
from push import *
import sys
import base64
from datetime import datetime, timezone, UTC, date, timedelta
from zoneinfo import ZoneInfo
from bson.decimal128 import Decimal128

def extract_daily_sales(from_date=None,to_date=None):
    if not(from_date and to_date):
        from_date = str(input('From date [YYYY-MM-DD]: '))
        to_date = str(input('To date [YYYY-MM-DD]: '))
    from_date = datetime.strptime(from_date, "%Y-%m-%d").replace(tzinfo=ZoneInfo(IANATimeZone))
    to_date = datetime.strptime(to_date, "%Y-%m-%d").replace(tzinfo=ZoneInfo(IANATimeZone))
    delta = timedelta(days=1)
    current_date = from_date
    while current_date <= to_date:
        url = base_url + "/sales/daily?startDate="+str(int(current_date.timestamp()*1000))+"&endDate="+str(int(current_date.timestamp()*1000))+"&outletId="+outletId
        payload = {}
        headers = {
            'Authorization': 'Bearer '+bear_token
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        daily_sales = json.loads(response.text)['dailyReport']
        if daily_sales:
            transactionDate = current_date.replace(tzinfo=UTC)
            daily_sales = daily_sales[0]
            daily_sales["curatedSales"] = Decimal128(str(daily_sales["trueNetSales"]+daily_sales["serviceCharges"]))
            daily_sales["transactionDate"] = transactionDate
            print(daily_sales)
            push(daily_sales)
        current_date += delta
        
if __name__ == '__main__':
    if len(sys.argv) != 3:
        extract_daily_sales()
    else:
        extract_daily_sales(str(sys.argv[1]),str(sys.argv[2]))  
