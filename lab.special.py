def bin_search(p, a, l, r):
    m=(l+r)//2
    while l<r :
        m = (l+r)//2
        if a[m] == p:
            return True
        if a[m]>p:
            return bin_search(p, a, l, m)
        if a[m]<p:
            return bin_search(p, a, m+1, r)
    return False

a= list(map(int, input('Введите числа массива в порядке возрастания \n').split( )))
p = int(input('Введите число для поиска \n'))

if bin_search(p, a, 0, len(a)):
    print('Число есть в массиве')
else:
    print('Такого числа в массиве нет')