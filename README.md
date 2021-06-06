# Set50-Index-Sqlite
Thai Set50 index stock price today.

# Introduction & Goals
- get thai set50 index stock price data.
- then insert to sqlite database.

# Setup and start
Run the below commands in the project directory.

```bash
pip install -r requirements.txt
```

Start the services.
```bash
python app.py
```
```bash
set50 today: [{'date_': '2021-06-04', 'high': 980.5900268554688, 'low': 972.1900024414062, 'open': 974.25, 'close': 972.3200073242188, 'volume': 0.0, 'adj_close': 972.3200073242188}] # sample data
```
Check data in sqlite
```bash
sqlite3 # active sqlite cli
```
```bash
sqlite> .open stock_price_db.sqlite # access to sqlite db
```
```bash
sqlite> select * from set50_index; # select data at the table
```
```bash
2021-06-04|980.590026855469|972.190002441406|974.25|972.320007324219|0|972.320007324219 # sample data
```

# Stop
From sqlite3 cli terminal
```bash
sqlite> .exit
```

# Follow Me On

- [LinkedIn](https://www.linkedin.com/in/phich-buranchai-9660141b7/)

# Appendix

- [pandas datareader](https://pydata.github.io/pandas-datareader/)
- [yahoo finance](https://finance.yahoo.com/)