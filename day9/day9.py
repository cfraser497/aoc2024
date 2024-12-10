with open("day9.txt", "r") as file:
    diskMap = file.read().strip()

isBlock = True
idNum = 0
disk =[]
# diskMap = "2333133121414131402"


for block in diskMap:
    c = (idNum // 2) if isBlock else "."
    for _ in range(int(block)):
        disk.append(str(c))
    idNum += 1
    isBlock = not isBlock

# print(disk)

r = len(disk) - 1
for i in range(len(disk)):
    if disk[i] != ".":
        continue

    while disk[r] == ".":
        r -= 1

    if i >= r:
        break

    disk[i], disk[r] = disk[r], disk[i]
    r -= 1


total = 0
for i in range(len(disk)):
    if disk[i] == ".":
        continue
    total += int(disk[i]) * i
    i += 1

print(total)
