# get file and read lines
with open('input.txt') as r:
    lines = r.readlines()

count = 0
for line in lines:
    count += int(line)

print("Part 1: " + str(count))
