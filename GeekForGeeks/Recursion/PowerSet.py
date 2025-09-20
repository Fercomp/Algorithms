l = [1, 2, 3, 1]

# I will call this techinique take and not take, 
# fist we take an option and call recursively and after return we
# don't take the option so we will try all possiblities
def power_set(l, i, r):
    if i == len(l):
        print(r)
        return
    
    r.append(l[i])
    power_set(l, i+1, r)
    # Is very very important to remove because the previus call is waiting a array
    # with the original r, and if you added in this call you need to remove
    r.pop()
    power_set(l, i+1, r)

def sum_k(l, i, k, r):
    if sum(r) == k:
        print(r)
        return
    
    if i == len(l):
        return
    
    r.append(l[i])
    sum_k(l, i+1, k, r)
    r.pop()
    sum_k(l, i+1, k, r)
    
sum_k(l, 0, 2, [])