
gesamt = 0;
def vergleiche_temperatur(gesamtVal):
    result = gesamtVal / 5
    print(result)

for i in range(1,6):
    temp = int(input(f"Temp {i}: "))
    gesamt += temp
    
vergleiche_temperatur(gesamt)