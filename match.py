a = int(input("num: "))

match a:
    case _ if a < 42:
        print('Less')
    case _ if a == 42:
        print('The answer')
    case _ if a > 42:
        print('Greater')