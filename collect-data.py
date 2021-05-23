import cv2
import numpy as np
import os

# Create the directory structure
if not os.path.exists("data"):
    os.makedirs("data")
    os.makedirs("data/train")
    os.makedirs("data/test")
    os.makedirs("data/train/0")
    os.makedirs("data/train/1")
    os.makedirs("data/train/2")
    os.makedirs("data/train/3")
    os.makedirs("data/train/4")
    os.makedirs("data/train/5")
    os.makedirs("data/train/6")
    os.makedirs("data/train/7")
    os.makedirs("data/train/8")
    #os.makedirs("data/train/9")
    
    os.makedirs("data/test/0")
    os.makedirs("data/test/1")
    os.makedirs("data/test/2")
    os.makedirs("data/test/3")
    os.makedirs("data/test/4")
    os.makedirs("data/test/5")
    os.makedirs("data/test/6")
    os.makedirs("data/test/7")
    os.makedirs("data/test/8")
    #os.makedirs("data/test/9")
    

# Train or test 
mode = 'test'
# Directory Path
directory = 'data/'+mode+'/'

# Capturing the Webcam Feed.0 corresponds to our webcam. If there are multiple webcams then it can be 1,2,etc.
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Getting count of existing images
    count = {'A': len(os.listdir(directory+"/0")),
             'B': len(os.listdir(directory+"/1")),
             'C': len(os.listdir(directory+"/2")),
             'I': len(os.listdir(directory+"/3")),
             'L': len(os.listdir(directory+"/4")),
             'O': len(os.listdir(directory+"/5")),
             'V': len(os.listdir(directory+"/6")),
             'W': len(os.listdir(directory+"/7")),
             'X': len(os.listdir(directory+"/8")),
             #'O': len(os.listdir(directory+"/9"))
             }
    
    # Printing the count in each set to the screen
    cv2.putText(frame, "MODE : "+mode, (10, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1)
    cv2.putText(frame, "IMAGE COUNT", (10, 100), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1)
    cv2.putText(frame, "A (Press 0 to save): "+str(count['A']), (10, 120), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "B (Press 1 to save): "+str(count['B']), (10, 140), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "C (Press 2 to save): "+str(count['C']), (10, 160), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "I (Press 3 to save): "+str(count['I']), (10, 180), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "L (Press 4 to save): "+str(count['L']), (10, 200), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "O (Press 5 to save): "+str(count['O']), (10, 220), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "V (Press 6 to save): "+str(count['V']), (10, 240), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "W (Press 7 to save): "+str(count['W']), (10, 260), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    cv2.putText(frame, "X (Press 8 to save): "+str(count['X']), (10, 280), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    #cv2.putText(frame, "O (Press 9 to save): "+str(count['O']), (10, 300), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 1)
    
    # Coordinates of the ROI
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    # Drawing the ROI
    # The increment/decrement by 1 is to compensate for the bounding box
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    # Extracting the ROI
    roi = frame[y1:y2, x1:x2]
    roi = cv2.resize(roi, (64, 64)) 
 
    cv2.imshow("Frame", frame)
    
    #_, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
    #kernel = np.ones((1, 1), np.uint8)
    #img = cv2.dilate(mask, kernel, iterations=1)
    #img = cv2.erode(mask, kernel, iterations=1)
    # do the processing after capturing the image!
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("ROI", roi)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
    if interrupt & 0xFF == ord('0'):
        cv2.imwrite(directory+'0/'+str(count['A'])+'.jpg', roi)
    if interrupt & 0xFF == ord('1'):
        cv2.imwrite(directory+'1/'+str(count['B'])+'.jpg', roi)
    if interrupt & 0xFF == ord('2'):
        cv2.imwrite(directory+'2/'+str(count['C'])+'.jpg', roi)
    if interrupt & 0xFF == ord('3'):
        cv2.imwrite(directory+'3/'+str(count['I'])+'.jpg', roi)
    if interrupt & 0xFF == ord('4'):
        cv2.imwrite(directory+'4/'+str(count['L'])+'.jpg', roi)
    if interrupt & 0xFF == ord('5'):
        cv2.imwrite(directory+'5/'+str(count['O'])+'.jpg', roi)
    if interrupt & 0xFF == ord('6'):
        cv2.imwrite(directory+'6/'+str(count['V'])+'.jpg', roi)
    if interrupt & 0xFF == ord('7'):
        cv2.imwrite(directory+'7/'+str(count['W'])+'.jpg', roi)
    if interrupt & 0xFF == ord('8'):
        cv2.imwrite(directory+'8/'+str(count['X'])+'.jpg', roi)
    #if interrupt & 0xFF == ord('9'):
        #cv2.imwrite(directory+'9/'+str(count['O'])+'.jpg', roi)
    
cap.release()
cv2.destroyAllWindows()
"""
d = "old-data/test/0"
newd = "data/test/0"
for walk in os.walk(d):
    for file in walk[2]:
        roi = cv2.imread(d+"/"+file)
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
        cv2.imwrite(newd+"/"+file, mask)     
"""
