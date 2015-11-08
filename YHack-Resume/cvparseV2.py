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
    
    # need this to work in case no input
    if filename == " ":
        return ("", "")
    # is .pdf; need to convert to .txt
    elif filename.endswith(".pdf"):
        resume = pdftotextmaybe.convert(filename)
    else: 
        resume = readFile(filename).lower()
    # return resume as a string with different sections
    # good enough for the demo, lol
    return resume

def category(resume):
    # Return the category that appears the most
    (cat, score) = getCategory.mainCategoryAndScore(resume)
    return (cat, score)

def sectionScore(resume):
    section_tokens = tokenize.input_file_words(resume,[])
    employmentSection = false
    projectSection = false
    leaderSection = false
    currentIndex = -1
    wordCount = [0,0,0]
    for x.lower in section_tokens: 
        if(x.strip("!@#$%^&*()_+|}{:?") in ["work experience", "employment", "experience"] and currentIndex != 0):
            currentIndex = 0
        elif(x.strip("!@#$%^&*()_+|}{:?") in ["publications", "projects", "research"] and currentIndex != 1):
            currentIndex = 1
        elif(x.strip("!@#$%^&*()_+|}{:?") in ["leadership"] and currentIndex != 2):
            currentIndex = 2    
        elif(x.strip("!@#$%^&*()_+|}{:?") in ["education", ,"activites","skils", "interests", "extracurricular", "honors", "references", "awards", "acheivements"]):
            currentIndex = -1
        else:
            wordCount[currentIndex] += 1

    return  ((sum(wordCount) - min(wordCount))) / 350.0 * 10

