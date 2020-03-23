from datetime import datetime


def printMatrix(m):
    print('\n'.join(str(i) + ': ' + str(e) for i, e in enumerate(m)) + '\n')


def knapsackProblem0_1(amountOfItems, knapsackWeight, m, weights, values, pairsMatrix):
    for i in range(len(weights)):
        m[i][weights[i]] = values[i]
        pairsMatrix[i][weights[i]] = [(weights[i], values[i])]

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

    return pairsMatrix[-1][-1], m[-1][-1], sum([x for x, _ in pairsMatrix[-1][-1]])


def printKnapsackProblem0_1(amountOfItems, knapsackWeight, m, weights, values, pairsMatrix):
    t0 = datetime.now()
    pairs, maxValue, weight = knapsackProblem0_1(amountOfItems, knapsackWeight, m, weights, values, pairsMatrix)

    print('Задача о рюкзаке 0-1:')
    s0 = 'Макс. стоимость: ' + str(maxValue)
    s1 = 'Вес: ' + str(weight)
    s2 = 'Список пар: ' + str(pairs)
    print(s0, s1, 'Затраченное время:',
          str((datetime.now() - t0).seconds) + '.' + str((datetime.now() - t0).microseconds) + ' сек.')
    #
    # print('Макс. стоимость:', maxValue, 'Вес:', weight, 'Список пар:', pairs, 'Затраченное время:',
    #       str((datetime.now() - t0).seconds) + '.' +
    #       str((datetime.now() - t0).microseconds) + ' сек.')
