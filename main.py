from exhaustiveSearch import *
from geneticAlgorithm import *
from knapsackProblem0_1 import *
from greedyAlgorithm import *


def getAllData(amountOfItems: int, knapsackWeight: int):
    weights = [randint(2, amountOfItems) for _ in range(amountOfItems)]  # веса
    values = [randint(2, amountOfItems * 2) for _ in range(amountOfItems)]  # ценность

    tupleList = []
    for i in range(len(weights)):
        tupleList.append(tuple([weights[i], values[i]]))

    m = [[0 for _ in range(knapsackWeight)] for _ in range(amountOfItems)]

    pairsMatrix = [[[] for _ in range(knapsackWeight)] for _ in range(amountOfItems)]

    greedyList = [values[i] / weights[i] for i in range(len(values))]
    greedyMatrix = [(weights[i], values[i], greedyList[i]) for i in range(len(weights))]

    return tupleList, m, weights, values, pairsMatrix, sorted(greedyMatrix, key=lambda k: k[2], reverse=True)


if __name__ == '__main__':
    # Определяем входные данные:
    amountOfItems = 5
    knapsackWeight = amountOfItems * 15

    print('Количество предметов:', amountOfItems)
    print('Макс. вместимость рюкзака:', knapsackWeight)

    # tupleList - для полного перебора [(w0, v0), ..., (wi, vi), ..., (wn, vn)]
    # m, weights, values, pairsMatrix - для задаче о рюкзаке 0-1
    tupleList, m, weights, values, pairsMatrix, greedyMatrix = getAllData(amountOfItems, knapsackWeight)

    # Полный перебор
    printExhaustiveSearch(amountOfItems, knapsackWeight, tupleList)

    # Задача о рюкзаке 0-1
    printKnapsackProblem0_1(amountOfItems, knapsackWeight, m, weights, values, pairsMatrix)

    # Жадный алгоритм
    printGreedyAlgorithm(greedyMatrix, amountOfItems, knapsackWeight)

    # Генетический алгоритм
    printGeneticAlgorithm(amountOfItems, knapsackWeight, weights, values, 100)
