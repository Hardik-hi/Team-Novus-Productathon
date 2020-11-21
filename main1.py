import cv2 
  
cap = cv2.VideoCapture('footage2.mp4') 

# Trained XML classifiers describes some features of some object we want to detect 
car_cascade = cv2.CascadeClassifier('cars.xml') 
  
while(cap.isOpened()): 
    ret, frames = cap.read() 
      
    if ret == True:
        count = 0
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
  
        # Detects cars of different sizes in the input image 
        cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
      
        for (x,y,w,h) in cars: 
            if w*h > 2500:

                cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
                cv2.circle(frames, (x+w//2, y+h//2), 1, (0,255,255), 2)
                count = count + 1

        if count < 5:
            print("Less...")
        elif count > 5 and count < 20:
            print("Moderate...")
        else:
            print("Heavy...")
  
        cv2.imshow('video', frames) 
      
        if cv2.waitKey(15) == 27: 
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()
