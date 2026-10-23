MAX_DNIV = 30
TSIL_ZOLOTA = 10000


def pereviryty_kinec(dien, zoloto, zillia):
    """Повертає win, lose або None."""
    if zoloto >= TSIL_ZOLOTA and "Еліксир короля" in zillia:
        return "win"
    if dien > MAX_DNIV:
        return "lose"
    return None


def pokazaty_stan(dien, zoloto):
    print("\n" + "=" * 40)
    print(f"День: {dien}/{MAX_DNIV} | Золото: {zoloto}")
    print("=" * 40)


def kintsiwka(rezultat):
    if rezultat == "win":
        print("\nВІТАЄМО! Ти створила Еліксир короля та зібрала 10 000 золота.")
        print("Король зробив тебе головною алхімікинею королівства. ТИ ПЕРЕМОГЛА!")
    else:
        print("\nМинуло 30 днів, а завдання короля не виконано.")
        print("Ти втратила звання придворної алхімікині. ГРУ ЗАВЕРШЕНО.")
