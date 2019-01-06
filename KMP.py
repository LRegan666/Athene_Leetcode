def prefix_compute(p):
    k, m = 0, len(p)
    pi = [0]*m
    for q in range(1, m):
        while k > 0 and p[k] != p[q]:
            k = pi[k-1]
        if p[k] == p[q]:
            k += 1
        pi[q] = k
    return pi


def kmp_matcher(s, p):
    start_index_lists = []
    pi = prefix_compute(p)
    ls, lp = len(s), len(p)
    k = 0
    for i in range(ls):
        while k > 0 and p[k] != s[i]:
            k = pi[k-1]
        if p[k] == s[i]:
            k += 1
        if k == lp:
            ind = i - k + 1
            start_index_lists.append(ind)
            k = pi[k-1]
    return start_index_lists


if __name__ == '__main__':
    s = 'bbacbababacaddeababaca'
    p = 'ababaca'
    res = kmp_matcher(s, p)
    print(res)

