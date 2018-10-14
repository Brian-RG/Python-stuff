from _thread import start_new_thread as p

a=100000
def b(r):
    global a
    print("Hi from thread ",r)
    for i in range(100):
        a-=2
        print("Value of a is ",a)
def c(r):
    global a
    print("Hi from thread ",r)
    for j in range(100):
        a+=5
        print("Value of a is ",a)
def d(r):
    global a
    print("Hi from thread ",r)
    for k in range(100):
        a-=10
        print("Value of a is ",a)
p(b,(1,))
p(c,(2,))
p(d,(3,))