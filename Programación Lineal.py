from pulp import*

#Declaración de variables
prob = LpProblem("Producción", LpMaximize)  #Creación de Lp maximization problem

F1 = LpVariable("F1", lowBound=0, upBound=5)  #Combustible 1
F2 = LpVariable("F2", lowBound=0, upBound=4)  #Combustible 2

#restricciones
prob += (200*F1+250*F2, 'Función Objetivo')
prob += (1*F1+2*F2 <= 1000, 'Restricción 1')
prob += (1*F1+2*F2 <= 1200, 'Restricción 2')
prob += (2*F1+2*F2 <= 900, 'Restricción 3')
prob += (4*F1+3*F2 <= 1500, 'Restricción 4')
prob += (F1 <= 200, 'Restricción 5')
prob += (F2 <= 400, 'Restricción 6')
print(prob)  #Impresión en pantalla

#Solución Optima
status = prob.solve()
print(f"status: {prob.status}, {LpStatus[prob.status]}")
print(f"objective: {prob.objective.value()}")

for var in prob.variables():
    print(f"{var.name}: {var.value()}")
