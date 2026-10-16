from tabulate import tabulate

def demo_tabulate():
    data = [
        ["Alina", 12],
        ["Maria", 10],
        ["Oleh", 11]
    ]

    print(tabulate(data, headers=["Name", "Grade"]))