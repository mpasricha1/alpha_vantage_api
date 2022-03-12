import requests 
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['API_Key']['api_key']

print(api_key)