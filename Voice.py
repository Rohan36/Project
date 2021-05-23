# Import the gTTS module for text  
# to speech conversion  
from gtts import gTTS  
  
# This module is imported so that we can  
# play the converted audio  
  
from playsound import playsound  
  
# It is a text value that we want to convert to audio  
t0 = ' A'  
t1 = ' B'
t2 = ' C'
t3 = ' I'
t4 = ' L'
t5 = ' O'
t6 = ' V'
t7 = ' W'
t8 = ' X'
 
# Here are converting in English Language  
language = 'en'  
  
# Passing the text and language to the engine,  
# here we have assign slow=False. Which denotes  
# the module that the transformed audio should  
# have a high speed  
#obj = gTTS(text=t0, lang=language, slow= False)  
#obj = gTTS(text=t1, lang=language, slow= False) 
#obj = gTTS(text=t2, lang=language, slow= False)  
#obj = gTTS(text=t3, lang=language, slow=False)  
#obj = gTTS(text=t4, lang=language, slow=False)  
#obj = gTTS(text=t5, lang=language, slow=False)  
#obj = gTTS(text=t6, lang=language, slow=False)  
#obj = gTTS(text=t7, lang=language, slow=False)   
obj = gTTS(text=t8, lang=language, slow=False)  
  
#Here we are saving the transformed audio in a mp3 file named  
# exam.mp3  
#obj.save("A.mp3")  
#obj.save("B.mp3")  
#obj.save("C.mp3")
#obj.save("I.mp3")
#obj.save("L.mp3")
#obj.save("O.mp3")
#obj.save("V.mp3")
#obj.save("W.mp3")
obj.save("X.mp3")
  
# Play the exam.mp3 file  
#playsound("exam.mp3")  
#playsound("A.mp3")