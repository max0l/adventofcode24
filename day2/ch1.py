# This checks if the following numbers are smaller and returns nothing if so
def checksmaller(nums):
    for x in range(len(nums)-1):
        if nums[x] < nums[x+1] and nums[x+1] in range(nums[x]+1, nums[x]+4):
            continue
        else:
            return False
    return True

def checkbigger(nums):
    for x in range(len(nums)-1):
        if nums[x] > nums[x+1] and nums[x+1] in range(nums[x]-3, nums[x]):
            continue
        else:
            return False
    return True


file = open("input", "r")
content = file.read()
lines = content.split("\n")
numbers = []
safe_counter = 0
for line in lines:
    if len(line) > 5:
        strings = line.split()
        temp_num_array = []
        for string in strings:
            temp_num_array.append(int(string))
        numbers.append(temp_num_array)

for nums in numbers:
    if nums[0] < nums[1]:
        if checksmaller(nums):
            safe_counter = safe_counter + 1
    elif nums[0] > nums[1]:
        if checkbigger(nums):
            safe_counter = safe_counter + 1
    else:
        continue

print(safe_counter)