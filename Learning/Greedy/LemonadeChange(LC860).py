def lemonadeChange(bills):
    total = 0
    for b in bills:
        if b != 5:
            change = b - 5
            if change > total:
                return False
        total += 5
    return True

lemonadeChange([5,5,10,10,20])