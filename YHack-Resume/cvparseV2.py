## Nazli Uzgur

from __future__ import with_statement # for Python 2.5 and 2.6
import urllib
import os

class cvparse():
    def __init__(self):

        ########################################################
        ### Convert pdf to txt with pdf miner 
        ########################################################


        # the whole resume is in this file (and in lowercase)
        self.resume = readFile("resume.txt").lower()

        # The resumes are nearly always in a template form:
        # They have titles, such as:
        #   Experience, Education, Skills, Interests, Extracurricular
        # I'm going to put these in a list so I can check as I go
        #   through the resume to estimate how long each section is.
        titles = ["Experience", "Education", "Skills",
            "Interests", "Extracurricular"]

        # Create a dictionary for words that show which category this 
        #   resume is in
        category = {'programming':0, 'business':0}
        # good enough for the demo, lol

    def score(resume_d):
        # scoring according to the dict


    def main():
        # initialize variables
        count = 0 # the count 
        resume_d = dict() # dictionary to have the titles and how many
                          #  words there are under that title
        tokens = input_file(resume,[]) # have the words as tokens in a list


        # Go through the tokens:
        for token in tokens:
            if(token in )





def readFile(filename, mode="rt"):
    # rt = "read text"
    with open(filename, mode) as fin:
        return fin.read()

cvparse.main();
