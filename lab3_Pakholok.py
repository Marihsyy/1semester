kataloh = {
    1: {"nazva": "Noutbuk", "tsina": 25000.0, "zalyshok": 5},
    2: {"nazva": "Myshka", "tsina": 650.5, "zalyshok": 20},
    3: {"nazva": "Klaviatura", "tsina": 1200.0, "zalyshok": 10}}
koshyk = {}
format_tsina = lambda tsina: f"{tsina:.2f}hrn"
def pokazaty(admn: bool = False) -> None:
    print("\n--- Spysok tovariv ---")
    spysok_id = [1, 2, 3]
    rezultat_map = map(lambda tovar_id: tovar_id, spysok_id)

    for tovar_id in list(rezultat_map):
        tovar = kataloh[tovar_id]
        riadok = f"ID: {tovar_id} | {tovar['nazva']} | {format_tsina(tovar['tsina'])}"
        if admn == True:
            riadok = riadok + f" |Na skladi: {tovar['zalyshok']} sht."
        print(riadok)
    
def dodaty() -> None:
    pokazaty(admn=False)
    idx = int(input("\nVvedit ID tovaru: "))
    q = int(input("Vvedit kilkist: "))
    
    if idx in kataloh:
        tovar = kataloh[idx]
        if tovar["zalyshok"] >= q:
            if idx in koshyk:
                koshyk[idx] = koshyk[idx] + q
            else:
                koshyk[idx] = q
            print("Uspishno dodano!")
        else:
            print("Nemaie stilky na skladi!")
    else:
        print("Tovar ne znaideno!")

def koshyk_info() -> float:
    print("\n--- Vash koshyk ---")
    zahalna_vartist = 0.0
    for idx in koshyk:
        tovar = kataloh[idx]
        kilkist = koshyk[idx]
        vartist_tovaru = tovar["tsina"] * kilkist
kataloh = {
    1: {"nazva": "Noutbuk", "tsina": 25000.0, "zalyshok": 5},
    2: {"nazva": "Myshka", "tsina": 650.5, "zalyshok": 20},
    3: {"nazva": "Klaviatura", "tsina": 1200.0, "zalyshok": 10}}
koshyk = {}
format_tsina = lambda tsina: f"{tsina:.2f}hrn"
def pokazaty(admn: bool = False) -> None:
    print("\n--- Spysok tovariv ---")
    spysok_id = [1, 2, 3]
    rezultat_map = map(lambda tovar_id: tovar_id, spysok_id)
    for tovar_id in list(rezultat_map):
        tovar = kataloh[tovar_id]
        riadok = f"ID: {tovar_id} | {tovar['nazva']} | {format_tsina(tovar['tsina'])}"
        if admn == True:
            riadok = riadok + f" | Na skladi: {tovar['zalyshok']} sht."
        print(riadok)
def dodaty() -> None:
    pokazaty(admn=False)
    idx = int(input("\nVvedit ID tovaru: "))
    q = int(input("Vvedit kilkist: "))
    if idx in kataloh:
        tovar = kataloh[idx]
        if tovar["zalyshok"] >= q:
            if idx in koshyk:
                koshyk[idx] = koshyk[idx] + q
            else:
                koshyk[idx] = q
            print("Uspishno dodano!")
        else:
            print("Nemaie stilky na skladi!")
    else:
        print("Tovar ne znaideno!")
def koshyk_info() -> float:
    print("\n--- Vash koshyk ---")
    zahalna_vartist = 0.0
    for idx in koshyk:
        tovar = kataloh[idx]
        kilkist = koshyk[idx]
        vartist_tovaru = tovar["tsina"] * kilkist
        zahalna_vartist = zahalna_vartist + vartist_tovaru
        print(f"{tovar['nazva']} x {kilkist} sht. = {format_tsina(vartist_tovaru)}")

    print(f"Vsioho do splaty: {format_tsina(zahalna_vartist)}")
    return zahalna_vartist
def vydalyty() -> None:
@@ -62,7 +57,6 @@ def kupyty() -> None:
               kataloh[idx]["zalyshok"] = kataloh[idx]["zalyshok"] - kilkist
           koshyk.clear()
           print("Diakuiemo za pokupku!")

def admin(*args, **kwargs) -> None:
    parol = input("\nVvedit parol admina: ")
    if parol == kwargs["pwd"]:
@@ -72,16 +66,15 @@ def admin(*args, **kwargs) -> None:
        print("Nevernyi parol!")
menu = {"1": lambda: pokazaty(admn=False), "2": lambda: dodaty(), "3": lambda: koshyk_info(), "4": lambda: vydalyty(),
        "5": lambda: kupyty(), "6": lambda: admin("Vkhid_Admina", pwd="777"), "7": lambda: exit()}

def main() -> None:
    while True:
        print("\n========== MENIU ==========")
        print("1. Kataloh | 2. Dodaty v koshyk | 3. Perehliad koshyka")
        print("4. Vydalyty z koshyka | 5. Kupyty | 6. Admin Panel | 7. Vykhid")

        vybir = input("Oberit diiu (1-7): ")
        if vybir in menu:
            menu[vybir]()
        else:
            print("Nevirnyi vybir!")
if __name__ == "__main__":
    main()
