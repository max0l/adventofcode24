import re

f = open("input", "r")
contents = f.read()

results = re.findall(r"do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\)", contents)

sum = 0
enabled = True

for result in results:
    if result == "do()":
        enabled = True
        continue
    if result == "don't()":
        enabled = False
        continue
    if enabled:
        numbers = result.split(",")
        sum += int(re.sub(r"\D", "", numbers[0])) * int(re.sub(r"\D", "", numbers[1]))

print(sum)