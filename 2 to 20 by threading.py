import threading
import time
def Evennum():
    for i in range(2, 22, 2):
        time.sleep(2)
        print(i)
threading.Thread(target=Evennum).start()