def main(resume):
    # initialize variables 
    # have the words as tokens in a list
    tokens = tokenize.input_file_lines(resume,[])
    # current section of resume
    current_title = ""
    # number of words
    count = 0
    # "errors" will be taken out of possible score of 100
    # 100 is an impressive resume in contrast to 
    # 0, which would be a resume not suitable for the job or
    # not meeting requirements of the job
    errors = 0
    score = 100
    email = ""

    # word count
    for tok in tokens:
        if tok != "":
            count += 1
    # 475 words -> average amount of words on one page
    if count == 475: errors += 0
    # accounts for resumes too short and too long
    else:
        errors += min(abs(475-count)/20, 5)

    # GPA
    word_tokens = tokenize.input_file_words(resume,[])
    # print word_tokens
    gpaFound = False
    for token in word_tokens:
        if "gpa" in token.lower():
            index = word_tokens.index(token)
            if "/" in word_tokens[index + 1]:
                words = word_tokens[index + 1].split("/")
                gpa = float(words[0])
                if gpa == 4.00:
                    errors += 0
                elif gpa >= 3.00 and gpa < 4.00:
                    errors += 3
                elif gpa >= 2.00 and gpa < 3.00:
                    errors += 5
                else:
                    errors += 7
                gpaFound = True
                for word in words:
                    gpa = float(word)
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
                gpa = float(word_tokens[index + 1])
                if gpa == 4.00:
                    errors += 0
                elif gpa >= 3.00 and gpa < 4.00:
                    errors += 3
                elif gpa >= 2.00 and gpa < 3.00:
                    errors += 5
                else:
                    errors += 7
                gpaFound = True
    # a resume with a GPA might indicate a lower GPA
    if gpaFound == False: errors += 9

    # get email
    for token in word_tokens:
        if "@" in token:
            email = token
            break

    # level of degree
    desiredDegree = raw_input("Degree needed: ")
    word_tokens_lower = [x.lower() for x in word_tokens]
    # searches for similar words
    degree = difflib.get_close_matches(desiredDegree.lower(), word_tokens_lower)
    close_match_fail = False
    close_match = ""
    if degree == []:
        for word in word_tokens_lower:
            if (desiredDegree.lower() in word):
                close_match_fail = True
                close_match = word
                break
    stop_search = False
    while (not stop_search):
        if degree == [] and close_match_fail == False: 
            answer2 = raw_input("There are no matches. Search again? (Y/N) \n")
            if answer2 == "Y" or answer2 == "y" or answer2 == "yes" or answer2 == "Yes":
                desiredDegree = raw_input("Degree needed: ")
                degree = difflib.get_close_matches(desiredDegree.lower(), word_tokens_lower)
            else:
                stop_search = True
        else:
            if close_match_fail == True:
                print("Closest match to " + desiredDegree + " is " +
                close_match + ".")
                stop_search = True
            else:
                print("Closest match to " + desiredDegree + " is " +
                    degree[0] + ".")
                stop_search = True
    close_match_fail = False
    close_match = ""
    stop_search = False
    while (not stop_search):
        answer1 = raw_input("Would you like to search for another degree? (Y/N)\n")
        if answer1 == "Y" or answer1 == "y" or answer1 == "yes" or answer1 == "Yes":
            desiredDegree = raw_input("Degree needed: ")
            degree = difflib.get_close_matches(desiredDegree.lower(), word_tokens_lower)
            if degree == []:
                for word in word_tokens_lower:
                    if (desiredDegree.lower() in word):
                        close_match_fail = True
                        close_match = word
                        break
            if degree == [] and close_match_fail == False:
                answer3 = raw_input("There are no matches. Search again? (Y/N) \n")
                if answer3 == "Y" or answer3 == "y" or answer3 == "yes" or answer3 == "Yes":
                    desiredDegree = raw_input("Degree needed: ")
                    degree = difflib.get_close_matches(desiredDegree.lower(), word_tokens_lower)
                else:
                    stop_search = True
            else:  
                if close_match_fail == True:
                    print("Closest match to " + desiredDegree + " is " +
                        close_match + ".")
                else:
                    print("Closest match to " + desiredDegree + " is " +
                            degree[0] + ".")
        else:
            stop_search = True
    degreeFound = False
    answer4 = raw_input("Would you like to search the word 'degree'? (Y/N) \n")
    if answer4 == "Y" or answer4 == "y" or answer4 == "yes" or answer4 == "Yes":
        print("Searching 'degree' and returning adjacent words...") 
        for word in word_tokens_lower:
            if ("degree" in word):
                index = word_tokens_lower.index(word)
                if index - 1 >= 0 and index + 1 < len(word_tokens_lower):
                    prev_word = word_tokens_lower[index - 1]
                    after_word = word_tokens_lower[index + 1]
                    print("Word before 'degree': " + prev_word)
                    print("Word after 'degree': " + after_word)
                    degreeFound = True
                    break
                elif index - 1 >= 0 and index + 1 >= len(word_tokens_lower):
                    prev_word = word_tokens_lower[index - 1]
                    print("Word before 'degree': " + prev_word + "\n")
                    print("No word found after 'degree'.")
                    degreeFound = True
                    break
                elif index - 1 < 0 and index + 1 < len(word_tokens_lower):
                    after_word = word_tokens_lower[index + 1]
                    print("Word after 'degree': " + after_word + "\n")
                    print("No word found before 'degree'.")
                    degreeFound = True
                    break
                else:
                    # should not happen
                    print("The only word in the resume is 'degree'.")
                    degreeFound = True
                    break
        if degreeFound == False:
            print("The word 'degree' does not appear in the resume.")
    else:
        pass
    answer = raw_input("Is this what you are looking for? (Y/N)\n")
    # yes if desired degree found else degree not attained or present
    if answer == "yes": errors += 0
    else: errors += 10

    # word count under experience/projects/leadership

    print "finished parsing"
    score -= errors
        
    (cat, c_score) = category(resume)
    return (cat, score, email)

def readFile(filename, mode="rt"):
    # rt = "read text"
    with open(filename, mode) as fin:
        return fin.read()

resume = init()
if resume != "":
    print main(resume)
