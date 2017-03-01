ticker = "AAPL"
start_date="2015-01-01"
END_date="2017-02-17"

options={
'qtype':'close',
'tables':['adjPrice','tradingdate']
}

from fetchData import getRawData

ticketDataRaw=getRawData(ticker,start_date,end_date,options)

print(ticketDataRaw.head())
