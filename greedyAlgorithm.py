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
    pairs = greedyAlgorithm(greedyMatrix, amountOfItems, knapsackWeight)
    maxValue = sum([v for _, v in pairs])
    weight = sum([w for w, _ in pairs])

    print('\nЖадный алгоритм:')
    print('Макс. вместимость рюкзака:', knapsackWeight)
    print('Макс. стоимость:', maxValue, 'Вес:', weight, 'Список пар:', pairs)
