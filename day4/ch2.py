def checkxmas(line, letter):
    if array[line+1][letter+1] == "S" and array[line+1][letter-1] == "M" and array[line-1][letter-1] == "M" and array[line-1][letter+1] == "S"\
        or array[line+1][letter+1] == "M" and array[line+1][letter-1] == "M" and array[line-1][letter-1] == "S" and array[line-1][letter+1] == "S"\
        or array[line+1][letter+1] == "S" and array[line+1][letter-1] == "S" and array[line-1][letter-1] == "M" and array[line-1][letter+1] == "M"\
        or array[line+1][letter+1] == "M" and array[line+1][letter-1] == "S" and array[line-1][letter-1] == "S" and array[line-1][letter+1] == "M":
        global counter
        counter += 1

f = open("input", "r")
contents = f.read().split("\n")


array = []
counter = 0

for lines in contents:
    array.append(list(lines))

for line in range(len(array)-3):
    for letter in range(len(array[line])-2):
        if array[line+1][letter+1] == "A":
            checkxmas(line+1,letter+1)

print(counter)
