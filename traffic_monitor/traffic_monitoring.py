import cv2
import matplotlib.pyplot as plt
import time
import sys

starting_time = time.time()
t1_light = 'red'
t2_light = 'green'
string = ""


def time_manager(d1, d2):

    global t1_light, t2_light, starting_time, string
    string = ""

    if(d1 > d2):

        if(t2_light == 'green'):
            # changes from yellow to red for t2 and green for t1
            string += "e561_23 e561_9 "  # yellow on T1, yellow on T2
            # time.sleep(6)  # process of changing from yellow

        if(t1_light != 'green'):
            t1_light = 'green'
            starting_time = time.time()

        if(t2_light != 'red'):
            t2_light = 'red'

    if(d2 > d1):

        if(t1_light == 'green'):
            # changes from yellow to red for t2 and green for t1
            string += "e561_23 e561_9 "  # yellow on T1, yellow on T2
            # time.sleep(6)  # process of changing from yellow

        if(t2_light != 'green'):
            t2_light = 'green'
            starting_time = time.time()

        if(t1_light != 'red'):
            t1_light = 'red'

    if(t1_light == 'red'):
        string += "e561_22 "  # red on T1
    elif(t1_light == 'green'):
        string += "e561_24 "  # green on T1

    if(t2_light == 'red'):
        string += "e561_8 "  # red on T2
    elif(t2_light == 'green'):
        string += "e561_10 "  # green on T2


cap = cv2.VideoCapture('assets/traffic_on_two_roads.mp4')

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('assets/cars.xml')

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
            if y <= 240:
                if y - (0.71 * x) + 299.42 > 0:
                    if w*h > 2000:
                        cv2.rectangle(frames, (x, y),
                                      (x+w, y+h), (0, 0, 255), 2)
                        count1 = count1 + 1
            else:
                if y - (0.78 * x) + 91.7 > 0:
                    if w*h > 2000:
                        cv2.rectangle(frames, (x, y),
                                      (x+w, y+h), (0, 255, 0), 2)
                        count2 = count2 + 1

        counter += 1

        avg1 += count1 / 6
        avg2 += count2 / 6

        if counter % 6 == 0:
            avg1 = round(avg1)
            avg2 = round(avg2)
            time_manager(avg1, avg2)
            print(string)
            sys.stdout.flush()

            avg1 = 0
            avg2 = 0

        cv2.imshow('Traffic Monitoring on 2 roads', frames)

        if cv2.waitKey(15) == 27:
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
