import sqlalchemy
from sqlalchemy.sql import select, update, text
import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class DB_connector:
	def __init__(self):
		self.engine = self.establish_connection()
		self.conn = self.engine.connect()

	def establish_connection(self):
		try:
			return sqlalchemy.create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/stock_db')
		except Exception as e: 
			print(e)

	def reflect_table(self, table_name): 
		metadata = sqlalchemy.MetaData(bind=self.engine)

		return sqlalchemy.Table(table_name, metadata , autoload=True)

	def select_table(self, table_name):
		table = self.reflect_table(table_name)

		s = select([table])
		results = self.conn.execute(s)

		return results.first()
