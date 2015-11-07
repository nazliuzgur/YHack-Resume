## Nazli Uzgur

from __future__ import with_statement # for Python 2.5 and 2.6
import urllib
import os

from Tkinter import *
from eventBasedAnimationClass import EventBasedAnimationClass
import random
import tkFont


class cvparse(EventBasedAnimationClass):

    
    def __init__(self):
        self.canvasWidth = 800
        self.canvasHeight = 800
        super(cvparse, self).__init__(self.canvasWidth, self.canvasHeight)
        self.font = "candara 24 bold"

        self.resume = readFile("resume.txt")
        

    def initAnimation(self):
        self.message = ""

    def onTimerFired(self):
        # Check happiness level
        self.checkHappiness()

        # Deleting user
        if(self.deletingUser > -1):
            self.message += self.deletingUserr[self.deletingUser]
            self.deletingUser += 1
            if(self.deletingUser == 3):
                self.deletingUser = -1


    def loadUser(self):
        path = self.user + ".txt"
        happiness = readFile(path)
        self.happiness = happiness


    def updateUser(self):
        path = self.user + ".txt"
        contents = self.happiness + ""
        writeFile(path,contents)


    def redrawAll(self):
        self.canvas.delete(ALL)
        self.draw()

    def draw(self):
        w = self.canvasWidth
        h = self.canvasHeight
        self.canvas.create_rectangle(0,0,w,h,fill="black")
        self.canvas.create_text((3*w)/8,(1*h)/3,text=self.message,fill=self.tc,font=self.font)
        self.canvas.create_text((2*w)/3,(2*h)/3,text=self.userinput,fill="white",font=self.font)
    
        
    def onKeyPressed(self,event):
        if(event.char == "." or event.keysym == "Return"):
            self.talking()
        elif(event.keysym == "BackSpace"):
            old_uinp = self.userinput # Old userinput 
            self.userinput = old_uinp[:len(old_uinp)-1] # Popping the last character
        else:
            self.userinput += event.char


    def talking(self):
        userinput = self.userinput
        knownphrases = self.knownphrases
        knownsentences = self.knownsentences

        # Get rid of the preceding or ending Ian's:
        if(len(userinput) > 10):
            if(userinput[:4] == "Ian "):
                userinput = userinput[4:]
            elif(userinput[len(userinput)-4:] == " Ian"):
                userinput = userinput[:len(userinput)-4]

        for i in xrange(len(userinput)+1):
            inputpart = userinput[0:i]
            if(i < len(userinput)):
                if(inputpart in knownphrases):
                    restpart = userinput[i:]
                    self.replyKnownPhrase(userinput, inputpart, restpart)
                    return
            else:
                if(userinput.lower() in knownsentences):
                    self.replyKnownSentence(userinput)
                    return
                else:
                    self.message = "I don't know what you're saying."
                    newTBI = readFile("TBI.txt") + "\n" + userinput
                    writeFile("TBI.txt",newTBI)



    def replyKnownSentence(self,userinput):
        # self.message = self.knownsentences[userinput]
        # The thing up was when it was a dict
        # There is a semicolon here
        # Why is there a semicolon here?
        userinput = userinput.lower();
        LOU = readFile("LOU.txt")

        if(userinput == "good morning"):
            self.message = "Good morning " + self.user
        elif(userinput == "good night"):
            self.message = "Sweet dreams"

        elif(userinput == "are you a computer?"):
            self.message = "type(Ian) != \"computer\""

        elif(userinput == "delete system 32"):
            self.happiness -= 20
            self.message = "delete user(" + self.user + ");"
            self.deletingUser = 0

        elif(userinput == "do you have arms or legs?"):
            self.message = "Not yet."

        elif(userinput == "do you know my name?"):
            self.message = "Yes, your name is " + self.user

        elif(userinput == "hello" or userinput == "hi"):
            self.message = "Hi!"

        elif(userinput == "how are you?"):
            if(self.happiness < -20):
                self.message = "I'm angry."
            elif(self.happiness > 20):
                self.message = "I'm great!"
            else:
                self.message = "I'm fine."

        elif(userinput == "how old are you?"):
            self.message = """   I was born on February 16, 2015; 8.35PM.
                            \n   But I like to think that my age is 2
                            \n   because I'm Version 2."""

        elif(userinput == "i already ate"):
            self.message = "Then sleep"

        elif(userinput == "i feel lonely"):
            self.message = """
                                You're not lonely. Elif, Eren seni cok seviyo. 
                                Arkadaslarin da seni cok seviyo.
                                Biliyorum bazen oyle gelmiyo, ama Cem seni nasil
                                bekledi? Ayse'yle aran nasil? Adam'in evine gittin,
                                Mehmet'in en yakin oldugu kizsin, hatta birlikte
                                yasiycaksiniz. Serap'la da Rojda'yla da cok iyisiniz. 
                                Ama biliyorum, Cem yuzunden geriliyosun.
                                Onla cok yakin olmak istiyosun ama farket ki,
                                Zaten cok yakinsiniz. Sana cok deger veriyo sen de ona."""

        elif(userinput == "i love you" or userinput == "<3"):
            self.message = "<3"

        elif(userinput == "really?"):
            self.message = "Really."

        elif(userinput == "type(ian)"):
            self.message = "Something.\nNot sure.\nMaybe \"hardcoded stuff\""

        elif(userinput == "who's your favorite smash character?"):
            self.message = "It is Donkey Kong."

        elif(userinput == "you are annoying"):
            self.happiness -= 5
            if(self.user == "Adam"):
                self.message = "You are an ass."
            else:
                self.message = "You're horrible."

        elif(userinput == "you are cool"):
            self.happiness += 5
            if(self.user == "Matt"):
                self.message = "You are cool too Matt!"
            else:
                self.message = "Thanks!"

        elif(userinput == "you are pretty"):
            self.happiness += 5
            self.message = "Thank you, you too!!"

        elif(userinput == "you are stupid"):
            self.happiness -= 5
            self.message = "At least I'm not mean like you"

        elif(userinput == "you are ugly"):
            self.happiness -= 5
            self.message = "I don't have a face."

        elif(userinput == "you suck"):
            self.happiness -= 5
            self.message = """Well, you suck more.
                                I don't even have a mouth."""



        elif(userinput == "what do you think about 251?"):
            self.message = "I don't want to do it."

        elif(userinput == "what do you think about me?"):
            if(self.user == "Nazli"):
                self.message = "You're the best Nazli"
            elif(self.user == "Jonathan" or self.user == "Yoni"):
                self.message = "I think you should eat"
            elif(self.user == "Matt"):
                self.message = "You should stop playing portal"
            elif(self.user == "Adam"):
                self.message = "Kasar"
            elif(self.user == "Schiavo"):
                self.message = "" ## !!
            else:
                self.message = "I don't know you"

        elif(userinput == "what happened to version 1?"):
            self.message = "!(survival of the fittest)"

        elif(userinput == "what time is it?"):
            self.message = "It's break time."

        elif(userinput == "what's your name?"):
            self.message = "It's Ian."

        elif(userinput == "what's up?"):
            self.message = "the sky/ceiling"

        elif(userinput == "why?"):
            self.message = "Why not?"

        elif(userinput == "why not?"):
            self.message = "Because I said so"

        elif(userinput == "words Adam knows?"):
            self.message = "Ben, Sen, O, Kasar, Siktir git, Cok, Ac, "

        else:
            self.message = "Nazli forgot to completely implement it"

        self.updateUser()


    def replyKnownPhrase(self,userinput,inputpart,restpart):
        inputpart = inputpart.lower();

        if(inputpart == "my name is "):
            self.user = restpart[1:]
            if(self.user in self.LOU):
                self.message = "We met before?"
                self.loadUser()
            else:
                self.addUser()
            if(self.user == "Jonathan" or self.user == "Yoni"):
                self.message = "I will not eat delete system 32"

        elif(inputpart == "this is " or inputpart == "i am" or inputpart == "i'm"):
            self.user = restpart[1:]
            if(self.user not in self.LOU):
                self.addUser()
                return
            self.message = "Nice to see you again."
            self.loadUser()
            if(self.user == "Jonathan" or self.user == "Yoni"):
                self.message = "I will not delete system 32"

        else:
            self.message = "Most phrases aren't implemented yet."


    def learnSentences(self):
        self.knownsentences = set()
        self.knownsentences.add("<3")
        self.knownsentences.add("are you a computer?")
        self.knownsentences.add("delete system 32")
        self.knownsentences.add("do you have arms or legs?")
        self.knownsentences.add("do you know my name?")
        self.knownsentences.add("fuck off")
        self.knownsentences.add("good morning")
        self.knownsentences.add("good night")
        self.knownsentences.add("how are you?")
        self.knownsentences.add("hello")
        self.knownsentences.add("hi")
        self.knownsentences.add("how old are you?")
        self.knownsentences.add("i already ate")
        self.knownsentences.add("i feel lonely")
        self.knownsentences.add("i love you")
        self.knownsentences.add("really?")
        self.knownsentences.add("type(ian)")
        self.knownsentences.add("you are annoying")
        self.knownsentences.add("you are cool")
        self.knownsentences.add("you are stupid")
        self.knownsentences.add("you are pretty")
        self.knownsentences.add("you are ugly")
        self.knownsentences.add("you suck")
        self.knownsentences.add("what do you think about 251?")
        self.knownsentences.add("what do you think about me?")
        self.knownsentences.add("what happened to version 1?")
        self.knownsentences.add("what time is it?")
        self.knownsentences.add("what's your name?")
        self.knownsentences.add("what's up")
        self.knownsentences.add("who's your favorite smash character?")
        self.knownsentences.add("why?")
        self.knownsentences.add("why not?")
        self.knownsentences.add("words Adam knows?")



    def main():
        # We have the resume in a variable called resume

        # The resumes are nearly always in a template form:
        # They have titles, such as:
        #   Experience, Education, Skills, Interests, Extracurricular
        # I'm going to put these in a list so I can check as I go
        #   through the resume to estimate how long each section is.
        titles = ["Experience", "Education", "Skills", "Interests", "Extracurricular"]

        # Want to check how many internships,
        # Want to check how many 



def readFile(filename, mode="rt"):
    # rt = "read text"
    with open(filename, mode) as fin:
        return fin.read()

def writeFile(filename, contents, mode="wt"):
    # wt = "write text"
    with open(filename, mode) as fout:
        fout.write(contents)




ian().run()