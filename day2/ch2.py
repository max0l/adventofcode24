# This checks if the following numbers are smaller and returns nothing if so
def checksmaller(nums):
    for x in range(len(nums) - 1):
        if nums[x] < nums[x + 1] and nums[x + 1] in range(nums[x] + 1, nums[x] + 4):
            continue
        else:
            return False
    return True


def checkbigger(nums):
    for x in range(len(nums) - 1):
        if nums[x] > nums[x + 1] and nums[x + 1] in range(nums[x] - 3, nums[x]):
            continue
        else:
            return False
    return True


file = open("ch2/input", "r")
content = file.read()
lines = content.split("\n")
number_lines = []
safe_counter = 0
for line in lines:
    if len(line) > 5:
        strings = line.split()
        temp_num_array = []
        for string in strings:
            temp_num_array.append(int(string))
        number_lines.append(temp_num_array)

for numbers in number_lines:
    for x in range(len(numbers)):
        superset = x
        nums_superset = []
        for y in range(len(numbers)):
            if y != superset:
                nums_superset.append(numbers[y])

        if nums_superset[0] < nums_superset[1]:
            if checksmaller(nums_superset):
                safe_counter = safe_counter + 1
                break
        elif nums_superset[0] > nums_superset[1]:
            if checkbigger(nums_superset):
                safe_counter = safe_counter + 1
                break
        else:
            continue

print(safe_counter)