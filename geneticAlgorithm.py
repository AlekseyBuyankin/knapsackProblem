from random import randint, shuffle
from datetime import datetime
from knapsackProblem0_1 import printMatrix
from numpy import var, sqrt, random
import numpy as np


def getData(amountOfItems, numberOfIndividuals):
    return [[randint(0, 1) for _ in range(amountOfItems)] for _ in range(numberOfIndividuals)]


def getAnswer(preResultedPopulation, weight, values):
    resultedPopulation = []

    for i in range(len(weight)):
        if preResultedPopulation[0][i] == 1:
            resultedPopulation.append((weight[i], values[i]))

    return (resultedPopulation, preResultedPopulation[1], preResultedPopulation[2])


def fitnessFunction(population: list, weights: list, values: list, knapsackWeight: int):
    hw = []
    hv = []

    for i in range(len(population)):
        sumWeight = 0
        sumValue = 0
        for j in range(len(population[0])):
            if population[i][j] == 1:
                sumWeight += weights[j]
                sumValue += values[j]
        hw.append(sumWeight)
        hv.append(sumValue)

    allData = list(
        sorted([(population[i], hw[i], hv[i]) for i in range(len(hv))], key=lambda k: k[1], reverse=True))

    less_than_weight = list(sorted(list(filter(lambda k: k[1] <= knapsackWeight, allData)),
                                   key=lambda k: k[2], reverse=True))
    return allData, less_than_weight


# селекция (отбор)
def sigmaClippingSelection(population: list, weights, values, knapsackWeight: int):
    allData, less_than_weight = fitnessFunction(population, weights, values, knapsackWeight)

    h = [ind[1] for ind in allData]
    favg = sum(h) / len(allData)
    Fis = [1 + (fi - favg) / (2 * sqrt(var(h))) for fi in h]
    pi = np.array([Fi / sum(Fis) for Fi in Fis])
    sumNegPi = sum(list(filter(lambda p: p < 0, pi)))

    pi = [0 if p < 0 else p for p in pi]

    if sumNegPi != 0:
        pi[0] += sumNegPi

    pi = [0 if np.isnan(p) else p for p in pi]

    indexes = [x for x in range(len(allData))]
    resIndexes = random.choice(indexes, len(indexes) // 2, p=pi, replace=False)
    resList = [allData[i] for i in resIndexes]

    return resList


# скрещивание
def crossing(selectedPopulation, numberOfIndividuals):
    crossedPopulation = []

    for _ in range(numberOfIndividuals):
        shuffle(selectedPopulation)
        parent1 = selectedPopulation[0][0]
        shuffle(selectedPopulation)
        parent2 = selectedPopulation[0][0]

        crossedPopulation.append(parent1[0:len(parent1) // 2] + parent2[len(parent2) // 2:])

    return crossedPopulation


# мутация
def mutation(crossedPopulation):
    mutatedPopulation = [[x if randint(0, 9) > 1 else int(not x) for x in crossedPopulation[i]]
                         for i in range(len(crossedPopulation))]
    return mutatedPopulation


def geneticAlgorithm(amountOfItems, knapsackWeight, weights, values, numberOfGenerations):
    numberOfIndividuals = amountOfItems * 2  # количество особей в первой популяции
    population = getData(amountOfItems, numberOfIndividuals)
    preResultedPopulation = []

    for number in range(numberOfGenerations + 1):
        selectedPopulation = sigmaClippingSelection(population, weights, values, knapsackWeight)

        crossedPopulation = crossing(selectedPopulation, numberOfIndividuals)

        mutatedPopulation = mutation(crossedPopulation)

        # готовимся к следующему раунду
        population = list(mutatedPopulation)

        allData, preResultedPopulation = fitnessFunction(population, weights, values, knapsackWeight)

    return preResultedPopulation[0]


def printGeneticAlgorithm(amountOfItems, knapsackWeight, weights, values, numberOfGenerations):
    t0 = datetime.now()
    preResultedPopulation = geneticAlgorithm(amountOfItems, knapsackWeight, weights, values, numberOfGenerations)

    resultedPopulation = getAnswer(preResultedPopulation, weights, values)

    print('Генетический алгоритм:')
    s0 = 'Макс. стоимость: ' + str(resultedPopulation[2])
    s1 = 'Вес: ' + str(resultedPopulation[1])
    s2 = 'Список пар: ' + str(resultedPopulation[0])
    print(s0, s1, 'Затраченное время:',
          str((datetime.now() - t0).seconds) + '.' + str((datetime.now() - t0).microseconds) + ' сек.')
