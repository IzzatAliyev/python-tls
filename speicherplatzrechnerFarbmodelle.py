class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'

def chooseFabrModelle():
    try:
        farbModell = input(Colors.BLUE + "Wählen Sie ein Farbmodell aus: " + Colors.RESET)
        match farbModell:
            case '1': return 3
            case '2': return 4
            case '3': return 3
            case '4': return 3
            case '5': return 3
            case '6': return 1
        raise Exception(Colors.RED + 'Wählen Sie bitte ein vorhandenen Farbmodell aus: ' + Colors.RESET)
    except Exception as ex:
        print(Colors.RED + str(ex) + Colors.RESET)
        chooseFabrModelle();

try:
    bildhoehe = int(input(Colors.BLUE + "Geben Sie die Bildhöhe in Pixeln ein: " + Colors.RESET))
    bildbreite = int(input(Colors.BLUE + "Geben Sie die Bildbreite in Pixeln ein: " + Colors.RESET))
    print(Colors.CYAN + '''
          Farbmodelle
          (1) RGB;
          (2) CMYK;
          (3) HSB/HSV;
          (4) LAB;
          (5) YCbCr;
          (6) Grayscale;
          (0) EXIT;
          ''' + Colors.RESET)
    
    speicherbedarf_pro_pixel = chooseFabrModelle();
    anzahl_bilder = int(input(Colors.BLUE + "Geben Sie die Anzahl der Bilder ein: " + Colors.RESET))

    speicherbedarf = bildhoehe * bildbreite * speicherbedarf_pro_pixel * anzahl_bilder
    speicherbedarf_gibibyte = speicherbedarf / (1024 * 1024 * 1024)

    print(f"{Colors.GREEN}Der Speicherbedarf beträgt {speicherbedarf_gibibyte:.4f} GiB.{Colors.RESET}")
except Exception as e:
    print(e)
