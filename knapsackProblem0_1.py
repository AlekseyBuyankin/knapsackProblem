from random import randint


# def getAllData(amountOfItems: int, knapsackWeight: int):
#     weights = []
#     values = []
#
#     while len(weights) != amountOfItems or len(values) != amountOfItems:
#         weights = list(set([randint(2, knapsackWeight - 1) for _ in range(amountOfItems)]))  # веса
#         values = list(set([randint(2, amountOfItems * 2) for _ in range(amountOfItems)]))  # ценность
#
#     m = [[0 for _ in range(knapsackWeight)] for _ in range(amountOfItems)]
#
#     pairsMatrix = [[[] for _ in range(knapsackWeight)] for _ in range(amountOfItems)]
#
#     return m, weights, values, pairsMatrix


def printMatrix(m):
    print('\n'.join(str(e) for e in m) + '\n')


def knapsackProblem0_1(amountOfItems, knapsackWeight, m, weights, values, pairsMatrix):
    # m, weights, values, pairsMatrix = getAllData(amountOfItems, knapsackWeight)

    for i in range(len(weights)):
        m[i][weights[i]] = values[i]
        pairsMatrix[i][weights[i]] = [(weights[i], values[i])]

    # Ввод:
    # Ценности предметов(загруженные в массив v = values)
    # Веса предметов(загруженные в массив w = weights)
    # Количество предметов(n = amountOfItems)
    # Грузоподъемность(W = knapsackWeight)

    for i in range(amountOfItems):
        for j in range(knapsackWeight):
            if weights[i] > j:
                m[i][j] = m[i - 1][j]
                pairsMatrix[i][j] = pairsMatrix[i - 1][j]
            else:
                m[i][j] = max(m[i - 1][j], m[i - 1][j - weights[i]] + values[i])
                newList = list(pairsMatrix[i - 1][j - weights[i]])
                newList.append((weights[i], values[i]))
                pairsMatrix[i][j] = pairsMatrix[i - 1][j] if m[i - 1][j] > m[i - 1][j - weights[i]] + values[i] \
                    else newList

    # printMatrix(m)
    # printMatrix(pairsMatrix)

    return pairsMatrix[-1][-1], m[-1][-1], sum([x for x, _ in pairsMatrix[-1][-1]])


def printKnapsackProblem0_1(amountOfItems, knapsackWeight, m, weights, values, pairsMatrix):
    pairs, maxValue, weight = knapsackProblem0_1(amountOfItems, knapsackWeight, m, weights, values, pairsMatrix)

    print('\nЗадача о рюкзаке 0-1:')
    print('Макс. вместимость рюкзака:', knapsackWeight)
    print('Макс. стоимость:', maxValue, 'Вес:', weight, 'Список пар:', pairs)
