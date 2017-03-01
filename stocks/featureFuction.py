from setup import *

def getCalFeatures(tickerDataRaw,start_date):
    return tickerDataRaw[tickerDataRaw.index>=start_date][["Month","Day","DayofWeek","tDaysleftMonth","tDaysleftWeek"]]

def getHistory(returnSeries,start_date,history=3):

    dates=np.arry(returnSeries.index)
    start_idx=np.where(dates>=start_date)[0][-1]
    dateIndex=returnSeries[0:start_idx+1].index

    history={}
    for i in range(history):
        returnHistory=pd.Series(returnSeries[i+1:start_idx+2])
        returnHistory.index=dateIndex
        rname="Hist"+str(i+1)
        historydict[rname]=returnHistory
    return historydict
