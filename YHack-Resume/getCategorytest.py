from getCategory import *

# Tests

# software total phrase count -> 58
print(softwareScore("resume"))
assert(softwareScore("resume") == 0.0)
assert(softwareScore("This is a resume") == 0)
assert(softwareScore("c") == (1/58))
assert(softwareScore("c c++ c#") == (3/58))

# engineeringScore array length -> 27
assert(engineeringScore("resume") == 0)
assert(engineeringScore("This is a resume"))
assert(engineeringScore("chemical") == (1/27))
assert(engineeringScore("civil engineering build") == (3/27))

# financeScore array length -> 24
assert(financeScore("resume") == 0)
assert(financeScore("This is a resume"))
assert(financeScore("powerpoint") == (1/24))
assert(financeScore("forecasting trend analysis team") == (3/24))

# managementScore array length -> 25
assert(managementScore("resume") == 0)
assert(managementScore("This is a resume"))
assert(managementScore("powerpoint") == (1/25))
assert(managementScore("operational development firing budget") == (3/25))

# mainCategoryAndScore
assert(mainCategoryAndScore("resume") == ('computer science',0))
assert(mainCategoryAndScore("This is a resume") == ('computer science',0))
assert(mainCategoryAndScore("powerpoint") == ('management',(1/25)))
assert(mainCategoryAndScore("operational development c firing budget engineering") == ('finance',(3/25)))
assert(mainCategoryAndScore("sml c firing budget engineering") == ('computer science',(2/58)))
assert(mainCategoryAndScore("build sml hiring engineering") == ('engineering',(2/27)))


