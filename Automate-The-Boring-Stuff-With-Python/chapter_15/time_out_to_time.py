import datetime
import time
halloween2017 = datetime.datetime(2017, 3, 1, 17, 0, 0)
while datetime.datetime.now() < halloween2017:
    print("hello " + str(round(time.time(),2)))
    time.sleep(1)


    
