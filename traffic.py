

""" import threading

def set_interval(func,sec):
    def func_wrapper():
        set_interval(func,sec)
        func()
    t=threading.Timer(sec,func_wrapper)
    t.start()
    return t

x=set_interval(lambda: print("helli"),4)

 """

 #python code to determine time according to determined densities
import time

starting_time = time.time()
t1_light='red'
t2_light='green'

def time_manager(d1,d2):
    if(d1>d2 and time.time()-starting_time>20 and time.time()-starting_time<60):

        if(t2_light=='green'):
            print("YELLOW ON T1") #changes from yellow to red for t2 and green for t1
            print("YELLOW ON T2")
            time.sleep(6) #process of changing from yellow

        
        
        
        