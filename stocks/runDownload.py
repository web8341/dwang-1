from download import constructYFURL
from download import download
from setup import *

nasdaq=pd.read_csv('NASDAQ_companylist.csv',sep=',')
print(nasdaq['Symbol'][:5])
nas_lists=nasdaq['Symbol']

start_date="2014-01-01"
end_date="2017-02-17"
freq="d"

for ticker in nas_lists:
    yfURL=constructYFURL(ticker,start_date,end_date,freq)
    print (yfURL)

    loacalFilePath="D:\\hotma\\AlgorTrading\\algo\\files\\"+ticker+".csv"
    download(loacalFilePath,yfURL)
    time.sleep(0.2)
print('Done')
