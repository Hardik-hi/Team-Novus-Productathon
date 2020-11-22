import cv2
import matplotlib.pyplot as plt
import time
#python code to determine time according to determined densities


starting_time = time.time()
t1_light='red'
t2_light='green'

#function that turns on and off the lights accordingly
def time_manager(d1,d2):

    global t1_light,t2_light,starting_time

    if(d1>d2):

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

    if(d2>d1):

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

    
        
        
cap = cv2.VideoCapture('video_final.mp4')

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')

counter = 0

avg1 = 0
avg2 = 0
while(cap.isOpened()):
    ret, frames = cap.read()

    if ret == True:
        count1 = 0
        count2 = 0
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

        # Detects cars of different sizes in the input image
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        for (x, y, w, h) in cars:
            if y<= 240:
                if y - (0.71 * x) + 299.42 > 0:
                    if w*h > 2000:
                        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 0, 255), 2)
                        count1 = count1 + 1
            else:
                if y - (0.78 * x) + 91.7 > 0:
                    if w*h > 2000:
                        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        count2 = count2 + 1

        cv2.imshow('video', frames)
    
        counter += 1

        avg1 += count1 / 6
        avg2 += count2 / 6

        
        if counter % 6 == 0:
            avg1 = round(avg1)
            avg2 = round(avg2)
            print("Sent:" , avg1, avg2)
            time_manager(avg1, avg2)
            avg1 = 0
            avg2 = 0
        
        if cv2.waitKey(15) == 27:
            break
    
    else:
        break

cap.release()
cv2.destroyAllWindows()
