from random import randint

global resArr
resArr = []


# def getAllData(amountOfItems: int, knapsackWeight: int):
#     weights = []
#     values = []
#
#     while len(weights) != amountOfItems or len(values) != amountOfItems:
#         weights = list(set([randint(2, knapsackWeight) for _ in range(amountOfItems)]))  # веса
#         values = list(set([randint(2, amountOfItems * 2) for _ in range(amountOfItems)]))  # ценность
#
#     resTuple = []
#
#     for i in range(len(weights)):
#         resTuple.append(tuple([weights[i], values[i]]))
#
#     return resTuple


def exhaustiveSearch(amountOfItems: int, data: list):
    # data = [(5, 10), (8, 7), (2, 2), (4, 6), (1, 3)]
    # data = [(2, 2), (2, 6), (2, 3)]

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
    exhaustiveSearch(amountOfItems, tupleList)
    maxValue, savedWeight, savedPairs = findMaxValue(knapsackWeight)

    print('\nПолный перебор:')
    print('Макс. вместимость рюкзака:', knapsackWeight)
    print('Макс. стоимость:', maxValue, 'Вес:', savedWeight, 'Список пар:', savedPairs)
