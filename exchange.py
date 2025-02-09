#import libraries to work get json files
import os
from dotenv import load_dotenv
import requests
from pprint import pprint

#load env files
load_dotenv()

#we ll get API keys here
def get_currency(from_currency= "RWF"):
    url=requests.get(f'https://v6.exchangerate-api.com/v6/{os.getenv('API_Key')}/latest/{from_currency}')
    exchange_app=url.json()
    return exchange_app
    #pprint(exchange_app)
#test the code via terminal
def main():
    pprint(get_currency)
if __name__=="__main__":
    main()