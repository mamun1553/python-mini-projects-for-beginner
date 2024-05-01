import os

# importing text to speech library. there are two kinds of text to speech library. gtts and pyttsx3
# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

import pyttsx3
engine = pyttsx3.init()
# engine.say("hellow")
# engine.runAndWait()

# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:

file = open("textfile.txt", "r")
# print(file.read())
file_read = file.read().replace("\n", " ")

engine.setProperty('rate', 130)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)

# engine.save_to_file(file_read, 'audiobook.mp3')
engine.say(file_read)
file.close()
engine.runAndWait()
# os.system("start audiobook.mp3")

