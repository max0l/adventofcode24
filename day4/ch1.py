def searchhorizontal(x,y):
    if (y + len(word)) > len(array[x]):
        return False
    for j in range(len(word)):
        if array[x][y+j] != splitted_word[j]:
            return False
    #print("Horizontal")
    global counter
    counter += 1

def searchhorizontalref(x,y):
    if (y - len(word)+1) < 0:
        return False
    for j in range(len(word)):
        if array[x][y-j] != splitted_word[j]:
            return False
    #print("horizontal rev")
    global counter
    counter += 1

def searchverticaldown(x,y):
    if (x + len(word)) >= len(array):
        return False
    for j in range(len(word)):
        if array[x+j][y] != splitted_word[j]:
            return False
    #print("Vertical down")
    global counter
    counter += 1

def searchverticalup(x,y):
    if (x - len(word)+1) < 0:
        return False
    for j in range(len(word)):
        if array[x-j][y] != splitted_word[j]:
            return False
    #print("Vertical up")
    global counter
    counter += 1

def searchdiagonaldownright(x,y):
    #print(f"{y} + {len(word)} > {len(array[x])} or {x} + {len(word)} >= {len(array)}")
    if (y + len(word)) > len(array[x]) or (x + len(word)) >= len(array):
        return False
    for j in range(len(word)):
        if array[x+j][y+j] != splitted_word[j]:
            return False
    #print("Diagonal down right")
    global counter
    counter += 1

def searchdiagonaldownleft(x,y):
    #print(f"{y} - {len(word) + 1} < 0 or {x} + {len(word)} >= {len(array)}")
    if (y - len(word)+1) < 0 or (x + len(word)) >= len(array):
        return False
    for j in range(len(word)):
        if array[x+j][y-j] != splitted_word[j]:
            return False
    #print("Diagonal down left")
    global counter
    counter += 1

def searchdiagonalupleft(x,y):
    #print(f"{y} - {len(word) + 1} < 0 or {x} - {len(word)} < 0")
    if (y - len(word)+1) < 0 or (x - len(word)+1) < 0:
        return False
    for j in range(len(word)):
        if array[x-j][y-j] != splitted_word[j]:
            return False
    #print("Diagonal up left")
    global counter
    counter += 1

def searchdiagonalupright(x,y):
    #print(f"{y} + {len(word)} > {len(array[x])} or {x} - {len(word)} < 0")
    if (y + len(word)) > len(array[x]) or (x - len(word)+1) < 0:
        return False
    for j in range(len(word)):
        if array[x-j][y+j] != splitted_word[j]:
            return False
    #print("Diagonal up right")
    global counter
    counter += 1

f = open("input", "r")
contents = f.read().split("\n")


array = []
counter = 0
word = "XMAS"
splitted_word = list(word)

for lines in contents:
    array.append(list(lines))

for line in range(len(array)-1):
    for letter in range(len(array[line])):
        if array[line][letter] == "X":
            searchhorizontal(line,letter)
            searchhorizontalref(line,letter)
            searchverticaldown(line, letter)
            searchverticalup(line, letter)
            searchdiagonaldownright(line, letter)
            searchdiagonalupright(line, letter)
            searchdiagonalupleft(line, letter)
            searchdiagonaldownleft(line, letter)

print(counter)