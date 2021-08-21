import re

s = "A-"

regexy = re.search("\AA", s, re.DEBUG)
if regexy:
    print("Trü")
else:
    print("not Trü")

print(regexy.group())