from faker import Faker

def demo_faker():
    fake = Faker()
    print("[faker] Random name:", fake.name())