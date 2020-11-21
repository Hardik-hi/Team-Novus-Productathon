import cv2
import time

def distance(x1, x2, y1, y2):
    
    sum = ((x1 - x2)**2 + (y1 - y2)**2)**1/2
    return sum


cap = cv2.VideoCapture("videoplayback.mp4")

subtractor = cv2.createBackgroundSubtractorMOG2(history = 50, varThreshold = 20)

base_centers = []
curr_centers = []
prev_centers = []

threshold = 1000

count = 0
distances = []

thresh = 10000000

it = 0
el = 0

res = 1
while res:
    res, frame = cap.read()

    mask = subtractor.apply(frame)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    k = 0

    flag = 0

    for cnts in contours:
            (x, y, w, h) = cv2.boundingRect(cnts)

            if w * h > 1000:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                
                #print(x + w/2, y + h/2)
                
                if count % 5 == 0:
                    it = time.time()
                    elapsed = el - it
                    el = it
                    base_centers.append([x + w/2, y + h/2, k])
                    #print(base_centers)
                    speeds = []
                    for i in range(len(base_centers)):
                        for j in range(len(curr_centers)):
                            if base_centers[i][2] == curr_centers[j][2]:
                                dist = distance(base_centers[i][0], curr_centers[j][0], base_centers[i][1], curr_centers[j][1])
                                speeds.append(dist/elapsed)
                                #print(speeds)
                    prev_centers = []
                    prev_centers.extend(base_centers)
                else:

                    curr_centers = []
                    curr_centers.append([x + w/2, y + h/2])
                    print("prev:" , prev_centers)
                    
                    
                    for i in range(len(curr_centers)):
                        for j in range(len(prev_centers)):
                            dist = distance(prev_centers[j][0], curr_centers[i][0], prev_centers[j][1], curr_centers[i][1])
                            #print(dist)
                            if dist < threshold and dist != 0 :
                                if dist < thresh:
                                    thresh = dist
                                    print(thresh)
                                    flag = j
                        curr_centers[i].append(flag)
                    print("curr:", curr_centers)
                    prev_centers = []
                    prev_centers.extend(curr_centers)
                    

                            

                k += 1
        

    cv2.imshow("Frame", frame)

    cv2.imshow("mask", mask)

    count += 1

    key = cv2.waitKey(30)
    if key == 27:
        break
