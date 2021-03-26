import pyttsx3 # importing dependencies 

friend = pyttsx3.init() #initializing the pyttsx3 library

friend.say("my name is hilary and i am a good boy") #add text to change to voice 


voices = friend.getProperty("voices") # set voice 

friend.setProperty("voice" , voices[1].id) # voice type "female"

friend.runAndWait() # run program
