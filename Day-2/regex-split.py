import re

text = "apple,banana,orange,grape"
pattern = r","
split_result = re.split(pattern, text)
print("split words", split_result)