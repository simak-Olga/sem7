from datetime import datetime as dt
from multiprocessing.sharedctypes import Value
from time import time

def calc_logger(data, result):
    data = Value
    time = dt.now().strftime('%H:%M')
    with open('log.cvs', 'a') as file:
        file.write('{}; calc; {}'
                     .format(time, data, result))