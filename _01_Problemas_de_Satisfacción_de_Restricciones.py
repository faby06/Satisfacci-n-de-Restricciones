#- Problemas de Satisfacción de Restricciones
def constraint_propagation(csp):
    queue = [(X, Y) for X in csp.variables for Y in csp.neighbors[X]]
    while queue:
        (X, Y) = queue.pop()
        if revise(X, Y, csp):
            if not csp.domains[X]:
                return False
            for Z in csp.neighbors[X]:
                if Z != Y:
                    queue.append((Z, X))
    return True

def revise(X, Y, csp):
    revised = False
    for x in csp.domains[X][:]:
        if not any(satisfies(x, y) for y in csp.domains[Y]):
            csp.domains[X].remove(x)
            revised = True
    return revised

def satisfies(x, y):
    # Implementa la funci�n de satisfacci�n seg�n tus necesidades.
    pass

# Ejemplo de uso:
class CSP:
    def __init__(self):
        self.variables = ["A", "B", "C"]
        self.domains = {
            "A": [1, 2, 3],
            "B": [1, 2, 3],
            "C": [1, 2, 3]
        }
        self.neighbors = {
            "A": ["B", "C"],
            "B": ["A", "C"],
            "C": ["A", "B"]
        }

problem = CSP()  # Define el CSP como en el ejemplo anterior

if constraint_propagation(problem):
    solution = backtracking_search(problem)
    print("Solucion encontrada:", solution)
else:
    print("No hay solucion.")



