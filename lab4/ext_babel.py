from babel.numbers import format_currency

def demo_babel():
    result = format_currency(1250, "UAH", locale="uk_UA")
    print("[babel] Price:", result)