def operation(num1, num2, oper):
    match oper:
        case 1: print(sum(num1, num2))
        case 2: print(minus(num1, num2))
        case 3: print(multiply(num1, num2))
        case 4: print(divide(num1, num2))
        case _: print('nix')

def sum(num1, num2):
    return num1 + num2
def divide(num1, num2):
    return num1 / num2
def multiply(num1, num2):
    return num1 * num2
def minus(num1, num2):
    return num1 - num2

print('Wählen Sie ein operation: ')
wahl = int(input(
    '''
    (1) sum
    (2) minus
    (3) multiply
    (4) divide
    '''))
num1 = int(input('Geben Sie erste Nummer ein: '))
num2 = int(input('Geben Sie zweite Nummer ein: '))

operation(num1, num2, wahl)