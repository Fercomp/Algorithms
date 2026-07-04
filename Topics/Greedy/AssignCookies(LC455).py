def findContentChildren(g, s):
    g.sort()
    s.sort()
    count = 0
    g_index = 0
    s_index = 0
    while g_index < len(g) and s_index < len(s):
        if g[g_index] <= s[s_index]:
            count += 1
            g_index += 1
            s_index += 1
        else:
            s_index += 1
    return count