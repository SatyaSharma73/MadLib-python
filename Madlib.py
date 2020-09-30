import vlc
import time
import pyttsx3

engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 170)     # setting up new voice rate
"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1
"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female


sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\sound3.mp3")
sound_file.play()
time.sleep(0)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part1.mp3")
sound_file.play()
print("Get ready to think some words")
time.sleep(8)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part2.mp3")
sound_file.play()
print("This Is Mad Libs")
time.sleep(2)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part3.mp3")
sound_file.play()
print("The World Greatest Word Game")
time.sleep(2)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part4.mp3")
sound_file.play()
print("I Will Help You To Fill In The Blanks ")
time.sleep(2.5)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part6.mp3")
sound_file.play()
print("It's time to get creative")
time.sleep(2.5)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part7.mp3")
sound_file.play()
p1=input("First word i need a person in room")
time.sleep(0)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part8.mp3")
sound_file.play()
print("Good ! ")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part9.mp3")
sound_file.play()
p2 = input("Say a verb ending in 'ING'")
time.sleep(0)


sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part10.mp3")
sound_file.play()
print("COOL")
time.sleep(2)


sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part16.mp3")
sound_file.play()
p17 = input("Alright I need a prural noun.")
time.sleep(0)




sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part14.mp3")
sound_file.play()
print("Nice One")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part15.mp3")
sound_file.play()
p5 = input("How about a Number")
time.sleep(0)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part12.mp3")
sound_file.play()
print("That's the way ")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part16.mp3")
sound_file.play()
p6 = input("Alright i need a prural noun")
time.sleep(0)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part19.mp3")
sound_file.play()
print("Way to go ")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part17.mp3")
sound_file.play()
p7 = input("Give me a Noun")
time.sleep(0)


sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part8.mp3")
sound_file.play()
print("Good")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part18.mp3")
sound_file.play()
p8 = input("say a verb's past tense")
time.sleep(0)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part12.mp3")
sound_file.play()
print("That's the way ")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part20.mp3")
sound_file.play()
p9 = input("How about a type of food")
time.sleep(0)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part22.mp3")
sound_file.play()
print("OKAY ")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part21.mp3")
sound_file.play()
p10 = input("You have played before huh , a type of liquid ")
time.sleep(0)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part22.mp3")
sound_file.play()
print("okay ")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part24.mp3")
sound_file.play()
p12 = input("say a colour")
time.sleep(0)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part8.mp3")
sound_file.play()
print("Good ")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part25.mp3")
sound_file.play()
p13=input("Alright I need a noun")
time.sleep(0)



sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part16.mp3")
sound_file.play()
p14 = input("Alright i need a prural noun.")
time.sleep(0)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part22.mp3")
sound_file.play()
print("OKAY")
time.sleep(3)


sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part26.mp3")
sound_file.play()
p15=input("4 words left ,Tell me a number")
time.sleep(0)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part14.mp3")
sound_file.play()
print("Nice One")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part24.mp3")
sound_file.play()
p16 = input("Say a colour")
time.sleep(0)


sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part8.mp3")
sound_file.play()
print("Good ")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part13.mp3")
sound_file.play()
p4 = input("I need an animal")
time.sleep(0)


sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part22.mp3")
sound_file.play()
print("OKAY")
time.sleep(3)


sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part28.mp3")
sound_file.play()
p18 = input("And finally tell me a noun ")
time.sleep(0)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part12.mp3")
sound_file.play()
print("That's the way !")
time.sleep(3)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part29.mp3")
sound_file.play()
print("Well done.")
time.sleep(2)

sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part30.mp3")
sound_file.play()
print("Time to read")
time.sleep(5)

c='The appropriate title i guess should be Thanksgiving'
print(" The appropriate title i guess should be Thanksgiving")

engine.say(c)
engine.runAndWait()
engine.stop()
time.sleep(2)

print("It was thanksgiving,I asked ",p1,"about scent of succlent roasted ",p2,"through my house")
line1='It was thanksgiving,I asked'+p1,'about scent of succlent roasted '+p2,'through my house'
engine.say(line1)
engine.runAndWait()
engine.stop()

print("Thanksgiving is my favorite holidays. The huge",p4,"sat steaming weighing about",p5,"killos. The table was laid with every kind of",p7,"imaginable.")
line2='Thanksgiving is my favorite holidays. The huge'+p4,'sat steaming weighing about'+p5,'killos. The table was laid with every kind of'+p7,'imaginable.'
engine.say(line2)
engine.runAndWait()
engine.stop()

print("There ws a basket of hot buttered",p6,"and glass of sparkling",p10,".It's time to eat",p9,".my mother",p8,"! I could not wait to get my present on that day,")
line3='There ws a basket of hot buttered'+p6,'and glass of sparkling'+p10,'.It''s time to eat'+p9,'.my mother'+p8,'! I could not wait to get my present on that day'
engine.say(line3)
engine.runAndWait()
engine.stop()

print("A bowl of ruby-",p12,",",p13,"sauce,a sweet casserole,a dish of mashed potatoes on the table number",p15,". The",p16,"lights on the table",p17,"was mindblowing.")
line4='A bowl of ruby-'+p12,','+p13,'sauce,a sweet casserole,a dish of mashed potatoes on the table number'+p15,'. The'+p16,'lights on the table'+p17,'was mindblowing.'
engine.say(line4)
engine.runAndWait()
engine.stop()

print("But the dish I looked forward was my Granny",p1,"'s famous",p18,"pic.")
line5='But the dish I looked forward was my Granny'+p1,'s famous'+p18,'pic.'
engine.say(line5)
engine.runAndWait()
engine.stop()


sound_file=vlc.MediaPlayer("C:\\Users\SATYA\Desktop\project\male\part31.mp3")
sound_file.play()
time.sleep(10)




