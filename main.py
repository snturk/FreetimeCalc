cmd = 0
schUnordered = []
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
            schUnordered.append([eventStart, eventEnd])
            print("Event has been added")
        else:
            print("Event time is not compatible with your beginning/ending time of your day...")
    elif cmd == 2:
        freeTime = []
        for i in range(len(schUnordered) - 1):
            if schUnordered[i][0] > schUnordered[i + 1][0]:
                replace(schUnordered, i)
        if schUnordered[0][0] != totalTime[0]:
            freeTime.insert(order, [totalTime[0], schUnordered[0][0]])
            order += 1

        for i in range(len(schUnordered) - 1):
            ftimeStart = 0
            ftimeEnd = 0
            if schUnordered[i][1] != schUnordered[i + 1][0]:
                ftimeStart = float(schUnordered[i][1])
                ftimeEnd = float(schUnordered[i + 1][0])
                ftimeTotal += ftimeEnd - ftimeStart
                freeTime.append([ftimeStart, ftimeEnd])

        if schUnordered[-1][1] != totalTime[1]:
            freeTime.append([schUnordered[-1][1], totalTime[1]])

        print("Your freetimes:")
        for i in range(len(freeTime)):
            print("{:.2f}".format(float(freeTime[i][0])) + " - " + "{:.2f}".format(float(freeTime[i][1])))

    elif cmd == 3:
        break
    else:
        print("Wrong command...")
