import random

# 200 різних інгредієнтів
OSNOVY = [
    "М'ята", "Ромашка", "Лаванда", "Шавлія", "Кропива",
    "Полин", "Чебрець", "Валеріана", "Меліса", "Папороть",
    "Корінь мандрагори", "Корінь імбиру", "Корінь женьшеню", "Корінь солодки",
    "Біла троянда", "Чорна троянда", "Сонячна квітка", "Місячна квітка",
    "Зоряна лілія", "Кришталева орхідея", "Вогняний мак", "Крижаний лотос",
    "Драконяча луска", "Феніксове перо", "Єдиноріжий волос", "Грифоняче перо",
    "Пилок феї", "Пилок ельфа", "Павутиння тіні", "Пелюстка світанку",
    "Пелюстка заходу", "Сльоза русалки", "Вода з джерела", "Роса світанку",
    "Крапля дощу", "Снігова крихта", "Лід з печери", "Попіл фенікса",
    "Вулканічний попіл", "Зола дуба", "Морська сіль", "Чорний пісок",
    "Золотий пісок", "Місячний пил", "Зоряний пил", "Кристал кварцу",
    "Рубінова крихта", "Сапфірова крихта", "Смарагдова крихта", "Аметистова крихта"
]

OSNOVY = (OSNOVY * 4)[:200]
INGREDIENTS = [f"{name} {i // 50 + 1}" for i, name in enumerate(OSNOVY)]
# Перші 20 інгредієнтів частіше трапляються, щоб гравець міг варити зілля.
COMMON_INGREDIENTS = INGREDIENTS[:20]


def dodaty_ingredient(inventar, nazva, kilkist=1, limit_slotiv=25, limit_staka=25):
    """Додає інгредієнти, не перевищуючи ліміт слотів і стаку."""
    try:
        if nazva in inventar:
            dodaty = min(kilkist, limit_staka - inventar[nazva])
            inventar[nazva] += dodaty
            return kilkist - dodaty
        if len(inventar) >= limit_slotiv:
            return kilkist
        dodaty = min(kilkist, limit_staka)
        inventar[nazva] = dodaty
        return kilkist - dodaty
    except (TypeError, ValueError):
        print("Помилка під час додавання інгредієнта.")
        return kilkist


def otrymaty_ingredienty(inventar, kilkist=5):
    """Щодня видає 5 випадкових інгредієнтів."""
    try:
        vybrani = random.choices(COMMON_INGREDIENTS, k=kilkist)
        print("\nСьогодні ти знайшла:")
        for nazva in vybrani:
            ne_dodano = dodaty_ingredient(inventar, nazva)
            if ne_dodano:
                print(f"Не вдалося додати {nazva}: немає місця або стак заповнений.")
            else:
                print(f"+ {nazva}")
    except (TypeError, ValueError):
        print("Не вдалося отримати інгредієнти.")


def pokazaty_ingredienty(inventar):
    print("\n--- ІНВЕНТАР ІНГРЕДІЄНТІВ ---")
    if not inventar:
        print("Інвентар порожній.")
        return
    for i, (nazva, kilkist) in enumerate(inventar.items(), start=1):
        print(f"{i}. {nazva} — {kilkist}/25")
    print(f"Зайнято слотів: {len(inventar)}/25")
