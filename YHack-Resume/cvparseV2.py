## Nazli Uzgur

from __future__ import with_statement # for Python 2.5 and 2.6
import urllib
# import PyPDF2
import re, collections
import os
import tokenize

def init():

    ########################################################
    ### Convert pdf to txt with pdf miner 
    ########################################################

    # input the file name
    filename = raw_input("File name: ")
    if filename == " ":
        return ("", "", "")
    # elif filename.endswith(".pdf"):
    #     content = getPDFContent(filename).encode("ascii", "ignore")
    #     resume = content
    else: 
        resume = readFile(filename).lower()

    # the whole resume is in this file (and in lowercase)
    # self.resume = readFile("resume.txt").lower()

    # The resumes are nearly always in a template form:
    # They have titles, such as:
    #   Experience, Education, Skills, Interests, Extracurricular
    # I'm going to put these in a list so I can check as I go
    #   through the resume to estimate how long each section is.
    titles = ["resume","experience", "education", "skills",
        "interests", "extracurricular", "projects", "leadership"]

    # Create a dictionary for words that show which category this 
    #   resume is in
    category = {'computer science':0, 'business':0, "engineering":0, "health sciences":0, "physical sciences":0,
                "fine arts":0, "humanities":0}
    # good enough for the demo, lol
    return (resume, titles, category)

# def getPDFContent(filename):
#     content = ""
#     # Load PDF into pyPDF
#     pdf = PyPDF2.PdfFileReader(file(filename, "rb"))
#     # Iterate pages
#     for i in xrange(0, pdf.getNumPages()):
#         # Extract text from page and add to content
#         content += pdf.getPage(i).extractText()
#     # Collapse whitespace
#     content = " ".join(content.replace(u"\xa0", " ").strip().split())
#     return content

def category():
    # Return the category that appears the most
    return 42

def words(text): return re.findall("[a-z]+", text.lower())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

def edits1(word):
    splits = [(word[:i], word[i:]) for i in xrange(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words):
    return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

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
    errors = 0
    score = 0

    for token in tokens:
        if len(token.split()) == 1:
            token = token[0:len(token) - 1]
            if token in titles:
                current_title = token
    print tokens

    for token in tokens:
        if len(token.split()) == 1:
            if token[0:len(token) - 1] in titles:
                continue
            else:
                if (correct(token) != token):
                    print token
                    errors += 1
        else: 
            token_parse = token.split()
            for tok in token_parse:
                if (correct(tok) != tok):
                    if ("'" in tok):
                        continue
                    else:
                        print tok
                        errors += 1
    score += errors % 10


    # Go through the tokens until first title:
    # for token in tokens:
    #     if(token in category):
    #         category[token] += 1
    #     if(token in titles):
    #         current_title = token

    # Now we have the first title and can go through the tokens:
    # I know this is not efficient but it should work
    # for token in tokens:
    #     print token
    #     if(token in category):
    #         category[token] += 1
    #     if(token in titles):
    #         # Add what you have until now to dictionary
    #         resume_d[current_title] = count

    #         # Now, change the title and initialize the count
    #         current_title = token
    #         count = 0
    #     count+=1 
        # one more word has been counted

    # Now we have the dict resume_d with the titles and how many
    #   words there are in that section

    # We also have a dict of categories and should return the
    #   category that appears the most
    # x = category()

    # Send this to scoring and return score
    # y = scoring(resume_d)
# 


def readFile(filename, mode="rt"):
    # rt = "read text"
    with open(filename, mode) as fin:
        return fin.read()

(resume, titles, category) = init()
NWORDS = train(words(file("dictionary.txt").read()))
alphabet = "abcdefghijklmnopqrstuvwxyz"
if (resume, titles, category) != ("", "", ""):
    main(resume, titles, category)
