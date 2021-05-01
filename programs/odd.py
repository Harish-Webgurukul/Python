from datetime import datetime
from time import sleep
from random import randint
#import time
#import random

odds =[22,23,25,27,28,29,30]

for i in range(5):
    sleep(5)
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print("minute is little odd")
    else:
        print("Not odd")
