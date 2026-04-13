# Importa a biblioteca que resolve expressões matemáticas com ordem correta
import re

# Função que soma dois números
def somar(a, b):
    return a + b

# Função que subtrai dois números
def subtrair(a, b):
    return a - b

# Função que multiplica dois números
def multiplicar(a, b):
    return a * b

# Função que divide dois números
def dividir(a, b):
    if b == 0:  # verifica se o segundo número é zero
        return "Erro: divisão por zero!"
    return a / b

# Função principal que resolve a expressão completa respeitando a ordem correta
def calcular_expressao(expressao):
    try:
        # Substitui os símbolos visuais pelos operadores do Python
        expressao = expressao.replace("×", "*")
        expressao = expressao.replace("÷", "/")
        expressao = expressao.replace(",", ".")

        # Verifica se a expressão tem apenas números e operadores permitidos
        if not re.match(r'^[\d\s\+\-\*\/\.\(\)]+$', expressao):
            return "Erro: expressão inválida!"

        # O Python já respeita a ordem correta de operações
        resultado = eval(expressao)

        # Arredonda para evitar casas decimais desnecessárias
        return round(resultado, 10)

    except ZeroDivisionError:
        return "Erro: divisão por zero!"
    except:
        return "Erro: expressão inválida!"