def imprime_menu():
    print('''MENÚ
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
Elija una opción:
          ''')

def escoger_opcion():
    correcta = False
    while not correcta:
        imprime_menu()
        opcion = int(input())
        if opcion >= 1 and opcion <= 5: # Correcta
            correcta = True
    return opcion

def pedir_operandos():
    op1 = float(input("Escribe el primer operando: "))
    op2 = float(input("Escribe el segundo operando: "))
    return op1, op2

def sumar(op1, op2):
    return op1 + op2

def restar(op1, op2):
    return op1 - op2

def multiplicar(op1, op2):
    return op1 * op2

def dividir(op1, op2):
    if op2 != 0:
        return op1 / op2
    else:
        print("No se puede dividir entre 0")

# Programa principal
opcion = 1
while opcion != 5:
    opcion = escoger_opcion()
    if opcion >= 1 and opcion <= 4:
        op1, op2 = pedir_operandos()
        if opcion == 1:
            resultado = sumar(op1, op2)
        elif opcion == 2:
            resultado = restar(op1, op2)
        elif opcion == 3:
            resultado = multiplicar(op1, op2)
        elif opcion == 4:
            resultado = dividir(op1, op2)

    if (resultado != None):
        print(round(resultado, 2))