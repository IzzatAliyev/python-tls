def rabattRechnen(umsatz):
    rabatt = 0
    betrag = 0
    if (umsatz > 100):
        if (umsatz > 500):
            rabatt = 10
        else:
            rabatt = 5
    betrag = umsatz - umsatz/100 * rabatt
    return betrag

input_value = int(input('Geben Sie den Umsatz ein: '))
result = rabattRechnen(input_value)
print("Der Rabatt ist: ", result)