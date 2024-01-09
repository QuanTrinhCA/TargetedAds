print("Input:")

#Get min number of perfect [0] and perfect + close cases [1]
buffer = input().split()
minNumOfCases = [int(buffer[0]), int(buffer[1])]
del buffer

locations = dict()
for x1 in range(int(input())):
    name = input()
    result = [0, 0, 0]
    for x2 in range(int(input())):
        buffer = input().split()
        if buffer[2] == "yes":
            if int(buffer[0]) >= 30 and int(buffer[0]) <= 39:
                if int(buffer[1]) >= 6 and int(buffer[1]) <= 10:
                    result[0] += 1
                    result[1] += 1
                elif (int(buffer[1]) >= 3 and int(buffer[1]) <= 5) or (int(buffer[1]) >= 11 and int(buffer[1]) <= 15):
                    result[1] += 1
            elif (int(buffer[0]) >= 20 and int(buffer[0]) <= 29) or (int(buffer[0]) >= 40 and int(buffer[0]) <= 49):
                if int(buffer[1]) >= 6 and int(buffer[1]) <= 10:
                    result[1] += 1
    if result[0] >= minNumOfCases[0] and result[1] >= minNumOfCases[1]:
        result[2] = 1
    locations[name] = result

for x in locations:
    if locations[x][2] == 1: print("Good: " + x + " " + str(locations[x][0]) + " " + str(locations[x][1]))
    else: print("Not good: " + x + " " + str(locations[x][0]) + " " + str(locations[x][1]))