#!/usr/bin/env python

import csv
import datetime
import dateutil.relativedelta as relativedelta
import sys

def str2datetime(x,y):
    return datetime.datetime(int(x)/10000, int(x)/100%100, int(x)%100, int(y)/100, int(y)%100)

def str2date(x):
    return datetime.date(int(x)/10000, int(x)/100%100, int(x)%100)

def str2time(x):
    return datetime.time(int(x)/100, int(x)%100)

INPUT=sys.argv[1]+'.csv'
OUTPUT=sys.argv[1]+'.wnd'
firstrow=True
starttime=datetime.datetime(2012,01,01,00,00)
#INPUT='201201wind.csv'
#OUTPUT='pocessed.wnd'
f=file(INPUT,'r')
infile=csv.reader(f)
headers=infile.next()
outfile=file(OUTPUT,'w')
#ensure we have the correct indices
D=headers.index('Date')
T=headers.index('Time')
W=headers.index('WindSpeed')

temp_array=[]
working_datetime=starttime

reltime=relativedelta.relativedelta(hours=+1)
for row in infile:
    temptime=str2datetime(row[D],row[T])
    if (firstrow==True):
        working_datetime=str2datetime(row[D], 000)
        firstrow=False

    if((working_datetime<=temptime) and (temptime<(working_datetime+reltime))):
        #datetime matches
        try:
            temp_array.append(float(row[W])) ## save data
        except ValueError:
            print 'LINE ERROR'+str(infile.line_num)+' '+INPUT
    elif(temptime>=(working_datetime+reltime)):
        #moved to new timeslot,
        ##process old data
        if len(temp_array)==0:
            averageWindspeed=0.0
        else:
            averageWindspeed=sum(temp_array)/float(len(temp_array))
            
        sys.stdout.write(str(working_datetime)+'\t%.2f\t%d\n'%(averageWindspeed, len(temp_array)))
        ##convert to m/s
        averageWindspeed*=0.44704 #mph to m/s
        ##write to file
        outfile.write('%.4f\r\n'%(averageWindspeed))
        ##reset variables
        working_datetime=working_datetime+reltime
        temp_array=[]
        ##begin processing new data
        try:
            temp_array.append(float(row[W]))
        except ValueError:
            print 'LINE ERROR'+str(infile.line_num)+' '+INPUT
    else:
        print 'ERROR'
        print row
        break
        



    
