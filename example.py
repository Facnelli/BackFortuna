x = 1+ 2  # espaços errados
y = 3
z = 1


def soma(a, b):  # sem espaço depois da vírgula
    
    
    return a + b


def inutil():
    print("Função que não é usada")  # Ruff detecta função não usada


print(soma(x, y))
