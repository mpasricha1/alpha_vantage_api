create table stock_ticker(
	id serial PRIMARY KEY, 
	ticker VARCHAR(10), 
	stock_name VARCHAR(100), 
	country VARCHAR(100),
	ipo_year INT, 
	sector VARCHAR(100), 
	industry VARCHAR(100), 
	exchange VARCHAR(10)
); 