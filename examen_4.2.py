match opcion :
    case 1:
        resultado = cantidad / 17.5
        moneda = "USD"
    case 2:
        resultado = cantidad / 19.2
        moneda = "EUR"
    case 3:
        resultado = cantidad / 0.52
        moneda = "THB"
    case 4:
        resultado = cantidad / 0.12
        moneda = "JPY"
    case 5:
        resultado = cantidad / 0.013
        moneda = "KRW"
    case 6:
        resultado = cantidad / 11.5
        moneda = "AUD"
    case 7:
        resultado = cantidad / 4.6
        moneda = "PEN"
    case 8:
        resultado = cantidad / 12.8
        moneda = "CAD"
    case 9:
        resultado = cantidad / 0.48
        moneda = "VES"
    case 10:
        resultado = cantidad / 0.02
        moneda = "ARS"
    case _:
        print("Opción no válida")
        resultado = None