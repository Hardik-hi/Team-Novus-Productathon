#python code to determine time according to determined densities
import time

starting_time = time.time()
t1_light='red'
t2_light='green'

#function that turns on and off the lights accordingly
def time_manager(d1,d2):

    global t1_light,t2_light,starting_time

    if(d1>d2 and time.time()-starting_time>20 and time.time()-starting_time<60):

        if(t2_light=='green'):
            print("YELLOW ON T1") #changes from yellow to red for t2 and green for t1
            print("YELLOW ON T2")
            time.sleep(6) #process of changing from yellow

        if(t1_light!='green'):
            t1_light='green'
            starting_time=time.time()
        
        if(t2_light!='red'):
            t2_light='red'
        
    #if traffic is more at t2

    if(d2>d1 and time.time()-starting_time>20 and time.time()-starting_time<60):

        if(t1_light=='green'):
            print("YELLOW ON T1") #changes from yellow to red for t2 and green for t1
            print("YELLOW ON T2")
            time.sleep(6) #process of changing from yellow

        if(t2_light!='green'):
            t2_light='green'
            starting_time=time.time()
        
        if(t1_light!='red'):
            t1_light='red'

    print("T1 IS ",t1_light)
    print("T2 IS ",t2_light)




def master():
    d1=int(input("t1 density"))
    d2=int(input("t2 density"))
    time.sleep(21)
    time_manager(d1,d2)

master()

    
        
        