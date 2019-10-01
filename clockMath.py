import datetime

def hms():
    x=str(datetime.datetime.now())
    x=x.split(" ")
    x=x[1]
    x=x.split('.')
    x=x[0]
    x=x.split(':')
    return x
