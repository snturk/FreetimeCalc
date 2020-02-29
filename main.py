cmd = 0
schU = []
aabb = [[13.30, 14.50], [11.30, 13.20], [13.22, 13.25]]
totalTime = []
ftimeTotal = 0
order = 0

def replace(array, index):
        store = array[index]
        array[index] = array[index + 1]
        array[index + 1] = store

print("Welcome to The Freetime Calculator")
while True:
    print("Choose a beginning time for your day: (xx.xx)")
    begTime = float(input())
    print("Now choose an end time for your day: (xx.xx)")
    endTime = float(input())
    if begTime >= endTime:
        print("Wrong time format")
    else:
        totalTime.append(begTime)
        totalTime.append(endTime)
        break

while cmd != 3:
    cmd = 0
    print(
"""Choose an operation:
1- Add event
2- Show freetimes
3- Exit"""
    )
    cmd = int(input())

    if cmd == 1:
        print("Add an event start time: (xx.xx)")
        eventStart = float(input())
        print("Add an event end time: (xx.xx)")
        eventEnd = float(input())
        if eventStart >= begTime and eventEnd <= endTime:
            schU.append([eventStart, eventEnd])
            print("Event has been added")
        else:
            print("Event time is not compatible with your beginning/ending time of your day...")
    elif cmd == 2:
        freeTime = []
        for i in range(len(schU) - 1):
            if schU[i][0] > schU[i + 1][0]:
                replace(schU, i)
        if schU[0][0] != totalTime[0]:
            freeTime.insert(order, [totalTime[0], schU[0][0]])
            order += 1

        for i in range(len(schU) - 1):
            ftimeStart = 0
            ftimeEnd = 0
            if schU[i][1] != schU[i + 1][0]:
                ftimeStart = float(schU[i][1])
                ftimeEnd = float(schU[i + 1][0])
                ftimeTotal += ftimeEnd - ftimeStart
                freeTime.append([ftimeStart, ftimeEnd])

        if schU[-1][1] != totalTime[1]:
            freeTime.append([schU[-1][1], totalTime[1]])

        print("Your freetimes:")
        for i in range(len(freeTime)):
            print("{:.2f}".format(float(freeTime[i][0])) + " - " + "{:.2f}".format(float(freeTime[i][1])))

    elif cmd == 3:
        break
    else:
        print("Wrong command...")
