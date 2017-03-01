from setup import *

def getRawData(ticker,start_date,end_date,options,buf=300):
    dtype=options['qtype']
    stockTable=option['tables'][0]
    daysTable = option['tables'][1]

    query = 'select c.timestamp,c. ' + qtype + ' ,t.month,t.day,t.dayOfWeek,' \
             't.tDaysLeftMonth,t.tDayinMonth,t.tDayinWeek from' \
             ' ' + stockTable + ' c left join ' + daysTable + ' t on c.timestamp=t.tDay' \
             ' where c.symbol=%s and c.timestamp<%s and ' \
             't.id>=(select max(id) from tradingDays where tDay<=%s)-%s order by timestamp desc'
    params=(ticker,start_date,end_date,buf)
    rawData=getQuery(query,params)
    ticketDataRaw=pd.DataFrame(rawData,columns=["Timestamp","Price","Month","Day","DayofWeek","tDaysleftMonth","tDaysleftWeek")]
    ticketDataRaw.index=ticketDataRaw["Timestamp"]
    del ticketDataRaw["Timestamp"]
    return ticketDataRaw

def insertRawData(ticker,start_date,end_date,options,buf=300):
    dtype=options['qtype']
    stockTable=option['tables'][0]
    daysTable = option['tables'][1]

    query = 'select c.timestamp,c. ' + qtype + ' ,t.month,t.day,t.dayOfWeek,' \
             't.tDaysLeftMonth,t.tDayinMonth,t.tDayinWeek from' \
             ' ' + stockTable + ' c left join ' + daysTable + ' t on c.timestamp=t.tDay' \
             ' where c.symbol=%s and c.timestamp<%s and ' \
             't.id>=(select max(id) from tradingDays where tDay<=%s)-%s order by timestamp desc'
    params=(ticker,start_date,end_date,buf)
    rawData=getQuery(query,params)
    ticketDataRaw=pd.DataFrame(rawData,columns=["Timestamp","Price","Month","Day","DayofWeek","tDaysleftMonth","tDaysleftWeek")]
    ticketDataRaw.index=ticketDataRaw["Timestamp"]
    del ticketDataRaw["Timestamp"]
    return ticketDataRaw

def getQuery(query,params):
    config={
        'user':'dave',
        'password':'whh001',
        'host':'local',
        'database':'stock'
    }
    conn = psycopg2.connect(*config)

    c=conn.cursor()
    c.excute('set autocommit=1')
    c.excute('set global max_allowed_packet=1073741824;')
    c.excute(query,params)
    data=c.fetchall()
    conn.close()
    return data
