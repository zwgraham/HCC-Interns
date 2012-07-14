#!/usr/bin/env python

import csv
import datetime
import dateutil.relativedelta as relativedelta
import sys

def str2datetime(x,y):
    return datetime.datetime(int(x)/10000, int(x)/100%100, int(x)%100, int(y)/100, int(y)%100)






starttime=datetime.datetime(2012,01,01,00,00)

INPUT=sys.argv[1]+'.csv'
OUTPUT=sys.argv[1]+'.wnd'
#INPUT='01jan2012.csv'
#OUTPUT='jan.wnd'
f=file(INPUT,'r')
infile=csv.reader(f)
headers=infile.next()

#ensure we have the correct indices
D=headers.index('Date')
T=headers.index('Time')
W=headers.index('WindSpeed')

outfile=file(OUTPUT,'w')

temp_array=[]
working_datetime=starttime

reltime=relativedelta.relativedelta(hours=+1)
for row in infile:
    temptime=str2datetime(row[D],row[T])
    if((working_datetime<=temptime) and (temptime<(working_datetime+reltime))):
        #datetime matches
        try:
            temp_array.append(float(row[W])) ## save data
        except ValueError:
            print 'LINE ERROR'+str(infile.line_num)
    elif(temptime>=(working_datetime+reltime)):
        #moved to new timeslot,
        ##process old data
        if len(temp_array)==0:
            averageWindspeed=0.0
        else:
            averageWindspeed=sum(temp_array)/float(len(temp_array))
        ##convert to m/s
        averageWindspeed*=0.44704 #mph to m/s
        sys.stdout.write(str(working_datetime)+'\t%.2f\t%d\n'%(averageWindspeed, len(temp_array)))
        ##write to file
        outfile.write('%.4f\n'%(averageWindspeed))
        ##reset variables
        working_datetime=working_datetime+reltime
        temp_array=[]
        ##begin processing new data
        try:
            temp_array.append(float(row[W]))
        except ValueError:
            print 'LINE ERROR'+str(infile.line_num)
    else:
        print 'ERROR'
        print row
        break

outfile.close()
f.close()
        



    
