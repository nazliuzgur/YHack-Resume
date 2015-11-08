import pdftotextmaybe

def programmingScore(resume):
    programming = ["assembly", "bash", " c " "c++", "c#", "coffeescript", "emacs lisp",
     "go!", "groovy", "haskell", "java", "javascript", "matlab", "max MSP", "objective c", 
     "perl", "php","html", "xml", "css", "processing", "python", "ruby", "sml", "swift", 
     "latex" "unity", "unix" "visual basic" "wolfram language", "xquery", "sql", "node.js", 
     "scala", "kdb", "jquery", "mongodb"]

    programmingTotal = 0

    for i in range(len(programming)):
        if programming[i].lower() in resume.lower() != -1:
            programmingScore += 1

    programmingScore = min(programmingTotal/8.0, 1) * 5.0

def softwareScore(resume):
    csKeyWords = ["computer", "software", "engineering", "computer science", "prototype", "structured design",
    "code development", "communication skills", "problem solving", "software design", "systems", "web", "client",
    "testing", "SDLC", "development process", "database management systems", "web applications", "code"
    "user support", "programming", "developing", "software", "server administration", "machine learning",
    "alogorithms", "team", "programming language"]

    print(len(csKeyWords))
    csWordScore = []
    for i in range(len(csKeyWords)):
        csWordScore.append(0)
        if csKeyWords[i].lower() in (resume.lower()) != -1:
            (csWordScore[i]) += 1

    csScore = min((float)(sum(csWordScore)+8) / (len(csKeyWords)),1.0) * 25.0

    return csScore

def engineeringScore(resume):
    engineeringKeyWords = ["chemical", "civil", "engineering", "mechanical", "CAD", "design",
    "mechanics", "analysis", "systems", "technical", "autodesk", "inventor", "skills", "realization",
    "technology", "functionality", "hardware", "design process", "process control", "protyping", "team",
    "project conceptualization", "design verification", "project management", "structural design", 
    "build", "modeling", "buildings", "tests", "application"]
    
    print(len(engineeringKeyWords))

    engWordScore = []
    for i in range(len(engineeringKeyWords)):
        engWordScore.append(0)
        if engineeringKeyWords[i].lower() in (resume.lower()) != -1:
            (engWordScore[i]) += 1

    engScore = min((float)(sum(engWordScore)+8) / len(engineeringKeyWords),1.0) * 25.0

    return engScore

def financeScore(resume):
    financeKeyWords = ["financial reporting", "excel", "finance", "trend analysis",
     "financial statement", "result analysis", "strategic planning", "develop trends",
    "DCF", "presentation skills", "team player", "financial analysis", "forecasting",
    "policy development", "business policies", "powerpoint", "microsoft word", "analytical",
    "accounting", "team player", "team", "ability", "accounting", "accountant", "balance sheet",
    "liquidy", "money", "stocks"]

    print(len(financeKeyWords))

    finWordScore = []
    for i in range(len(financeKeyWords)):
        finWordScore.append(0)
        if financeKeyWords[i].lower() in (resume.lower()) != -1:
            (finWordScore[i]) += 1

    finScore = min((float)(sum(finWordScore)+8) / len(financeKeyWords), 1.0) * 25.0
    return finScore

def managementScore(resume):
    managementKeyWords = ["data analysis", "automation", "planning", "ability to plan",
    "customer", "interaction", "consumer", "implement", "analytical", "network",
    "skill analysis", "hiring", "firing", "business development", "contract negotiation",
    "budget", "leadership", "operational development", "evaluations", "management",
    "business", "project planning", "production schedule", "responsibility", "budgeting",
    "optimization", "decision making", "organization", "business"]

    print(len(managementKeyWords))

    manWordScore = []
    for i in range(len(managementKeyWords)):
        manWordScore.append(0)
        if managementKeyWords[i].lower() in (resume.lower()) != -1:
            (manWordScore[i]) += 1

    manScore = min((float)(sum(manWordScore)+8) / len(managementKeyWords),1.0) * 25.0

    return manScore

def artsScore(resume):
    artsKeyWords = ["performance", "exhibit", "music", "art", "writing", "expressive",
    "editing", "editorial", "social work", "design", "artist", "musician", "collaborative",
    "group", "program", "exhibition", "media", "blog", "journalism", "creative", "innovative",
    "workshop", "master class", "teaching", "lectures", "practice", "studio", "newspaper",
    "english"]

    print(len(artsKeyWords))

    artsWordScore = []
    for i in range(len(artsKeyWords)):
        artsWordScore.append(0)
        if artsKeyWords[i].lower() in (resume.lower()) != -1:
            (artsWordScore[i]) += 1

    artsScore = min((float)(sum(artsWordScore)+8) / len(artsKeyWords), 1.0) * 25.0

    return artsScore

def mainCategoryAndScore(resume):
    cs = softwareScore(resume)
    eng = engineeringScore(resume)
    fin = financeScore(resume)
    man = managementScore(resume)
    art = artsScore(resume)

    a = ["computer science", "engineering", "finance", "business management", "arts"]
    b = [cs, eng, fin, man, art]
    
    maxScore = b[0]
    maxIndex = 0

    for x in range(len(b)):
        if (b[x]) > maxScore:
            maxIndex = x
            maxScore = b[x]

    c = zip(a,b)

    return c[maxIndex]

def printAllCategoryScores(resume):
    cs = softwareScore(resume)
    eng = engineeringScore(resume)
    fin = financeScore(resume)
    man = managementScore(resume)
    art = artsScore(resume)

    a = ["computer science", "engineering", "finance", "business management", "arts"]
    b = [cs, eng, fin, man, art]

    c = zip(a,b)

    print(c)

    return

print(pdftotextmaybe.convert("sample.pdf"))

printAllCategoryScores(pdftotextmaybe.convert("sample.pdf"))
