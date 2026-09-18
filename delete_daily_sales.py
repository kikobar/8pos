import requests
import json
from config import *
from delete import *
import sys
import base64
from datetime import datetime, timezone, UTC

def delete_daily_sales():
    from_date = str(input('From date [YYYY-MM-DD]: '))
    from_date = datetime.strptime(from_date, "%Y-%m-%d").replace(tzinfo=UTC)
    to_date = str(input('To date [YYYY-MM-DD]: '))
    to_date = datetime.strptime(to_date, "%Y-%m-%d").replace(tzinfo=UTC)
    query_filter = {
        "transactionDate": {'$gte': from_date, '$lte': to_date}
        }
    print(query_filter)
    delete(query_filter)
     
if __name__ == '__main__':
    delete_daily_sales()
    
