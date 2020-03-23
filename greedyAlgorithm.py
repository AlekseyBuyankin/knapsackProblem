from datetime import datetime


def greedyAlgorithm(greedyMatrix: list, amountOfItems: int, knapsackWeight: int):
    sumWeight = 0
    pairs = []
    for i in range(amountOfItems):
        if sumWeight + greedyMatrix[i][0] < knapsackWeight:
            sumWeight += greedyMatrix[i][0]
            pairs.append((greedyMatrix[i][0], greedyMatrix[i][1]))
        else:
            continue

    return pairs


def printGreedyAlgorithm(greedyMatrix: list, amountOfItems: int, knapsackWeight: int):
    t0 = datetime.now()
    pairs = greedyAlgorithm(greedyMatrix, amountOfItems, knapsackWeight)
    maxValue = sum([v for _, v in pairs])
    weight = sum([w for w, _ in pairs])

    print('Жадный алгоритм:')
    s0 = 'Макс. стоимость: ' + str(maxValue)
    s1 = 'Вес: ' + str(weight)
    s2 = 'Список пар: ' + str(pairs)
    print(s0, s1, 'Затраченное время:',
          str((datetime.now() - t0).seconds) + '.' + str((datetime.now() - t0).microseconds) + ' сек.')
    #
    # print('Макс. стоимость:', maxValue, 'Вес:', weight, 'Список пар:', pairs, 'Затраченное время:',
    #       str((datetime.now() - t0).seconds) + '.' +
    #       str((datetime.now() - t0).microseconds) + ' сек.')
