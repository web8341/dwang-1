# This module

def getRawData(ticket,start_date,end_date,option,buf=300):
    qtype=options['qtype']
    stockTable=options['qtype'][0]
    daysTable=options['qtype'][1]

    query = 'select c.timestamp, c.' + qtype + ', t.month, t.day, t.dayofweek, '\
        
