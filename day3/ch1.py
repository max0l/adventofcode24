import re

f = open("input", "r")
contents = f.read()

results = re.findall(r"mul\([0-9]+,[0-9]+\)", contents)

sum = 0

for result in results:
    numbers = result.split(",")
    sum += int(re.sub(r"\D", "", numbers[0])) * int(re.sub(r"\D", "", numbers[1]))

print(sum)