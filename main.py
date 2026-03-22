from pulp import LpProblem, LpVariable, LpMinimize, value
from math import ceil

problem = LpProblem("Diet", LpMinimize)
xOvo = LpVariable("Ovo", lowBound=1)
xSoja = LpVariable("Soja", lowBound=30, upBound=30)
xArroz = LpVariable("Arroz", lowBound=300)
xFeijao = LpVariable("Feijao", lowBound=300)
xPao = LpVariable("Pao", lowBound=1, upBound=9)

problem += (
    71 * xOvo + 1.3 * xArroz + 1.32 * xFeijao + 141.5 * xPao + 4 * xSoja == 3400
)  # Kcal
problem += (
    0.5 * xOvo + 0.286 * xArroz + 0.324 * xFeijao + 25 * xPao + 0.026 * xSoja <= 480
)  # Carboidrato
problem += (
    5.8 * xOvo + 0.027 * xArroz + 0.089 * xFeijao + 5.5 * xPao + 0.9 * xSoja >= 160
)  # Proteina
problem += (
    5.2 * xOvo + 0.003 * xArroz + 0.005 * xFeijao + 2.1 * xPao + 0.03 * xSoja == 80
)  # Gordura
problem.solve()

for item in [xSoja, xArroz, xFeijao]:
    print(f"{item.name}: {ceil(value(item)):.2f}g")
for item in [xOvo, xPao]:
    print(f"{item.name}: {ceil(value(item))} unidades")

kcal = (
    71 * value(xOvo)
    + 1.3 * value(xArroz)
    + 1.32 * value(xFeijao)
    + 141.5 * value(xPao)
    + 4 * value(xSoja)
)
carboidrato = (
    0.5 * value(xOvo)
    + 0.286 * value(xArroz)
    + 0.324 * value(xFeijao)
    + 25 * value(xPao)
    + 0.026 * value(xSoja)
)
proteina = (
    5.8 * value(xOvo)
    + 0.027 * value(xArroz)
    + 0.089 * value(xFeijao)
    + 5.5 * value(xPao)
    + 0.9 * value(xSoja)
)
gordura = (
    5.2 * value(xOvo)
    + 0.003 * value(xArroz)
    + 0.005 * value(xFeijao)
    + 2.1 * value(xPao)
    + 0.03 * value(xSoja)
)

print("\n")
print(f"Kcal: {ceil(kcal)}")
print(f"Carboidrato: {ceil(carboidrato)}")
print(f"Proteina: {ceil(proteina)}")
print(f"Gordura: {ceil(gordura)}")
