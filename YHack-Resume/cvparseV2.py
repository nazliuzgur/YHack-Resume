## Nazli Uzgur

from __future__ import with_statement # for Python 2.5 and 2.6
import urllib
import os
import tokenize

def __init__():

    ########################################################
    ### Convert pdf to txt with pdf miner 
    ########################################################

    # input the file name
    filename = input("File name: ")
    if filename == " ":
        return ("", "", "")
    resume = readFile(filename).lower()

    # the whole resume is in this file (and in lowercase)
    # self.resume = readFile("resume.txt").lower()

    # The resumes are nearly always in a template form:
    # They have titles, such as:
    #   Experience, Education, Skills, Interests, Extracurricular
    # I'm going to put these in a list so I can check as I go
    #   through the resume to estimate how long each section is.
    titles = ["Experience", "Education", "Skills",
        "Interests", "Extracurricular", "Projects", "Leadership"]

    # Create a dictionary for words that show which category this 
    #   resume is in
    category = {'computer science':0, 'business':0, "engineering":0, "health sciences":0, "physical sciences":0,
                "fine arts":0, "humanities":0}
    # good enough for the demo, lol
    return (resume, titles, category)

def category():
    # Return the category that appears the most
    return 42

def score(resume_d):
    # score according to the dict
    return 42

def main(resume, titles, category):
    # initialize variables 
    resume_d = dict() # dictionary to have the titles and how many
                      #  words there are under that title
    tokens = tokenize.input_file(resume,[]) # have the words as tokens in a list
    current_title = ""
    count = 0 # the count

    # Go through the tokens until first title:
    for token in tokens:
        if(token in category):
            category[token] += 1
        if(token in titles):
            current_title = token

    # Now we have the first title and can go through the tokens:
    # I know this is not efficient but it should work
    for token in tokens:
        if(token in category):
            category[token] += 1
        if(token in titles):
            # Add what you have until now to dictionary
            resume_d[current_title] = count

            # Now, change the title and initialize the count
            current_title = token
            count = 0
        count+=1 
        # one more word has been counted

    # Now we have the dict resume_d with the titles and how many
    #   words there are in that section

    # We also have a dict of categories and should return the
    #   category that appears the most
    x = category()

    # Send this to scoring and return score
    y = scoring(resume_d)

    return

            



def readFile(filename, mode="rt"):
    # rt = "read text"
    with open(filename, mode) as fin:
        return fin.read()

(resume, titles, category) = __init__()
if (resume, titles, category) != ("", "", ""):
    main(resume, titles, category)
