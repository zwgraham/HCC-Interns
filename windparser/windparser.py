#!/usr/bin/env python

import csv
import datetime
import dateutil.relativedelta as relativedelta

def str2datetime(x,y):
    return datetime.datetime(int(x)/10000, int(x)/100%100, int(x)%100, int(y)/100, int(y)%100)



starttime=datetime.datetime(2012,01,01,00,00)
INPUT='201201wind.csv'
OUTPUT='pocessed.wnd'

infile=csv.reader(file(INPUT, 'r'))
headers=infile.next()

#ensure we have the correct indices
D=headers.index('Date')
T=headers.index('Time')
W=headers.index('WindSpeed')

temp_array=[]
working_datetime=starttime
print str(working_datetime)
reltime=relativedelta.relativedelta(hours=+1)
for row in infile:
    temptime=str2datetime(row[D],row[T])
    print'\t'+str(temptime)
    if((working_datetime<=temptime) and (temptime<(working_datetime+reltime))):
        #datetime matches
        temp_array.append(float(row[W])) ## save data
    elif(temptime>=(working_datetime+reltime)):
        #moved to new timeslot,
        ##process old data
        if len(temp_array)==0:
            print ' no data'
        else:
            averageWindspeed=sum(temp_array)/float(len(temp_array))
            print averageWindspeed
        ##write to file
        ##reset variables
        working_datetime=working_datetime+reltime
        print str(working_datetime)
        temp_array=[]
        ##begin processing new data
        temp_array.append(float(row[W]))
    else:
        print 'ERROR'
        print row
        break
        



    
