from ingredients import pokazaty_ingredienty
from potions import pokazaty_zillia


def pokazaty_inventari(ingredienty, zillia):
    print("\n========== ІНВЕНТАР ==========")
    print("1. Інгредієнти")
    print("2. Зілля")
    try:
        vybir = int(input("Що показати? "))
        if vybir == 1:
            pokazaty_ingredienty(ingredienty)
        elif vybir == 2:
            pokazaty_zillia(zillia)
        else:
            print("Такого пункту немає.")
    except ValueError:
        print("Введи число.")
