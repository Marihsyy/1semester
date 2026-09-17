users = {
    "maria": {
        "password": "1234",
        "grades": [12, 10, 8, 11, 9, 4, 7, 12]
    },
    "anna": {
        "password": "2345",
        "grades": [10, 9, 6, 8, 11, 5, 3]
    },
    "oleh": {
        "password": "5678",
        "grades": [12, 11, 10, 7, 4, 3, 9]
    },
    "maksym": {
        "password": "1111",
        "grades": [8, 9, 5, 6, 10, 12, 2, 4]
    }
}


login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in users and users[login]["password"] == password:
    print("\nВхід виконано успішно!")
    grades = users[login]["grades"]
    
    print("Ваші оцінки:", grades)
    
    good = 0
    bad = 0

    for grade in grades:
        if 5 <= grade <= 12:
            good += 1
        elif 1 <= grade <= 4:
            bad += 1

    print("Кількість оцінок від 5 до 12:", good)
    print("Кількість оцінок від 1 до 4:", bad)
else:
    print("Неправильний логін або пароль!")


