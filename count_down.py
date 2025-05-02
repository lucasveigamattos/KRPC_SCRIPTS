import time

def count_down():
    for i in range(10, -1, -1):
        time.sleep(1)
        print(i)