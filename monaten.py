def getMonthWithGivenNumber(num):
    match num:
        case 1: print('Jan')
        case 2: print('Feb')
        case 3: print('Mär')
        case 4: print('Apr')
        case 5: print('Mai')
        case 6: print('Jun')
        case 7: print('Jul')
        case 8: print('Aug')
        case 9: print('Sep')
        case 10: print('Okt')
        case 11: print('Nov')
        case 12: print('Dez')
        case _: print('passt nicht')
        
monat = int(input('Geben Sie Monat ein: '))
getMonthWithGivenNumber(monat)