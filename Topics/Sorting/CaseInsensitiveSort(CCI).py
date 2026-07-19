def case_insensitive_sort(strings):
    return sorted(strings, key= lambda x: x.lower(), reverse=True)