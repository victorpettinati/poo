class Operation:
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __str__(self):
        return f"Opération({self.nombre1}, {self.nombre2})"

operation = Operation()
print(operation)