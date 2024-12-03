file = open("input", "r")
left = []
right = []
result = []
input = file.read()
lines = input.split("\n")
for line in lines:
    if len(line) > 5:
        left.append(int(line[0:5]))
        right.append(int(line[-5:]))

right.sort()
left.sort()

for num in left:
    result.append(right.count(num) * num)

print(sum(result))