#contruct url and download from Yahoo Finance
#Month index starts from 0

from datetime import datetime
def constructYFURL(ticker,start_date,end_date,freq):
    start_date=datetime.strptime(start_date,"%Y-%m-%d").date()
    end_date=datetime.strptime(end_date,"%Y-%m-%d").date()

    s=ticker.replace("^","%5E")
    if start_date.month-1<=10:
        a="0"+str(start_date.month-1)
    else:
        a=str(start_date.month-1)
    b=str(start_date.day)
    c=str(start_date.year)
    if start_date.month-1<=10:
        d="0"+str(end_date.month-1)
    else:
        d=str(end_date.month-1)
    e=str(end_date.day)
    f=str(end_date.year)
    g=freq
    #d=daily, w=weekly

    yfURL="http://chart.finance.yahoo.com/table.csv?s="+s+"&a="+a+"&b="+b+"&c="+c+"&d="+d+"&e="+e+"&f="+f+"&g="+g+"&ignore=.csv"
    return yfURL
def download(filePath, urlOfFile):
    import requests

    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
         'Accept-Language':'en-US,en;q=0.8',
         'Accept-Encoding':'none',
         'Connection':'keep-alive'}

    try:
        page = requests.get(urlOfFile,headers=header)
        content=page.content

        with open(filePath, 'wb') as output:
            output.write(bytearray(content))
    except requests.HTTPError:
        e=requests.HTTPError.strerror
        print("e")
