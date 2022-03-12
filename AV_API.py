import configparser 
import requests

config = configparser.ConfigParser()
config.read('config.ini')

class AV_API:
	def __init__(self, function, symbol, output_size, interval):
		self.function = function
		self.symbol = symbol
		self.output_size = output_size
		self.interval = interval
		self.api_key = config['API_Key']['api_key']
		self.base_url = config['URLs']['av_base_url']

	def call_api(self):
		try:
			response = requests.get(f'{self.base_url}&apikey={self.api_key}&function={self.function}&symbol={self.symbol}&outputsize={self.output_size}&interval={self.interval}')
			if response.status_code == 200:
				data = response.json()
				
				return data[f'Time Series ({self.interval})']			
			else:
				raise Exception ("Failed to call API due to error {response.status_code}")
		except Exception as e:
			print(e)

		


