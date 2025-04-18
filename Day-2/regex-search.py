import re

text = "Ravi is quick learner"

pattern = r"quick"
search = re.search(pattern,text)

if search:
    print("pattern found:", search.group())
else:
    print("No Match found")
