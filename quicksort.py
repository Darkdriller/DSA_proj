import time
no_comp = 0
def partition(data, head, tail, drawData, timeTick,quick_canv):
    global no_comp
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border),quick_canv)
    time.sleep(timeTick)

    for j in range(head, tail):
        if data[j] < pivot:
            no_comp+=1
            drawData(data, getColorArray(len(data), head, tail, border, j, True),quick_canv)
            time.sleep(timeTick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j),quick_canv)
        time.sleep(timeTick)


    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True),quick_canv)
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]

    return border

def quick_sort(data, head, tail, drawData, timeTick,quick_canv,comp):
    global no_comp
    no_comp=comp
    if head < tail:
        no_comp+=1
        partitionIdx = partition(data, head, tail, drawData, timeTick,quick_canv)

        #LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawData, timeTick,quick_canv,no_comp)

        #RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick,quick_canv,no_comp)

    return no_comp
def getColorArray(dataLen, head, tail, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')

        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = 'green'

    return colorArray
