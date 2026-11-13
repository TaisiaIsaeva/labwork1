def bin_search(p, a, l, r):
    m=(l+r)//2
    while l<r :
        m = (l+r)//2
        print(l, r, m)
        if a[m] == p:
            return True
        if a[m]>p:
            return bin_search(p, a, l, m)
        if a[m]<p:
            return bin_search(p, a, m+1, r)
    return False

a=[2, 3, 4, 5]
print( bin_search(0, a, 0, 3) )
