import pyttsx3 # importing dependencies 

friend = pyttsx3.init() #initializing the pyttsx3 library

friend.say(" I was made by hilary to help him read without stress, i will always serve him as he wishes. i love my creator Hilary. and i will do anything to make him happy") #add text to change to voice 


voices = friend.getProperty("voices") # set voice 

friend.setProperty("voice" , voices[1].id) # voice type "female"

friend.runAndWait() # run program
