def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Divisao por zero nao e permitida.")
    return a / b

def somar(a: float, b: float) -> float:
    return a + b
