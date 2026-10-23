from ingredients import INGREDIENTS, otrymaty_ingredienty, pokazaty_ingredienty
from potions import POTIONS, zvaryty_zillia, pokazaty_zillia
from inventory import pokazaty_inventari
from shop import prodaty_zillia
from game import MAX_DNIV, pereviryty_kinec, pokazaty_stan, kintsiwka


def holovne_menu():
    print("\n1. Подивитися інвентар")
    print("2. Зварити зілля")
    print("3. Продати зілля")
    print("4. Завершити день")
    print("5. Подивитися всі рецепти")
    print("0. Вийти з гри")


def main():
    ingredienty = {}
    zillia = {}
    zoloto = 100
    den = 1

    print("=" * 45)
    print("       RPG: ПРИГОДИ АЛХІМІКИНІ")
    print("=" * 45)
    print(f"У грі є {len(INGREDIENTS)} інгредієнтів і {len(POTIONS)} видів зіль.")
    print("Завдання: за 30 днів отримати 10 000 золота та створити Еліксир короля.")
    print("На початку кожного дня ти отримуєш 5 випадкових інгредієнтів.")

    otrymaty_ingredienty(ingredienty)

    while den <= MAX_DNIV:
        pokazaty_stan(den, zoloto)
        holovne_menu()

        try:
            vybir = int(input("Обери дію: "))

            if vybir == 1:
                pokazaty_inventari(ingredienty, zillia)
            elif vybir == 2:
                zvaryty_zillia(ingredienty, zillia)
            elif vybir == 3:
                zoloto = prodaty_zillia(zillia, zoloto)
            elif vybir == 4:
                den += 1
                if den <= MAX_DNIV:
                    print(f"\nПочинається день {den}!")
                    otrymaty_ingredienty(ingredienty)
            elif vybir == 5:
                from potions import pokazaty_recepty
                pokazaty_recepty()
            elif vybir == 0:
                print("Ти вийшла з гри.")
                return
            else:
                print("Такого пункту немає. Спробуй ще раз.")

            rezultat = pereviryty_kinec(den, zoloto, zillia)
            if rezultat:
                kintsiwka(rezultat)
                return

        except ValueError:
            print("Помилка! Введи номер пункту числом.")
        except (KeyError, TypeError):
            print("Сталася помилка. Спробуй ще раз.")

    kintsiwka("lose")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nГру зупинено.")
    except Exception as error:
        print(f"Непередбачена помилка: {error}")
