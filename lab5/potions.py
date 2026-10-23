from ingredients import INGREDIENTS

# 50 видів зіль. Для кожного рецепта потрібно два інгредієнти.
POTION_NAMES = [
    "Зілля здоров'я", "Зілля мани", "Зілля сили", "Зілля спритності",
    "Зілля мудрості", "Зілля невидимості", "Зілля вогню", "Зілля льоду",
    "Зілля отрути", "Зілля очищення", "Зілля удачі", "Зілля сну",
    "Зілля швидкості", "Зілля захисту", "Зілля витривалості", "Зілля зору",
    "Зілля правди", "Зілля спокою", "Зілля люті", "Зілля легкості",
    "Зілля тіні", "Зілля світла", "Зілля грому", "Зілля землі",
    "Зілля повітря", "Зілля води", "Зілля відновлення", "Зілля молодості",
    "Зілля пам'яті", "Зілля забуття", "Зілля хоробрості", "Зілля тепла",
    "Зілля холоду", "Зілля сновидінь", "Зілля захисту від магії",
    "Зілля проти прокляття", "Зілля духу", "Зілля енергії",
    "Зілля концентрації", "Зілля спритних рук", "Зілля кам'яної шкіри",
    "Зілля морської сили", "Зілля лісу", "Зілля місяця", "Зілля сонця",
    "Зілля зірок", "Зілля дракона", "Зілля фенікса",
    "Зілля безсмертя", "Еліксир короля"
]

POTIONS = {}
for i, nazva in enumerate(POTION_NAMES):
    POTIONS[i + 1] = {
        "nazva": nazva,
        "retsept": [INGREDIENTS[(i * 2) % 20], INGREDIENTS[(i * 2 + 1) % 20]],
        "tsina": 80 + i * 15
    }


def pokazaty_recepty():
    print("\n--- КНИГА РЕЦЕПТІВ ---")
    for nomer, zillia in POTIONS.items():
        sklad = " + ".join(zillia["retsept"])
        print(f"{nomer}. {zillia['nazva']} | {sklad} | ціна: {zillia['tsina']} золота")


def zvaryty_zillia(ingredienty, zillia_inventar):
    pokazaty_recepty()
    try:
        nomer = int(input("Введи номер зілля (0 — назад): "))
        if nomer == 0:
            return
        if nomer not in POTIONS:
            print("Такого рецепта немає.")
            return

        zillia = POTIONS[nomer]
        nazva = zillia["nazva"]

        if nazva not in zillia_inventar and len(zillia_inventar) >= 10:
            print("Інвентар зіль повний: усі 10 слотів зайняті.")
            return
        if nazva in zillia_inventar and zillia_inventar[nazva] >= 10:
            print("У цьому слоті вже максимальна кількість зіль (10).")
            return

        potribni = zillia["retsept"]
        for ingredient in potribni:
            if ingredient not in ingredienty or ingredienty[ingredient] < 1:
                print(f"Не вистачає інгредієнта: {ingredient}")
                return

        for ingredient in potribni:
            ingredienty[ingredient] -= 1
            if ingredienty[ingredient] == 0:
                del ingredienty[ingredient]

        zillia_inventar[nazva] = zillia_inventar.get(nazva, 0) + 1
        print(f"Ти зварила: {nazva}!")
    except ValueError:
        print("Введи номер рецепта числом.")
    except (KeyError, TypeError):
        print("Сталася помилка під час варіння зілля.")


def pokazaty_zillia(inventar):
    print("\n--- ІНВЕНТАР ЗІЛЬ ---")
    if not inventar:
        print("Поки немає жодного зілля.")
        return
    for i, (nazva, kilkist) in enumerate(inventar.items(), start=1):
        print(f"{i}. {nazva} — {kilkist}/10")
    print(f"Зайнято слотів: {len(inventar)}/10")
