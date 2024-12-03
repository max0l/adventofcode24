file = open("challenge1/input", "r")
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

for x in range(len(right)):
    if right[x] >= left[x]:
        result.append(right[x]-left[x])
    else:
        result.append(left[x]-right[x])


print(sum(result))
