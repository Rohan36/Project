from gtts import gTTS  
from playsound import playsound 



import numpy as np
from keras.models import model_from_json
import operator
import cv2
import sys, os

# Loading the model
json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
# load weights into new model
loaded_model.load_weights("model-bw.h5")
print("Loaded model from disk")

cap = cv2.VideoCapture(0)

# Category dictionary
categories = {0: 'A', 1: 'B', 2: 'C', 3: 'I', 4: 'L', 5: 'O', 6: 'V', 7: 'W', 8:'X'}

while True:
    _, frame = cap.read()
    # Simulating mirror image
    frame = cv2.flip(frame, 1)
    
    # Got this from collect-data.py
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
    
    # Resizing the ROI so it can be fed to the model for prediction
    roi = cv2.resize(roi, (64, 64)) 
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, test_image = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("test", test_image)
    # Batch of 1
    result = loaded_model.predict(test_image.reshape(1, 64, 64, 1))
    prediction = {'A': result[0][0], 
                  'B': result[0][1], 
                  'C': result[0][2],
                  'I': result[0][3],
                  'L': result[0][4],
                  'O': result[0][5],
                  'V': result[0][6],
                  'W': result[0][7],
                  'X': result[0][8],
                  }
    # Sorting based on top prediction
    prediction = sorted(prediction.items(), key=operator.itemgetter(1), reverse=True)
    
    #if prediction[0][0] == 'A':
       # playsound("A.mp3")
    #if prediction[0][0] == 'B':
        #playsound("B.mp3")
    #if prediction[0][0] == 'C':
        #playsound("C.mp3")
    #if prediction[0][0] == 'I':
     #   playsound("C.mp3")
    if prediction[0][0] == 'L':
        playsound("L.mp3")
    #if prediction[0][0] == 'O':
        #playsound("O.mp3")
    #if prediction[0][0] == 'V':
     #   playsound("C.mp3")
    if prediction[0][0] == 'W':
        playsound("W.mp3")
    #if prediction[0][0] == 'X':
      #  playsound("C.mp3")
        
    # Displaying the predictions
    cv2.putText(frame, prediction[0][0], (10, 120), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 2)    
    cv2.imshow("Frame", frame)
    
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == 27: # esc key
        break
        
 
cap.release()
cv2.destroyAllWindows()
