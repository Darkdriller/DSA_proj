import time
no_comp = 0
def merge_sort(data, drawData, timeTick,merge_canv):
    global no_comp
    no_comp=0
    merge_sort_alg(data,0, len(data)-1, drawData, timeTick,merge_canv)
    return no_comp

def merge_sort_alg(data, left, right, drawData, timeTick,merge_canv):
    global no_comp
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, drawData, timeTick,merge_canv)
        merge_sort_alg(data, middle+1, right, drawData, timeTick,merge_canv)
        merge(data, left, middle, right, drawData, timeTick,merge_canv)

def merge(data, left, middle, right, drawData, timeTick,merge_canv):
    global no_comp
    drawData(data, getColorArray(len(data), left, middle, right),merge_canv)
    time.sleep(timeTick)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1: right+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                no_comp+=1
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1

    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))],merge_canv)
    time.sleep(timeTick)

def getColorArray(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("yellow")
            else:
                colorArray.append("black")
        else:
            colorArray.append("white")

    return colorArray
