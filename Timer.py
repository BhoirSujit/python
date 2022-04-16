import time as t;

def countDown(k):
    for i in range(k, 0, -1):
        t.sleep(1)
        print(i)

if __name__ == "__main__":
    v = int(input("Enter time for count down : "))
    countDown(v)