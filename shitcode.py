import datetime
import random
import time

def print_time():
    twenty_three_hours = 23*60*60
    start_time = datetime.datetime.now()
    just_wait_a_lil = {
        1: 'close..',
        2: '..',
        3: "don't be an asshole, just wait",
        4: "not so fast",
        5: 'almost done',
        6: 'you can slepp a little',
        7: 'time is relative, brah'
    }
    print start_time

    while  datetime.datetime.now() <  start_time + datetime.timedelta(seconds=twenty_three_hours):
        print(just_wait_a_lil[random.randint(1,7)])
        time.sleep(1)
    return datetime.datetime.now()
