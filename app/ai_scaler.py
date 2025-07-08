import random
def calculate_price():
    base=499
    u=random.randint(400,1500)
    return base* (2 if u>1000 else (1.5 if u>700 else 1))
