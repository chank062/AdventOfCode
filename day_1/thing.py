# get file and read lines
with open('input.txt') as r:
    lines = r.readlines()

count = 0
for line in lines:
    count += int(line)

print("Part 1: " + str(count)) #505

count2 = set()
count = 0
pos = 0

while (True):
    # [pos %remainder (number of lines)]
    count += int(lines[pos % len(lines)])
    if (count in count2):
        break # if value is in set (then you've found the reocurring frequency)
    count2.add(count) # add to set
    pos += 1 # increment

print("Part 2: " + str(count)) # 72330
