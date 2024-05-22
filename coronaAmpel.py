print("Corona-Ampel")
print("=============\n\n")
neu = int(input("Geben Sie die Neuinfektionen der vergangenen 7 Tagen ein: "))
wohnerZahl = int(input("Geben Sie der Anzahl der Einwohner: "))
ergebnis = neu/wohnerZahl * 100_000
print(f"Ergebnis: {ergebnis}")