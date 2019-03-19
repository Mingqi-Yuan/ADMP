"""
Encoding = UTF-8
By Mingqi, Yuan, 2019/3/18
Usage: Generate unique id for each image
"""
from datetime import datetime

def generate_unique_id():
    time_now = str(datetime.now()).split('.')
    time_now[0] = time_now[0].split(' ')
    time_now[0][1] = time_now[0][1].split(':')
    id = time_now[0][0] + '_' + time_now[0][1][0] + '_' + time_now[0][1][1] + '_' + time_now[0][1][1] + '_' + time_now[1] + '.jpg'

    return id


