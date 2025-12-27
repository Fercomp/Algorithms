# vjudge.net/problem/UVA-11661
import math

while True:
    l = int(input())
    if l == 0:
        break
    
    street = input()
    minimun_distance = math.inf
    last_restaurant = -1
    last_drug_store = -1
    
    was_z = False
    for index, element in enumerate(street):
        # Early exit
        if element == "Z":
            print(0)
            was_z = True
            break
        
        if element == "D":
            last_drug_store = index
            if last_restaurant != -1:
                minimun_distance = min(minimun_distance, index - last_restaurant)
                    
        if element == "R":
            last_restaurant = index
            if last_drug_store != -1:
                minimun_distance = min(minimun_distance, index - last_drug_store)
    
    if not was_z:
        print(minimun_distance)