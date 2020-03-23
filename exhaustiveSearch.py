from datetime import datetime

global resArr
resArr = []


def exhaustiveSearch(amountOfItems: int, data: list):
    recSearch(data, 0, [], amountOfItems)


def recSearch(data: list, index: int, buff: list, amountOfItems: int):
    if index < amountOfItems:
        buff2 = list(buff)
        buff2.append(data[index])

        recSearch(data, index + 1, buff, amountOfItems), recSearch(data, index + 1, buff2, amountOfItems)
    else:
        resArr.append(buff)
        return buff


def findMaxValue(knapsackWeight):
    maxValue = 0
    savedWeight = 0
    savedPairs = []

    for pairs in resArr:
        weight = 0
        value = 0
        for pair in pairs:
            weight += pair[0]
            value += pair[1]

        if weight > knapsackWeight:
            continue

        else:
            if maxValue < value:
                maxValue = value
                savedWeight = weight
                savedPairs = list(pairs)
    return maxValue, savedWeight, savedPairs


def printExhaustiveSearch(amountOfItems, knapsackWeight, tupleList):
    t0 = datetime.now()
    exhaustiveSearch(amountOfItems, tupleList)
    maxValue, savedWeight, savedPairs = findMaxValue(knapsackWeight)

    print('Полный перебор:')
    s0 = 'Макс. стоимость: ' + str(maxValue)
    s1 = 'Вес: ' + str(savedWeight)
    s2 = 'Список пар: ' + str(savedPairs)
    print(s0, s1, 'Затраченное время:',
          str((datetime.now() - t0).seconds) + '.' + str((datetime.now() - t0).microseconds) + ' сек.')
