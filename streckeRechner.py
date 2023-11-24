# Rechner

strecke = float(input('Strecke km: '))
liter = float(input('Liter l: '))

# Berechnung des Benzinverbrauchs pro Strecke in Liter
proStrecke = liter / strecke
durchschnittsVerbrauch = proStrecke * 100
print(f'Durchschnittsverbrauch auf 100km: {round(durchschnittsVerbrauch, 2)}')