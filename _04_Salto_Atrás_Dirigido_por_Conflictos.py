#Salto Atrás Dirigido por Conflictos

def conflict_directed_backjumping(csp):
    return recursive_cbj({}, csp)

def recursive_cbj(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment

    var = select_unassigned_variable(assignment, csp)
    for value in order_domain_values(var, assignment, csp):
        if is_consistent(var, value, assignment, csp):
            assignment[var] = value
            inferences = forward_check(var, value, assignment, csp)
            if inferences is not None:
                result = recursive_cbj(assignment, csp)
                if result is not None:
                    return result
            undo_forward_check(var, value, assignment, inferences, csp)
            del assignment[var]
    return None

def forward_check(var, value, assignment, csp):
    inferences = {}
    for neighbor in csp.neighbors[var]:
        if neighbor not in assignment:
            pruned_values = []
            for neighbor_value in csp.domains[neighbor]:
                if not is_consistent(neighbor, neighbor_value, assignment, csp):
                    pruned_values.append(neighbor_value)
            if pruned_values:
                inferences[neighbor] = pruned_values
                csp.domains[neighbor] = [v for v in csp.domains[neighbor] if v not in pruned_values]
    return inferences

def undo_forward_check(var, value, assignment, inferences, csp):
    for neighbor, pruned_values in inferences.items():
        csp.domains[neighbor].extend(pruned_values)

# Funciones esenciales
def select_unassigned_variable(assignment, csp):
    unassigned_variables = [var for var in csp.variables if var not in assignment]
    if unassigned_variables:
        return unassigned_variables[0]  # Selecciona la primera variable no asignada
    return None

def order_domain_values(var, assignment, csp):
    return csp.domains[var]  # No se realiza ning�n ordenamiento

def is_consistent(var, value, assignment, csp):
    for neighbor in csp.neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False  # Hay un conflicto
    return True

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
solution = conflict_directed_backjumping(problem)
print("Solucion encontrada:", solution)


