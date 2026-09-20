import requests
from config import *
import sys
import json

def generate_token():
    url = token_url

    payload = json.dumps({
      "email": credential_email,
      "password": credential_password
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
	
	
if __name__ == '__main__':
    generate_token()
    
