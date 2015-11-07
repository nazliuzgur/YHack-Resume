def softwareScore(resume) :
    programming = ["assembly", "bash", "c", "c++", "c#", "coffeescript", "emacs lisp",
    "go", "go!", "groovy", "haskell", "java", "javascript", "machine code", "matlab", 
    "max", "objective c", "perl", "php","html", "xml", "css", "processing", "python", 
    "ruby", "sml", "swift", "latex" "unity", "unix shell" "visual basic" "wolfram language", 
    "xquery", "r", "julia", "sql", "clojure", "html5", "node.js", "scala", "kdb", "jquery"]

    csKeyWords = ["computer", "engineering", "computer science", "prototype", "structured design",
    "code development", "communication skills", "problem solving", "software design",
    "testing", "SDLC", "development process", "database management systems", "web applications",
    "user support", "programming", "developing", "software", "server administration"]

    programmingScore = []
    for i in range(len(programming)):
        programmingScore.append(0)
        if programming[i].lower().find(resume.lower()) != -1:
            (programmingScore[i]) += 1

    csWordScore = []
    for i in range(len(csKeyWords)):
        csWordScore.append(0)
        if csKeyWords[i].lower().find(resume.lower()) != -1:
            (csWordScore[i]) += 1

    csScore = (float)(sum(programmingScore) + sum(csWordScore)) / (len(programming) + len(csKeyWords))

    return csScore

def engineeringScore(resume):
    engineeringKeyWords = ["chemical", "civil", "engineering", "mechanical", "CAD", "design",
    "mechanics", "analysis", "systems", "technical", "autodesk", "inventor", "skills", "realization",
    "technology", "distribution systems", "design process", "process control", "protyping", "team",
    "technical specification", "project", "project conceptualization", "design verification",
    "project management", "structural design", "build"]

    engWordScore = []
    for i in range(len(engineeringKeyWords)):
        engWordScore.append(0)
        if engineeringKeyWords[i].lower().find(resume.lower()) != -1:
            (engWordScore[i]) += 1

    eingScore = (float)(sum(engWordScore) / len(engineeringKeyWords))

    return engScore

def financeScore(resume):
    financeKeyWords = ["financial reporting", "excel", "financial", "trend analysis",
     "financial statement", "result analysis", "strategic planning", "develop trends",
    "DCF", "presentation skills", "team player", "financial analysis", "forecasting",
    "policy development", "business policies", "powerpoint", "microsoft word", "analytical",
    "accounting", "team player", "team", "ability", "accounting", "accountant"]

    finWordScore = []
    for i in range(len(financeKeyWords)):
        finWordScore.append(0)
        if financeKeyWords[i].lower().find(resume.lower()) != -1:
            (finWordScore[i]) += 1

    finScore = (float)(sum(finWordScore) / len(financeKeyWords))

    return finScore

def managementScore(resume):
    managementKeyWords = ["data analysis", "automation", "planning", "ability to plan",
    "customer", "interaction", "consumer", "implement", "analytical", "network",
    "skill analysis", "hiring", "firing", "business development", "contract negotiation",
    "budget", "leadership", "operational development", "evaluations", "management",
    "business", "project planning", "data analysis", "production schedule", "network"]

    manWordScore = []
    for i in range(len(managementKeyWords)):
        manWordScore.append(0)
        if managementKeyWords[i].lower().find(resume.lower()) != -1:
            (manWordScore[i]) += 1

    manScore = (float)(sum(manWordScore) / len(managementKeyWords))

    return manScore

def mainCategoryAndScore(resume):
    cs = softwareScore(resume)
    eng = engineeringScore(resume)
    fin = financeScore(resume)
    man = managementScore(resume)

    a = ["computer science", "engineering", "finance", "business management"]
    b = [cs, eng, fin, man]
    
    maxScore = b[0]
    maxIndex = 0

    for x in b:
        if b[x] > maxScore:
            maxIndex = x
            maxScore = b[x]

    c = zip(a,b)

    return c[maxIndex]
