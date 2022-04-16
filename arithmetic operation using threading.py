import threading
def multiplication(num):
    print("\nMultiplication: {}".format(num * num))
def addition(num):
    print("\nAddition: {}".format(num + num))
def division(num):
    print("\nDivision: {}".format(num / num))
def substraction(num):
    print("\nsubstraction: {}".format(num - num))
if __name__ == "__main__":
    t1 = threading.Thread(target=multiplication, args=(20,))
    t2 = threading.Thread(target=addition, args=(5,))
    t3 = threading.Thread(target=division, args=(100,))
    t4 = threading.Thread(target=substraction, args=(3,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()