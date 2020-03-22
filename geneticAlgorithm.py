from random import randint, shuffle
from knapsackProblem0_1 import printMatrix


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
def selection(population: list, weights, values, knapsackWeight: int):
    allData, less_than_weight = fitnessFunction(population, weights, values, knapsackWeight)

    if len(less_than_weight) < len(allData) // 2:
        for i in range(len(allData) // 2 - len(less_than_weight)):
            less_than_weight.append(allData[i])

    less_than_weight = list(sorted(less_than_weight, key=lambda k: k[2], reverse=True))[0: len(allData) // 2]

    return less_than_weight


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


# супермутация - когда происходит вырождение популяции
def superMutation(crossedPopulation):
    printMatrix(crossedPopulation)
    mutatedPopulation = [[x if randint(0, 9) > 4 else int(not x) for x in crossedPopulation[i]]
                         for i in range(len(crossedPopulation))]

    printMatrix(mutatedPopulation)

    return mutatedPopulation


def geneticAlgorithm(amountOfItems, knapsackWeight, weights, values, numberOfGenerations):
    numberOfIndividuals = 10  # количество особей в первой популяции
    population = getData(amountOfItems, numberOfIndividuals)

    preResultedPopulation = []
    for number in range(numberOfGenerations + 1):
        selectedPopulation = selection(population, weights, values, knapsackWeight)

        crossedPopulation = crossing(selectedPopulation, numberOfIndividuals)
        mutatedPopulation = mutation(crossedPopulation)
        # готовимся к следующему раунду
        population = list(mutatedPopulation)

        _, preResultedPopulation = fitnessFunction(population, weights, values, knapsackWeight)
        if not preResultedPopulation:
            numberOfGenerations += 1

    return preResultedPopulation[0]


def printGeneticAlgorithm(amountOfItems, knapsackWeight, weights, values, numberOfGenerations):
    preResultedPopulation = geneticAlgorithm(amountOfItems, knapsackWeight, weights, values, numberOfGenerations)

    resultedPopulation = getAnswer(preResultedPopulation, weights, values)

    print('\nГенетический алгоритм:')
    print('Макс. стоимость:', resultedPopulation[2], 'Вес:', resultedPopulation[1], 'Список пар:',
          resultedPopulation[0])
