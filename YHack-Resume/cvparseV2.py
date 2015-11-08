## Nazli Uzgur

from __future__ import with_statement # for Python 2.5 and 2.6
import urllib
# import PyPDF2
import re, collections
import os
import tokenize
import pdftotextmaybe
import getCategory
import difflib

def init():

    ########################################################
    ### Convert pdf to txt with pdf miner 
    ########################################################

    # input the file name
    filename = raw_input("File name: ")
    if filename == " ":
        return ("", "")
    elif filename.endswith(".pdf"):
        resume = pdftotextmaybe.convert(filename)
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

    # good enough for the demo, lol
    return (resume, titles)

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

def category(resume):
    # Return the category that appears the most
    (cat, score) = getCategory.mainCategoryAndScore(resume)
    return (cat, score)

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

def main(resume, titles):
    # initialize variables 
    tokens = tokenize.input_file_lines(resume,[]) # have the words as tokens in a list
    current_title = ""
    count = 0 # the count
    errors = 0
    score = 100
    email = ""

    # word count
    for tok in tokens:
        if tok != "":
            count += 1
    if count == 475: errors += 0
    else:
        errors += min(abs(475-count)/20, 5)

    # GPA
    word_tokens = tokenize.input_file_words(resume,[])
    print word_tokens
    gpaFound = False
    for token in word_tokens:
        if "gpa" in token.lower():
            index = word_tokens.index(token)
            if "/" in word_tokens[index + 1]:
                words = word_tokens[index + 1].split("/")
                for word in words:
                    gpa = int(word)
                    if gpa == 4.00:
                        errors += 0
                    elif gpa >= 3.00 and gpa < 4.00:
                        errors += 3
                    elif gpa >= 2.00 and gpa < 3.00:
                        errors += 5
                    else:
                        errors += 7
                    gpaFound = True
            else:
                gpa = int(word_tokens[index + 1])
                if gpa == 4.00:
                    errors += 0
                elif gpa >= 3.00 and gpa < 4.00:
                    errors += 3
                elif gpa >= 2.00 and gpa < 3.00:
                    errors += 5
                else:
                    errors += 7
                gpaFound = True
    if gpaFound == False: errors += 9

    # get email
    for token in word_tokens:
        if "@" in token:
            email = token
            break

    # level of degree
    desiredDegree = raw_input("Degree needed: ")
    degree = difflib.get_close_matches(desiredDegree, word_tokens)
    print("Closest match to " + desiredDegree + " is " +
            degree + ".")
    quit = False
    while (!quit):
        answer1 = raw_input("Would you like to search for another degree? (Y/N)")
        if answer1 == "Y" or answer1 == "y" or answer == "yes" or answer == "Yes":
            desiredDegree = raw_input("Degree needed: ")
            degree = difflib.get_close_matches(desiredDegree, word_tokens)
            print("Closest match to " + desiredDegree + " is " +
                    degree + ".")
        else answer1 = "N" or answer1 == "n" or answer1 == "no" or answer1 == "No":
            quit = True
    answer = raw_input("Is this what you are looking for? (Y/N)")
    if answer == "yes": errors += 0
    else: errors += 10

    # word count under experience/projects/leadership


    # find spelling errors
    # for token in tokens:
    #     if len(token.split()) == 1:
    #         if token[0:len(token) - 1] in titles or token in titles:
    #             continue
    #         else:
    #             if (correct(token) != token):
    #                 errors += 1
    #     else: 
    #         token_parse = token.split()
    #         for tok in token_parse:
    #             if (correct(tok) != tok):
    #                 if ("'" in tok or "," in tok):
    #                     continue
    #                 else:
    #                     errors += 1
        # if token == "gpa":
        #     index = tokens.index(token)
        #     gpa = int(tokens[index + 1])
        #     if gpa == 4.00:
        #         if score == 100: score += 0
        #         else: score += 10
        #     elif gpa >= 3.00 and gpa < 4.00: 
        #         if score == 100: score += 0
        #         else: score += 5
        #     elif gpa >= 2.00 and gpa < 3.00:
        #         if score < 5: score -= 0
        #         else: score -= 5
        #     else:
        #         if score < 10: score -= 0
        #         else: score -= 10
    print "finished parsing"
    if errors % 10 == 0: score -= (errors + 1) % 10
    else: score -= errors % 10 
        
    (cat, c_score) = category(resume)
    return (cat, score)

def readFile(filename, mode="rt"):
    # rt = "read text"
    with open(filename, mode) as fin:
        return fin.read()

(resume, titles) = init()
NWORDS = train(words(file("dictionary.txt").read()))
alphabet = "abcdefghijklmnopqrstuvwxyz"
if (resume, titles) != ("", ""):
    print main(resume, titles)