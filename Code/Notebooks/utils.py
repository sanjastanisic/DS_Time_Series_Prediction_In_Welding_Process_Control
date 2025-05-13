from collections import namedtuple
import datetime

def square(x):
    return x*x

Date_Seq = namedtuple('Date_Seq', ['year', 'month', 'day'])

Time_Seq = namedtuple('Time_Seq', ['year', 'month', 'day', 'hour', 'minute', 'second', 'sequence'])

def extract_date(date_str, separator='_'):
    date_str = date_str.split('.')[0]
    a = date_str.split(separator)
    y = int(a[0])
    m = int(a[1])
    d = int(a[2])
    return Date_Seq(y, m, d)

def extract_time(time_str, separator='-'):
    time_str = time_str.split('.')[0]
    a = time_str.split(separator)
    y = int(a[0])
    m = int(a[1])
    d = int(a[2])
    h = int(a[3])
    mi = int(a[4])
    se = int(a[5])
    seq = int(a[6])
    return Time_Seq(y, m, d, h, mi, se, seq)

def are_neighbours(ts1, ts2):
    if abs(ts1.sequence-ts2.sequence) <= 1:
        return True
    else:
        if( ts2.sequence == 0 and ts1.sequence == 9999 ):
            return True
        else:
            return False
        
def min_max_avg_count(number_list):
    try:
        number_list = number_list[1:-1].split(",")
        number_list = [eval(i) for i in number_list]
        min = number_list[0]
        max = number_list[0]
        sum = number_list[0]
        count = 1
        for i in range(1,len(number_list)):
            if( number_list[i] < min):
                min = number_list[i]
            if( number_list[i] > max):
                max = number_list[i]
            sum += number_list[i]
            count += 1
        return (min, max, sum/count, count)
    except:
        return (None,None,None,None)

def sampling_intervals():
    return ['5s', '1s', '100ms'] # '1ms'
    # return ['5s', '1s', '100ms', '20ms'] 

def develop_mode():
    return True
    #return False
