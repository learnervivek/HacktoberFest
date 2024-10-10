import pyttsx3
engine = pyttsx3.init()
engine.say("hello vivek how are you feeling today?")
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 100)     # setting up new voice rate

engine.runAndWait()

