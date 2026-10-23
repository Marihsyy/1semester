from potions import POTIONS


def prodaty_zillia(inventar, zoloto):
    if not inventar:
        print("У тебе немає зіль для продажу.")
        return zoloto

    ceny = {z["nazva"]: z["tsina"] for z in POTIONS.values()}
    print("\n--- ПРОДАЖ ЗІЛЬ ---")
    for i, (nazva, kilkist) in enumerate(inventar.items(), start=1):
        print(f"{i}. {nazva} — {kilkist} шт. | {ceny.get(nazva, 50)} золота за штуку")
    print("0. Назад")

    try:
        vybir = int(input("Яке зілля продати? "))
        if vybir == 0:
            return zoloto
        spysok = list(inventar.items())
        if vybir < 1 or vybir > len(spysok):
            print("Неправильний номер.")
            return zoloto

        nazva, kilkist = spysok[vybir - 1]
        prodaty = int(input(f"Скільки продати (1-{kilkist})? "))
        if prodaty < 1 or prodaty > kilkist:
            print("Неправильна кількість.")
            return zoloto

        tsina = ceny.get(nazva, 50)
        zarobitok = tsina * prodaty
        inventar[nazva] -= prodaty
        if inventar[nazva] == 0:
            del inventar[nazva]
        zoloto += zarobitok
        print(f"Продано {prodaty} шт. Отримано {zarobitok} золота.")
        print(f"Тепер у тебе {zoloto} золота.")
        return zoloto
    except ValueError:
        print("Потрібно вводити числа.")
        return zoloto
    except (KeyError, TypeError):
        print("Не вдалося продати зілля.")
        return zoloto
