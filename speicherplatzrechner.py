try:
    bildhoehe = int(input("Geben Sie die Bildhöhe in Pixeln ein: "))
    bildbreite = int(input("Geben Sie die Bildbreite in Pixeln ein: "))
    speicherbedarf_pro_pixel = float(input("Geben Sie den Speicherbedarf pro Pixel in Byte ein: "))
    anzahl_bilder = int(input("Geben Sie die Anzahl der Bilder ein: "))

    speicherbedarf = bildhoehe * bildbreite * speicherbedarf_pro_pixel * anzahl_bilder
    speicherbedarf_gibibyte = speicherbedarf / (1024 * 1024 * 1024)

    print(f"Der Speicherbedarf beträgt {speicherbedarf_gibibyte:.4f} GiB.")
except Exception as e:
    print(e)
