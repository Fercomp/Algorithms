def check_if_subset(list1, list2):
    n = len(list1)
    m = len(list2)
    has_match = False

    # This n - m avoid test when is not already possible to have list2 as subset
    # The + 1 is important to include the case where list2 is the sufix of list1
    for i in range(n - m + 1):
        if list1[i] == list2[0]:
            has_match = True
            
            for j in range(m):
                if list1[i + j] != list2[j]:
                    has_match = False
                    break

    return has_match

def check_if_subset2(list1, list2):
    n, m = len(list1), len(list2)
    # 'any' returns True if at least one comparison is True
    # list1[i:i + m] creates a slice of length m starting at index i
    # We check all possible slices of list1 with length m and compare them to list2
    # If any of them is equal to list2, the function returns True
    return any(list1[i:i + m] == list2 for i in range(n - m + 1))


print(check_if_subset([0, 1, 2, 3], [1,2]))